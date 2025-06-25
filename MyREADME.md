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
