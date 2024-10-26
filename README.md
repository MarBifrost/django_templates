
# Melomani.ge

# E-commerce Music Store

Welcome to the E-commerce Music Store! This platform allows users to browse and purchase a wide range of music-related products. Users can explore various categories, add items to their cart, and proceed to checkout.

## Features

- **Product Browsing**: Users can view products categorized by genre, including Classical, Jazz, Rock, and more.
- **Search Functionality**: Filter products by price range and categories to easily find desired items.
- **Shopping Cart**: Add items to the cart, view the total price, and proceed to checkout.
- **User Accounts**: Users can create accounts, log in, and manage their orders.

## Technologies Used

- **Django**: The web framework used for building the application.
- **SQLite**: The database used for storing product and user information
- **HTML/CSS**: For creating a responsive and user-friendly interface.
- **Bootstrap**: For styling and layout.
- **MPTT**: For handling hierarchical categories.


## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:

   ```bash
    git clone https://github.com/yourusername/ecommerce-music-store.git
    cd ecommerce-music-store
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    ```
2. **Usage**
Navigate through the product categories.
Use the search feature to filter products by price.
Add products to your cart and proceed to checkout.
Manage your account and orders through the user dashboard.

3. **Database Setup**
Ensure you're using a database engine compatible with Django, such as PostgreSQL, MySQL, or SQLite. In this case you can download ready database, just to test the Functionality

4. **Models**
Models
You have the following primary models:

Category: Represents different categories of music products, utilizing the MPTT (Modified Preorder Tree Traversal) structure for hierarchical categorization.
Product: Represents individual music products, linked to categories through a Many-to-Many relationship.
Cart: Represents the user's shopping cart.
CartItem: Represents items within the user's cart.

5. **View Functionality**

- Cart View: Displays items in the user's shopping cart, including total price and shipping fees.
- Category View: Displays products filtered by selected categories.
- Product Filtering View: Handles filtering of products based on price range.

6. **View Functionality Details**
- Cart View:

Retrieves the current user's cart and the associated cart items.
Calculates the total price of items and includes a fixed shipping fee.
Prepares context data to render the cart.html template.

- Category View:

Fetches the category based on the slug passed in the URL.
Filters products belonging to that category and passes them to the template for rendering.

- Price Filtering View:

Processes a GET request containing a price range from the user.
Filters products based on the maximum price specified and prepares the filtered list for rendering.
