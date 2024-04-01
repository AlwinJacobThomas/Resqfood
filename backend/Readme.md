# Resqfood Project Documentation
## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Authentication](#authentication)
6. [Models](#models)
7. [Views](#views)
8. [Serializers](#serializers)
9. [URLs](#urls)

## Overview
The Resqfood project is a Django-based RESTful API project aimed at facilitating food donation and distribution. It allows organizations and individuals to register, create food donation requests, and confirm donations. This documentation provides an overview of the project structure, installation instructions, API endpoints, authentication mechanism, models, views, serializers, and URLs.

## Installation
To set up the Resqfood project locally, follow these steps:

```bash
# Clone the repository from GitHub.
git clone https://github.com/AlwinJacobThomas/Resqfood.git
cd Resqdood/backend/

#Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

# Install the required dependencies using pip.
pip install -r requirements.txt

# Set up the database configuration in the project settings.
# You need to configure your database settings in settings.py.
# Example:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'your_database_name',
#         'USER': 'your_database_user',
#         'PASSWORD': 'your_database_password',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Apply database migrations to create the necessary tables.
python manage.py makemigrations
python manage.py migrate

# Run the Django development server.
python manage.py runserver
```

## Usage
Once the project is set up, you can start using it by accessing the provided API endpoints. Make sure to authenticate where required and follow the API documentation for each endpoint.

## API Endpoints
The Resqfood project provides the following API endpoints:

/api/register/: Register a new user (organization or individual).
/api/login/: Log in with username and password to obtain an authentication token.
/api/logout/: Log out the user and invalidate the authentication token.
/api/logoutall/: Log out the user from all sessions.
/api/change_password/: Change the user's password.
(Add more endpoints as necessary based on your project)

## Authentication
The project uses token-based authentication using the Knox library. Users can obtain a token by logging in and use it to authenticate subsequent requests to protected endpoints.

## Models
The Resqfood project defines the following models:

IndividualProfile
OrganizationProfile
Location
FoodRequest
DonationTicket
DonationConfirmationTicket
(Provide a brief description of each model and its fields)

## Views
The project includes views for user registration, login, logout, password change, and other functionalities. These views handle incoming requests and interact with the appropriate models and serializers.

## Serializers
Serializers are used to convert complex data types, such as Django model instances, into native Python data types suitable for rendering in JSON format. The project defines serializers for user registration, login, password change, and other data manipulation operations.

## URLs
URL patterns are defined in the project's URL configuration file. Each URL is mapped to a corresponding view or viewset, allowing incoming requests to be routed to the appropriate handler.

