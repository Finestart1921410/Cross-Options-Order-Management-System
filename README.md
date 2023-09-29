# Cross Options Order Management System (OMS)

The Cross Options Order Management System (OMS) is a powerful yet user-friendly tool designed to streamline the process of executing and managing trades. This system enables traders at Cross Options to store all their trades in one centralized location, simplifying access and efficient trade data management. This README provides an overview of the OMS, its features, and instructions on how to use the system.

## Basic Features

1. **Homepage**: The starting point where users land upon visiting the app, offering an introduction and access to its core features and content.
   - **Home Page Button**
   - **About Us Button**
   - **Sign In Button**
   - **Sign Up Button**
   - **Admin Sign In Button**
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/cd6ae08a-c0ae-4020-9c2c-0ac8e517643d)


2. **Sign In**: Users can sign in and create new trades.
   - **Username**
   - **Password** (with password hashing)
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/d6185e80-2bd3-4b5a-a0f5-4bf221cee54f)


3. **Sign Up**: Users can register and create a new profile.
   - Automatically generated ID to avoid duplicate primary keys
   - **Username**
   - **Age**
   - **Password** (with password hashing)
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/304a5142-e0db-404a-a70e-6caa1e7d29a2)

        
4. **User Dashboard**: After signing in and authenticating, users can create and update additional trade information.
   - Authentication required for access
   - View all historical trades:
     - Presented with a data table
     - Option to specify a certain date range
   - Users cannot alter a trade once it has been recorded in the system
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/eb3f3573-964e-4f05-a9c8-311835a36bcc)
   - Create a new trade:
     - Trade is a completed order
     - Automatically generated unique TRADE ID
     - Date of execution
     - Number of shares bought
     - Symbol of shares
     - Indication of whether shares were bought or sold
     - User ID of the user who executed the trade
     - Total payment in $ for all shares in the trade
   - Log out: Terminates user access for security and privacy.

![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/ecf39ff8-8aa8-4cd4-8024-4b6a4da68cbf)


5. **Admin Log In**: After signing in and authenticating, the admin can log in using a username and password.
   - Default username and password for demo testing: "admin123"
   - Admin Sign In requires User ID, username, age, and password for authentication and directs to the admin dashboard.

![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/55b7633b-8001-4dc0-8b85-adf5cd682026)

6. **Admin Dashboard**: The admin can read, update, and delete user's trades.
   - Authentication required for access
   - View all users
   - View all trades for a specific user
   - Modify the following fields of a logged trade: number of shares or price paid
   - Log out: Terminates admin access for security and privacy.
   ![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/35fe1559-a2dd-47c2-90d3-c711b7ff5c7f)


**Database Used**: SQLite3 - Default database of Django
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/1664ae9d-0077-40cb-9354-f3723f21930f)


 - **BASIC ENTITIES** - CHECKED ✔
 - **OPERATIONS** - CHECKED ✔
 - **STORAGE & LOGGING** - CHECKED ✔
 - **TECHNICAL EXPECTATIONS** - CHECKED ✔

## Quick Start

To set up this project locally on your computer, follow these steps:

1. Set up a Python virtual environment.
2. Run the following commands:

 - $ pip install -r requirements.txt
 - $ python manage.py migrate
 - $ python manage.py createsuperuser
 - $ python manage.py runserver

![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/2ab2cb00-d97c-4915-9445-5cfabc36b1f8)



