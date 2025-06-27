#### title :               E-commerce Website
- One sentence summary : An Online Shop for selling & buying Clothes
- Who is the target user? Everone , mainly people who are busy and therefor are more comfortable shopping online. 
mainly owner's who have an Instagram page for selling clothes but would like to expand their customer audience.
- Main goal

What problem does it solve for these users? people who use instagram for online shopping know that it's not suitable for that task the user experience isn't 
optimized for that, Instagram Shops also lack reliability becuase there isn't much of a certificate or anything like that which would provide illegibility.
INSTAGRAM is also unreliable as a website because the servers are foreign which means it might be 
hard to access sometimes or you might need a VPN for it but if you have a website as an online shop people can access your webiste even with a poor inetner Connection,.
- PART 2 — Tech Stack
5️⃣ What technologies did you use?

Backend: Flask, SQLite, CS50 Library 
libraries and frameworks:
-OS
-SQL
- Flask, flash, redirect, render_template, request, session, url_for
- Session from flask_session 
- check_password_hash, generate_password_hash from werkzeug.security
- My Own functions: 
 apology, login_required, get_cart_details from helpers.py file 


Frontend: HTML, CSS, Bootstrap, Jinja2 templates, 

# What features did you implement?
        - User Registration & Login
        - Role-based access (Owner / Customer)
        - Product Management (Owners can add,  delete products)
        - Product Variants (Size, Color, Stock)
        - Product Listing page (Shop)
        - Product Details page
        - Shopping Cart
        - Checkout and Place Order
        - Order History
        - File/Image Upload for products (helped by AI)
        - Owner Dashboard
        - User Dashboard
        - Contact Page

❓ **What parts of the project were hardest for you to implement?**
At first getting the hang of passing data between front end and backend was challenging, after getting used to the syntax it wasn't hard.
**Challenges :**
  - implementing file uplaod (how to upload where to store the image how to access it)
  - Deleting Data from the database (i faced foreign key constraint multiple times and i couldn't figure out why later i realised i needed to first delete the variants of a product before deleting a product)

❓ Which parts were most fun or interesting for you?
the parts that are most challenging are usually the most fun after you finally figure them out.
I generally enjoy the backend.

❓ ** If you had more time, what would you add or improve?**
- Payment Gateway
- filter by category for product listing page
- Search functionality for products
- Sales Data for Owner Dashboard
- wishlist

**PART 5 — Installation Instructions**
Anyone can run it by installing the requirments and running the comand "flask run"

**PART 6 — Database**
 List Of All My Tables:
  -cart_items
  -order_items       
  -product_variants  
  -users           
  -categories        
  -orders            
  -products  

Table Schemas :
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    discount_price REAL, -- Optional discount price
    category_id INTEGER,
    stock INTEGER DEFAULT 0,
    image_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
CREATE TABLE product_variants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    size TEXT,
    color TEXT,
    stock INTEGER DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
CREATE TABLE cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_variant_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (product_variant_id) REFERENCES product_variants (id)
);
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_variant_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id),
    FOREIGN KEY (product_variant_id) REFERENCES product_variants (id)
);
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT 1,
    role TEXT DEFAULT 'user'
);
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    total_price REAL NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
 
ROUND 2 — DESIGN & ARCHITECTURE DECISIONS
1. Project Motivation
Why did you pick Flask instead of Django or something else?

Why SQLite instead of PostgreSQL or MySQL?

Did you consider any alternatives to Bootstrap?Backend: Flask 
Database: SQLite
Frontend: Bootstrap
these were my tech stack choices because I learned them in CS50 I wanted to make sure I had a good grasp on what I had already learned to strengthen my foundation before moving on to learning some new technologies.

2.  Authentication & Roles
How does your system differentiate between an Owner and a Customer? (Is there a "role" column in the Users table? How is it assigned?)

Can a user become an owner, or do you manually assign it directly in the database?How does your system differentiate between an Owner and a Customer? (Is there a "role" column in the Users table? How is it assigned?)

Can a user become an owner, or do you manually assign it directly in the database?
this part i think has a great potential for improvement because I manually assign the roles
I have a role column in the database and the idea is that the website either has one or very few owners so when i develop the website for them i will create an owner account for them and assign the owner role from directly manipulating the database and inserting the the user's table.
from then on anybody who signs up to the website using website's own interface will be automatically assigned the 'user' role.
3️⃣ Product Model Design
Why did you choose to separate product variants into a separate product_variants table?

Did you consider simplifying it to just one products table (without variants)? Why or why not?
I don't think it would be a good idea to put all of them in one table this seemed like the logical way to do it
honestly i can't remember now
but i feel like there is some benefits to what i did.
4. TODO : answer the rest 
 File Uploads
Where exactly are the images stored? (local folder, database, cloud storage, etc.)

Are the image URLs stored in the database or just filenames?

5️⃣ Error Handling
How do you handle cases where a user tries to buy an out-of-stock product?

What happens if someone enters invalid data in forms? (Do you flash messages? Do you validate input?)

6️⃣ Session Handling
Are you using Flask’s default session? How long does the session last?

Is there any kind of CSRF protection or logout timer?

7️⃣ Helpers
Tell me a bit more about helpers.py — what functions did you create there?

What does get_cart_details do exactly? Walk me through how it works.

8️⃣ Cart Logic
Where is the cart stored: database or session?

Can multiple users have their own carts at the same time? (multi-user handling)

9️⃣ Testing
How did you test your code? (manually? automated tests? Postman? Browser only?)

Any particular bugs you struggled with during testing?

🔟 Deployment (if any)
Was this deployed online anywhere or only tested locally?
EXTRA ROUND (Optional, but very useful)
1️⃣ Lessons Learned
What are 3-5 important lessons you learned while building this project?

2️⃣ If you rebuilt this project from scratch today, what would you do differently?

Let’s drill into each area so we can enrich your README with concrete detail. Please answer these:

### 1. User Flows & Features

1. **Registration & Login:**

   * How does a new user sign up? What fields are required, and what validations run?
   username , password, email, full name, password
   these fields are flagged as required in the HTML so user will be informed that they have to provide these info to be able to sign up
   and when the from is submitted via POST using flask and if statements i check to make sure theyr provided these fields
   then the password is checked against password confirmation and they should match otherwise the user will recieve an error
   In general in this project i use flash to inform the user when they are trying to do something that isn't allowed or when there is an error
   if the username they chose is already in the datbase they also can't sign up
   after these requirments are met , the form's inputs is INSERTed into the datbase using the datbasename.execute() function and the user is logged in.

   * What’s the post‑login redirect or landing page for customers vs. owners?
   they both get redirected to homepage

    sign up and login in genreal are managed using Flask's session library / framework
2. **Shopping Cart & Checkout:**

   * Step by step, what happens when a customer adds an item to their cart?

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
    explain it for me using the code provided
    my own explanation: 1. the product's info is extracted from the html form using request.forms.get
    and 2. then it's added to the cart_items table

   * Describe the checkout process: what forms do they fill, what payment methods are supported (or simulated), and what confirmation steps occur?

   the checkout process was designed from the experience i have had while making online purchases
   and also this website is designed so that both the owner and customers can make good use of it so after the customer makes the purchase the owner needs to have some basic infor about the customner for example the owner needs to know their email address so that they can send emails whenever necessary for example when they ship the order they would inform the customer

    and the owner also needs to know the customer's postal address so that they can ship the order
    for this part enhancments and improvements include : maybe all the data of all orders can be inserted into a spreadsheet so that it's easier for owner's to manage and whenever an order is placed owner is informed so that they don't have to check the website all the time

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


 

3. **Dashboards:**

   * For Owners: what data do you display (e.g., sales totals, new orders)? Any charts or tables?
     owner's dashboard has only 3 features, 
     1 . enables the owner to view all the orders that has even been placed on the website (from here they can update the status of orders when they ship them and they can access info about orders and their customers so thaey can gather the info they need for shipping products purchased)
     2. add or remove products from the website

     future improvments: add sales data , maybe add a feature that displays popular products or lets owner know which products are out of stock and also on peopl's wichlists so that they know what to make available on the shop
   * For Customers: what order history details are shown, and can they reorder or track status?
   the cutomer's dashboard doesn't have many features it just has 3 links 1 takes the user o a page that displays all of the orders that custoer has placed on the website 
   2. takes the customer to /shop
   3. takes the cutomer to /contact page

   customers can click view orders and see all the past orders they've placed on the store which also display the status when it's shipped it will be displayed here 


### 2. Design & Architecture

4. **Project Structure:**

   * How have you organized your Flask app directories (e.g., `static/`, `templates/`, `helpers/`, `models/`)?
   > project
        app.y
        static/
        templates/

   * Any design patterns (blueprints, service layer, etc.)?
   nope


5. **Database Details:**

   * Which columns/indexes are most critical for performance?
   i have no idea i think all of it is necessary
   * Any decisions around foreign‑key constraints or normalization beyond variants?
   no 
   in this project i mainly went with all the things i had learned in CS50 lectures and psets and tried to build a project using all the knwoledge from this course alone when i built this project i didn't have any knwoledge of web design or computer science outside of what i had learned in cs i made decision of not learning any other languages or frameword or tools for the time being in order to strengthening my fooundations before moving on

### 3. Deployment & DevOps

6. **Environment & Hosting:**
 i did not host it or make it online
   * Where would you deploy this (Heroku, AWS, DigitalOcean)?
   * How do you manage environment variables (e.g., secret keys, database URLs)?

7. **CI/CD & Containerization:**
i plan to learn these when taking CS50 w
   * Do you plan to use Docker? Automated pipelines (GitHub Actions, Travis CI)?

### 4. Testing & QA

8. **Test Coverage:**
no tests are automated i did all the testing manually by simulating the owner's experience and the customer's
how the wner might wanna add or manage products and access orders and how the customer will shop on the website
   * Which parts are manually tested vs. automated?
   * Any example unit or integration tests you wrote (e.g., for `get_cart_details`)?

9. **Edge Cases:**
i tried to take in account what edge case might occur and handle it using flask flashing error messages and redirecting
   * How do you handle invalid form submissions, network errors during checkout, or duplicate orders?

### 5. Security & Validation

10. **Authentication & CSRF:**
i used flask's framework to hash passwords

    * CSRF protection approach? Rate‑limiting login attempts?
    * Password policy (min length, complexity)?

11. **Data Validation:**

    * How do you validate user input (e.g., order address fields, product creation)?

### 6. Lessons & Roadmap

12. **Lessons Learned:**

    * List 3–5 specific “aha” moments or pitfalls you overcame.
    1. when deleting products i faced an error that was caused by not deleting the product vaiants before atempting to delete that product
    which caused a lot of confusion but then i figured it out
    2. to display images for each product i needed to owner to upload a photo and i needed a way of storing the photo on the database so that i could access it later and display it 
    i realised that convention with flask is to have an upload/ directory inside the static/ folder inside the main project directory and to store the images there , when the owner uploads the image i store it inside this folder and store the image url in the image column of the product table of the  database later whenever i need it i use an image tage and pass in the image url into the src attribute like this 

    {{% for product in products %}}
        <img src="{{product.image_url }}">
    {{% endfor %}}

    when i wanted to implement this feature i came up with the psuedocode and logic myself and it made sense but i didn't know how to translate it to python to do this i used the help of chatgpt 

    i don't remember much about coding this project and the chalanges i faced because it was a long time ago

13. **Future Roadmap:**

    * Beyond Django/PostgreSQL, what v2 features will you prioritize first (e.g., search, payment integration, analytics)?

Answer these and we’ll integrate your details into a 740+ word README.
i think this project is a solid way of practicing what i learned in cs50 but if i wanted to use it in the real world i would definetly consider building a version 2 of it using django and postgres to firtly make the deployment easier i  have realised many hosts are postgres and django friendly 
django has many capabilities

i think implementing search and filter capabilities is necessary 

i didn't implement a payment agteway because that required signing up to stripe/ paypal which i can't without a credit card

but i will definetly need to do this for a future project i plan on learning these

a version 2 of this website will also have sales data available on owner's dashboard
i also think managing products could be improved , i think owner should be able to edit products which i think it's easier to implement using django models and forms

and the owner should be able to easily increase the stock quantity whenever they want 
without having to remove and ass producrt from scratch

they should be informed whoch prodcuts are out of stock and users have tried to add to add to their cart (sorted by the amount of times people have tried to purchase them) so that they know which prodcuts would sell best if they made them avilable

