import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, get_cart_details
# from flask import Flask, flash, redirect, render_template, request, session 



# Configure application
app = Flask(__name__)
app.secret_key = '16c0a17ee38d04c3a6c57931a4c53e159cf019de683c87b6' 

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



db = SQL("sqlite:///database.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        """Register user"""
        # 1. check for valid inputs
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
        if not request.form.get("email"):
            return apology("must enter your email", 400)
        if (not request.form.get("first_name")) or (not request.form.get("last_name")):
            return apology("must provide first and last name")


        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match confirmation", 400)

        hashed_pass = generate_password_hash(request.form.get("password"))

        # try inserting the new username into the database
        try:
            value = db.execute(
                "INSERT INTO users (username, hash, email, first_name, last_name) VALUES (?, ?, ?, ?, ?)",
                request.form.get("username"), hashed_pass, request.form.get("email"), request.form.get("first_name"), request.form.get("last_name")
            )
        except ValueError:
            return apology(message = "username already taken", code = 400)

        new_user = db.execute(
            "SELECT id FROM users WHERE username = ?", request.form.get("username")
        )

        session["user_id"] = new_user[0]["id"]

        return redirect("/")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
          # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = int(rows[0]["id"])


        # Redirect user to home page
        return redirect("/")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/product" , methods=["GET", "POST"])
def product():
    if request.method == "GET":
        
        return render_template("product.html")
    else:
        product_id = request.form.get("product_id")
        if not product_id:
            product_id = request.args.get("product_id")
        product_id = int(product_id)
        if not product_id:
            return apology("Product not found", 404)

        action = request.form.get("action")
        if action == "viewdetail":
            product = db.execute(
                "SELECT * FROM products WHERE id = ?",
                product_id
            )
            variants = db.execute(
                "SELECT * FROM product_variants WHERE product_id = ?",
                product_id
            )
            return render_template("product.html", product = product[0], variants = variants)
        elif action == "remove":
            role_row = db.execute(
                """SELECT role FROM users 
                WHERE id = ? 
                """, session["user_id"]
            )
            role = role_row[0]["role"]
            if not role != "owner":
                flash("permission denied", "error")
                return redirect("/shop")
            db.execute("""
                    DELETE FROM cart_items
                    WHERE product_variant_id IN (
                        SELECT id FROM product_variants
                        WHERE product_id = ?
                    )
                """, product_id)
            db.execute(
                """DELETE FROM product_variants WHERE product_id = ?""",
                product_id
            )
            db.execute(
                "DELETE FROM products WHERE id = ?",
                product_id
            )
        return redirect("/shop")



@app.route("/add_to_cart", methods=["GET", "POST"])
@login_required
def addtocart():
    if request.method =="POST":
        # product_id = int(request.form.get("product_id"))
        product_id = request.args.get("product_id") or request.form.get("product_id")
        product_name = request.form.get("product_name")
        price = request.form.get("price")
        quantity = request.form.get("quantity")
        color = request.form.get("color")
        size = request.form.get("size")

        product_id = int(product_id)
        variant_id_rows = db.execute(
            """SELECT id FROM product_variants
            WHERE product_id = ? AND size = ? AND color = ?""",
            product_id, size, color

        )
        if not variant_id_rows:
            flash("This item is not available", "error")
            return redirect("/cart")
        variant_id = variant_id_rows[0]["id"]
        # when the form is submitted the information
        # of the product must be inserted into the sql database

        db.execute(
            """INSERT INTO cart_items
            (user_id, product_variant_id, quantity)
            VALUES (?, ?, ?) """,
            session["user_id"], variant_id, quantity
        )
        return redirect("/cart")




@app.route('/shop')
def shop():
    # extract products from database
    products = db.execute("SELECT * FROM products")

    if "user_id" in session:
        row = db.execute("SELECT role FROM users WHERE id = ?",
                            session["user_id"])
        role = row[0]["role"]
        if role == 'owner':
            isowner = True
        else:
            isowner = False
        return render_template("shop.html", products = products, isowner = isowner)
    else:
        isowner = False

    return render_template("shop.html", products = products, isowner = isowner)


@app.route('/checkout', methods=["GET"])
@login_required
def checkout():
    cart_details = get_cart_details(session["user_id"])
    return render_template("checkout.html",
                            cart_items = cart_details[0], n_items = cart_details[1], total_price = cart_details[2])

    
    
        
@app.route('/place-order', methods=["GET", "POST"])
@login_required
def place_order():
    buyer = session["user_id"]
    buyer_name = request.form.get("name")
    email = request.form.get("email")
    address = request.form.get("address")
    city = request.form.get("city")
    state = request.form.get("state")
    zip_code = request.form.get("zip-code")
    payment_method = request.form.get("payment_method")

    cart_items, n_items, total_price = get_cart_details(buyer)
    
    order_id = db.execute("""
    INSERT INTO orders (
        user_id, full_name, email, address, city, state, zip, payment_method, total_price
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, buyer, buyer_name, email, address, city, state, zip_code, payment_method, total_price)

    # update orders table using buyer's cart
    for item in cart_items:
        db.execute("""
            INSERT INTO order_items (
                order_id, product_variant_id, quantity, price
            ) VALUES (?, ?, ?, ?)
        """, order_id, item["variant_id"], item["item_quantity"], item["product_price"])

        # Update product_variant stock
        db.execute("""
            UPDATE product_variants
            SET stock = stock - ?
            WHERE id = ?
        """, item["item_quantity"], item["variant_id"])

        # update product stock
        db.execute("""
            UPDATE products
            SET stock = stock - ?
            WHERE id = ?
        """, item["item_quantity"], item["product_id"])

    # clear cart when order is placed 
    db.execute("DELETE FROM cart_items WHERE user_id = ?", buyer)
    
    order_list = db.execute("""
                       SELECT * FROM orders 
                       WHERE
                       user_id = ?
                       AND
                       id = ?""", 
                       session["user_id"], 
                       order_id)
    if order_list:
        order = order_list[0]
    else:
        return "order not found", 404
    items = db.execute("""
                       SELECT * FROM order_items
                       WHERE
                       order_id = ?""",  
                       order_id)
    return render_template("confirmation.html", order = order, items= items)


    


@app.route('/cart', methods=["POST", "GET"])
@login_required
def cart():
    if request.method == "GET":
        cart_details = get_cart_details(session["user_id"])
        return render_template("cart.html",
                               cart_items = cart_details[0], n_items = cart_details[1], total_price = cart_details[2])

@app.route('/remove', methods = ["GET", "POST"])
@login_required
def remove():
    ## remove item from database's cart_items table
    if request.method == "POST":
        product_variant_id = request.form.get("variant_id")
        # print(product_variant_id)
        rows = db.execute(
            """DELETE FROM cart_items
            WHERE product_variant_id = ?""",
            product_variant_id
        )
        # print(rows)
    return redirect("/cart")

@app.route('/wishlist')
@login_required
def wishlist():
    return render_template("wishlist.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/ownerdashboard')
@login_required
def owner():
    categories = db.execute(
        "SELECT * FROM categories"
    )
    return render_template("ownerdash.html", categories = categories)


@app.route('/dashboard')
@login_required
def dashboard():
    id = session["user_id"]
    rows = db.execute(
        "SELECT first_name, last_name FROM users WHERE id = ?", id
    )
    # print(len(rows))
    # print(rows)
    name = f"{rows[0]["first_name"].capitalize()} {rows[0]["last_name"].capitalize()}"
    return render_template("dashboard.html", name = name)

@app.route('/orders')
@login_required
def display_orders():
    all_orders = db.execute("""
                    SELECT * FROM orders 
                    WHERE 
                    user_id = ?
                    """,
                    session["user_id"]
                    )
    return render_template("orders.html", orders = all_orders)

@app.route("/addproduct", methods=["GET", "POST"])
def addproduct():
    if request.method == "POST":
        required_fields = ["name", "description", "price", "category_id", "stock"]

        # print("Form data received:", request.form)
        # Check if all required fields are present
        missing_fields = [field for field in required_fields if not request.form.get(field)]

        # print("Missing fields:", missing_fields)

        if missing_fields:
            flash(f"Missing fields: {', '.join(missing_fields)}", "error")
            return redirect("/ownerdashboard")  # Redirect back to the form page

        # Get form data
        product_name = request.form.get("name")
        product_id = request.form.get("id")
        description = request.form.get("description")
        price = float(request.form.get("price"))
        discount = request.form.get("discount_price")
        category_id = int(request.form.get("category_id"))
        stock = int(request.form.get("stock"))
        image_file = request.files.get("image")

        # get variants data
        variant_sizes = request.form.getlist("variant_size[]")
        variant_colors = request.form.getlist("variant_color[]")
        variant_stocks = request.form.getlist("variant_stock[]")

        # print("Sizes:", variant_sizes)
        # print("Colors:", variant_colors)
        # print("Stocks:", variant_stocks)

        if not (len(variant_sizes) == len(variant_colors) == len(variant_stocks)):
            return apology("Mismatch in variant inputs. Please check and try again.", "error")

            # since i haven't done this kind of thing before 
            #  all image handling code was written with chatgpt's help.
            # from here
        if not image_file:
            print("No file uploaded.")
            flash("No file uploaded.", "error")
        elif not image_file.filename:
            print("File uploaded but filename is empty.")
            flash("File uploaded but filename is empty.", "error")
        else:
            print(f"Uploaded file: {image_file.filename}")

        # Check UPLOAD_FOLDER
        print(f"UPLOAD_FOLDER: {app.config['UPLOAD_FOLDER']}")
        if not os.path.exists(app.config["UPLOAD_FOLDER"]):
            print("Upload folder does not exist. Creating it now.")
            os.makedirs(app.config["UPLOAD_FOLDER"])

        # Secure filename
        filename = image_file.filename
        print(f"Secure filename: {filename}")

        # File path
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        print(f"File will be saved to: {file_path}")

        # Save the file
        try:
            image_file.save(file_path)
            print(f"File successfully saved at: {file_path}")
        except Exception as e:
            print(f"Error saving file: {e}")
            flash("Error saving the file. Please try again.", "error")
        # upto here

        # Insert into database
        if discount:
            db.execute(
                """INSERT INTO products
                (name, description, price, discount_price, category_id, stock, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                product_name, description, price, discount, category_id, stock, file_path
            )
        else:
            db.execute(
                """INSERT INTO products
                (name, description, price, category_id, stock, image_url)
                VALUES (?, ?, ?, ?, ?, ?)""",
                product_name, description, price, category_id, stock, file_path
            )
        product_id = db.execute(
            "SELECT id FROM products WHERE name = ?",
            product_name
        )
        # add variants to database
        for i in range(len(variant_sizes)):
            db.execute(
                "INSERT INTO product_variants (product_id, size, color, stock) VALUES (?, ?, ?, ?)",
                product_id[0]["id"], variant_sizes[i], variant_colors[i], variant_stocks[i]
            )

        print("Product added successfully!", "success")
        return redirect("/shop")  # Redirect to the shop page

@app.route("/add-category", methods=["POST"])
def addcategory():
    category_name = request.form.get("category_name")
    db.execute(
        "INSERT INTO categories (name) VALUES (?)",
        category_name
    )
    return redirect("/ownerdashboard")
