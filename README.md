# OnlineShop

OnlineShop is a Django-based e-commerce application that allows customers to view and categorize products, manage their shopping carts, and place orders seamlessly. The project integrates asynchronous features to notify customers about their orders via email.

## Features

- **Product Display**: View all available products in the shop.
- **Product Categorization**: Products are grouped into respective categories for easier navigation. For example, a "Tea" category contains various tea flavors like green tea.
- **Shopping Cart**: 
  - Add items to the cart.
  - Remove items from the cart.
  - Adjust product quantities in the cart.
  - Cart management is implemented using Django sessions.
- **Global Cart Visibility**: A custom context processor ensures the cart is consistently visible across the project.
- **Order Placement**: Customers can place orders for items in their cart.
- **Email Notifications**: After an order is placed, customers receive email notifications about their orders asynchronously.
- **Asynchronous Processing**:
  - **Celery**: Handles background tasks for email notifications.
  - **RabbitMQ**: Used as the message broker for Celery tasks.

## Technologies Used

- **Framework**: Django
- **Asynchronous Task Management**: 
  - Celery
  - RabbitMQ
- **Backend**:
  - Python
  - Django sessions for cart management
- **Frontend**: 
  - Django templates
- **Database**: Configurable based on your Django project settings (e.g., PostgreSQL, SQLite, etc.)
- **Email**: Configured for sending order notifications.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/onlineshop.git
   cd onlineshop
