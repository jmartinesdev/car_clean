# Car Clean App - Client Management System

## Overview 

This project is a Django-based web application designed for managing clients and their cars. It provides functionalities to add and update client details, as well as keep a record of their cars.

## Features:

* Add Client: Allows you to input client details like name, surname, email, and phone number.
* Update Client: If a client with a specific phone number already exists, the system lets you update their details.
* Email Validation: The system has built-in email validation to ensure the correctness of the provided email address.
* Add Cars: For each client, multiple cars can be added. The details required include the car name, registration, and year.

## How to use:

### 1. Client Creation
To add a client, navigate to the clients.html page. Here, you'll be presented with a form. Fill out the client's name, surname, email, and phone number. You can also add details of the cars associated with the client.

### 2. Client Update
If a client with the entered phone number already exists in the system, you will be redirected to update the client's details.

### 3. Email Validation
The system validates the email entered using a regex pattern. If the email format is incorrect, the form will be rendered again, prompting you to enter the correct details.

### 4. Save Details
Once all details are entered correctly, the client's details and their associated cars are saved in the database.

# Dependencies:

* Django
* Python's regex library (re)

# Database Models:

- Clients: This model stores client details such as name, surname, email, and phone.
- Cars: This model keeps a record of cars associated with a client. It has fields for car name, registration, year, and a foreign key linking to the client.

# Future Improvements:
- Add delete functionality for clients and cars.
- Incorporate user authentication for better security.
- To get started with this project, ensure you have Django set up, and then migrate the database models. Once done, you can run the server and navigate to the clients.html page to begin adding clients.
