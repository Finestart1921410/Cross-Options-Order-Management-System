# Cross-Options-Order-Management-System

Django was used in the system .The Cross Options Order Management System (OMS) is a simple yet powerful tool designed to streamline the process of executing and managing trades. This system allows traders at Cross Options to save all their trades in a centralized location, making it easy to access and manage trade data efficiently. This README provides an overview of the OMS, its features, and instructions on how to use the system.

Basic Features of The App

1. Homepage - Starting point where users land upon visiting the app, offering an introduction and access to its core features and content.
        - Home page Button
        - About Us Button
        - Sign In Button
        - Sign Up Button
        - Admin Sign In Button
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/cd6ae08a-c0ae-4020-9c2c-0ac8e517643d)


2. Sign In - Users can Sign In and create a new trade
        - Username
        - Password - With password hashing
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/d6185e80-2bd3-4b5a-a0f5-4bf221cee54f)


3. Sign Up – Users can register and create a new profile
        - Auto ID Generated ID to  avoid double primary keys
        - Username
        - Age
        - Password - With password hashing
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/304a5142-e0db-404a-a70e-6caa1e7d29a2)

        
4. User Dashboard - Once Signed In and authenticated, users can create and update additional information such trade.
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
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/eb3f3573-964e-4f05-a9c8-311835a36bcc)

![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/ecf39ff8-8aa8-4cd4-8024-4b6a4da68cbf)


        
5. Admin Log In – Once Signed In and authenticated, Admin can login using username and password
        - "admin123" Default username and password for demo test
        - Admin Sign In requires User ID, username, age, and password to be authenticated and will be directed to admin dashboard
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/55b7633b-8001-4dc0-8b85-adf5cd682026)

        
6. Admin Dashboard – Admin can Read, Update and Delete user's trade
        - Need authentication to be valid to access this page
        - Find all users
        - Find all trades for a certain user
        - Change following fields of logged trade: number of shares or price paid
        - Log out: Terminates user access for security and privacy.
   ![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/35fe1559-a2dd-47c2-90d3-c711b7ff5c7f)


DATABASE USED : SQLITE3 - Default database of django
![image](https://github.com/Finestart1921410/Cross-Options-Order-Management-System/assets/136356100/1664ae9d-0077-40cb-9354-f3723f21930f)


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






