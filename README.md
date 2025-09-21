# Flask-Based Online Shop
#### (Video Demo)[https://youtu.be/agswBqxFVQo]
#### Description:

This project is a feature-rich, web-based **Online Shopping Platform** developed using **Python (Flask)**, **SQLite**, and standard web technologies (HTML, CSS, JS). It simulates a real-world e-commerce experience, supporting multiple user roles (customers and owners), product variant management, secure login, cart and order handling, and more. It draws directly upon many core topics taught in CS50, including HTTP, sessions, SQL, and Flask.

---

## Features

- **User Authentication**
  - Registration with username, email, password, and full name
  - Secure login/logout using hashed passwords and session management

- **Product Browsing and Management**
  - Public product listings and individual product detail views
  - Products can have **variants** by size and color
  - Owner-exclusive dashboard to add products, categories, and manage inventory

- **Shopping Cart**
  - Logged-in users can add product variants to their cart
  - Cart shows detailed item listings, quantity, and live subtotal and total price calculations
  - Remove items from cart functionality included

- **Checkout and Order Placement**
  - Form-based checkout with full shipping details and payment method
  - All items in the cart are converted into a finalized order, stock is decremented accordingly
  - Confirmation page with order summary

- **Order History**
  - Users can view their previous orders

- **Additional Pages**
  - Wishlist (stub page for future implementation)
  - Contact page
  - Owner and user dashboards

---

## File Overview

### `app.py`
Main application controller that defines the routing logic, session handling, and core operations. Key route functionalities include:

- `/signup`, `/login`, `/logout` — Handles user authentication
- `/shop` — Displays all available products
- `/product` — Shows product details or handles deletion (by owner)
- `/add_to_cart` — Adds a variant to the cart
- `/cart` — Displays the current user's cart
- `/remove` — Deletes items from the cart
- `/checkout` — Displays checkout page
- `/place-order` — Finalizes and stores the user's order
- `/orders` — View past orders
- `/dashboard`, `/ownerdashboard` — Show user and admin-specific dashboards
- `/addproduct` — Allows owners to add new products with variants and image uploads
- `/add-category` — Adds new product categories

The file is modular and structured with appropriate error-handling, session checks (`@login_required`), and secure database queries.

### `helpers.py`
Contains support functions for:
- `apology(message, code)` — For rendering error messages
- `login_required(f)` — Flask decorator to restrict routes to logged-in users
- `get_cart_details(user_id)` — Returns all items in a user's cart, subtotal calculations, total price, and item count.

---

## Design Decisions

- **Role-Based Access:** The application implements a basic RBAC system. Owners can access privileged routes like product creation and deletion.
- **Product Variants:** Instead of separate product listings for different sizes/colors, the app uses a normalized schema with a `product_variants` table.
- **Image Uploading:** Images are stored in the `static/uploads/` directory. Uploaded filenames are used directly for simplicity.
- **Session Management:** Flask’s secure session cookie is used for user state tracking.
- **Security:** Passwords are stored as hashes using Werkzeug; SQL queries use parameterized inputs to prevent injection.

---

## Limitations & Future Improvements

- **Wishlist Functionality:** Currently a placeholder; future iterations could allow adding/removing favorite items.
- **Payment Integration:** The checkout simulates payment via a form. Real payment gateway support could be added using Stripe or PayPal.
- **Image Handling:** Currently filenames are stored as-is; for production, use UUID filenames and validate file types.
- **Admin Dashboard:** Could be expanded to include analytics and order tracking.

---

## Skills Demonstrated

- Full-stack web development using Flask and SQL
- Authentication and access control
- File uploads and image storage
- Database schema design and relational querying
- Using decorators and utility functions for modularity
- Debugging and testing user input handling

---

## CS50 Concepts Applied

- HTTP, sessions, GET/POST
- SQL schema design, SELECT/INSERT/UPDATE/DELETE queries
- Error handling and user feedback via custom apology pages
- Templates and Jinja2 for HTML rendering
- Flask decorators and helper function modularization

---

## Acknowledgements

- Portions of the image upload logic were assisted by AI-based tools like ChatGPT, and appropriate citations are included in `app.py`.
- Design inspired by modern e-commerce flows.

---

