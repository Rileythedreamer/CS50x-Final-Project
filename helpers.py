import requests
from cs50 import SQL
from flask import redirect, render_template, session, url_for
from functools import wraps

db = SQL("sqlite:///database.db")

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function




def get_cart_details(user_id):
    # Query for cart items and product details
    cart_items = db.execute(
        """SELECT
        cart_items.id AS cart_item_id,
        cart_items.user_id AS user_id,
        cart_items.quantity AS item_quantity,
        cart_items.added_at AS added_at,
        product_variants.id AS variant_id,
        product_variants.size AS variant_size,
        product_variants.color AS variant_color,
        product_variants.stock AS variant_stock,
        products.id AS product_id,
        products.name AS product_name,
        products.description AS product_description,
        products.price AS product_price,
        products.category_id AS category_id,
        products.image_url AS image_url,
        products.stock AS product_stock,
        products.created_at AS product_created_at,
        products.updated_at AS product_updated_at
        FROM cart_items
        JOIN product_variants ON cart_items.product_variant_id = product_variants.id
        JOIN products ON product_variants.product_id = products.id
        WHERE cart_items.user_id = ?""",
        user_id
    )

    # Calculate subtotals and total price
    subtotals = []
    for cart_item in cart_items:
        subtotals.append(float(cart_item["product_price"]) * int(cart_item["item_quantity"]))

    for cart_item, subtotal in zip(cart_items, subtotals):
        cart_item["subtotal"] = subtotal

    n_items = total_price = 0
    for cart_item in cart_items:
        n_items += int(cart_item["item_quantity"])
        total_price += int(cart_item["item_quantity"]) * float(cart_item["product_price"])

    return cart_items, n_items, total_price
