# coffee-shop-challenge

Project Overview

For this assignment, we'll be working with a Coffee shop-style domain. We have three models: Coffee, Customer, and Order. For our purposes, a Coffee has many Orders, a Customer has many Orders, and an Order belongs to a Customer and to a Coffee. Coffee - Customer is a many-to-many relationship. Note: You should draw your domain on paper or on a whiteboard before you start coding. Remember to identify a single source of truth for your data.

Project Setup & Folder Structure

Create a new repository

Name it (for example) coffee-shop-challenge.

Initialize with a README.md.

Clone locally

git clone git@github.com:<your-username>/coffee-shop-challenge.git cd coffee-shop-challenge
Initialize your Python environment

pipenv install pipenv shell
Define your folder & file layout

coffee-shop-challenge/ ├── Pipfile ├── debug.py ├── customer.py ├── coffee.py ├── order.py └── tests/ ├── customer_test.py ├── coffee_test.py └── order_test.py
Initial commit

git add . git commit -m "chore: scaffold project structure"

☕ Coffee-Shop Challenge: Requirements

1. Models & Initializers
   Customer
   **init**(self, name)

Store a name (must be a str, 1–15 characters).

Property name

Getter returns the customer’s name.

Setter enforces str type and 1–15 character length.

Coffee
**init**(self, name)

Store a name (must be a str, at least 3 characters).

Property name

Getter returns the coffee’s name.

Immutable once initialized.

Order
**init**(self, customer, coffee, price)

Accepts a Customer instance, a Coffee instance, and a price (float, 1.0–10.0).

Property price

Getter returns the order price.

Immutable once initialized; enforces type and range.

2. Object Relationships
   Order.customer → returns the Customer instance (type-checked)

Order.coffee → returns the Coffee instance (type-checked)

Customer.orders() → all Order instances for that customer

Customer.coffees() → unique list of Coffee instances they’ve ordered

Coffee.orders() → all Order instances for that coffee

Coffee.customers() → unique list of Customer instances who’ve ordered it

3. Aggregates & Associations
   Customer.create_order(coffee, price)
   Instantiate a new Order, link it to this customer and the given coffee.

Coffee.num_orders()
Total count of orders for this coffee (0 if none).

Coffee.average_price()
Mean of all order prices for this coffee (0 if none).

4. Bonus (Optional)
   Customer.most_aficionado(coffee) (classmethod)
   Return the Customer Who’s spent the most on the given coffee (or None If no orders)

Happy Coding
