# Cross-Options-Order-Management-System

Django was used in the system .The Cross Options Order Management System (OMS) is a simple yet powerful tool designed to streamline the process of executing and managing trades. This system allows traders at Cross Options to save all their trades in a centralized location, making it easy to access and manage trade data efficiently. This README provides an overview of the OMS, its features, and instructions on how to use the system.

Basic Features of The App
1. Homepage - Starting point where users land upon visiting the app, offering an introduction and access to its core features and content.
        - Home page Button
        - About Us Button
        - Sign In Button
        - Sign Up Button
        - Admin Sign In Button

2. Sign Up – Users can register and create a new profile
        - Auto ID Generated ID to  avoid double primary keys
        - Username
        - Age
        - Password - With password hashing

3. User Dashboard - Once Signed In and authenticated, users can create and update additional information such trade.
        - Need authentication to access this page
        - Find all historical trades:
                    - Presented with datatable
                    -  With option to specify certain date range
        - A user is not allowed to alter a trade was it has been put in the system
        - Create new trade: 
                    - Trade is a completed order
                    - AUTO ID for generated unique TRADE ID
                    - Date of execution
                    - Amount of shares bought
                    - Symbol of Shares
                    - Field indicating whether shares were bought or sold,
                    - User ID of user that executed the trade
                    - Total payment in $ for all shares in the trade
        - Log out: Terminates user access for security and privacy.

        

4. Admin Log In – Once Signed In and authenticated, Admin can login using username and password
        - "admin123" Default username and password for demo test
        - Admin Sign In requires User ID, username, age, and password to be authenticated and will be directed to admin dashboard
        

5. Admin Dashboard – Admin can Read, Update and Delete user's trade
        - Need authentication to be valid to access this page
        - Find all users
        - Find all trades for a certain user
        - Change following fields of logged trade: number of shares or price paid
        - Log out: Terminates user access for security and privacy.

DATABASE USED : SQLITE3 - Default database of django

BASIC ENITIES - CHECKED
OPERATIONS - CHECKED
STORAGE & LOGGING - CHECKED
TECHNICAL EXPECTATIONS - CHECKED

Quick Start
To get this project up and running locally on your computer follow the following steps.

Set up a python virtual environment
Run the following commands

$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver






