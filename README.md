# Twitter
This repository contains a Django application through which I've learned the language and practiced my skills. It is a very basic example of the Twitter API, including users, permissions, posts, and comments.

## Prerequisites

Ensure you have the following installed before starting:

- Python 3.8 or higher
- Django 5.1
- pip (Python package manager)

## Installation

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


3. Apply the database migrations:

   ```bash
   python manage.py migrate

4. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser

5. Run the development server:

   ```bash
   python manage.py runserver

## Access the application

Using http://127.0.0.1:8000/ or http://localhost:8000/

## Features

- User registration and authentication using JWT
- User, categories, posts and comments creation and editing
- Permission management for users and endpoints
- Enpoints and documentation made with Swagger

## Usage

Once the development server is running, you can access:

- Admin panel at `http://127.0.0.1:8000/admin/` to manage users, categories, posts and comments
- Endpoints documentation at http://localhost:8000/docs/ or http://localhost:8000/redoc/

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you would like to change.
