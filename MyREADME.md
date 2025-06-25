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
  (I'm going to add these later when i have access to my datbase)

Table Schemas :
 (I'm going to add these later when i have access to my datbase)

 
