# Django REST API with JWT Authentication

This project is a Django-based REST API for managing products, customers, carts, and purchases. It includes JWT authentication for securing the endpoints.

## Features

- **Product Management**: CRUD operations for products.
- **Customer Management**: CRUD operations for customers.
- **Cart Management**: Create and manage carts, including checkout functionality.
- **Purchase Management**: Track purchases after cart checkout.
- **JWT Authentication**: Secure the API with token-based authentication.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository



##end points##

Products
List Products: GET /api/products/
Create Product: POST /api/products/
Retrieve Product: GET /api/products/{id}/
Update Product: PUT /api/products/{id}/
Delete Product: DELETE /api/products/{id}/
Customers
List Customers: GET /api/customers/
Create Customer: POST /api/customers/
Retrieve Customer: GET /api/customers/{id}/
Update Customer: PUT /api/customers/{id}/
Delete Customer: DELETE /api/customers/{id}/
Carts
List Carts: GET /api/carts/
Create Cart: POST /api/carts/
Retrieve Cart: GET /api/carts/{id}/
Update Cart: PUT /api/carts/{id}/
Delete Cart: DELETE /api/carts/{id}/
Checkout Cart: POST /api/carts/{id}/checkout/
Purchases
List Purchases: GET /api/purchases/
Create Purchase: POST /api/purchases/
Retrieve Purchase: GET /api/purchases/{id}/
Update Purchase: PUT /api/purchases/{id}/
Delete Purchase: DELETE /api/purchases/{id}/