Overview
This Django project implements user registration, login, logout, and a dynamic dashboard. It supports multiple database backends, allowing easy local development and production deployment.

Local Database Configuration

- Install Oracle Database or connect to an existing instance.
- Install the Python driver:
pip install oracledb
- Update settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '140.238.254.50:1521/orclpdb',
        'USER': 'TESTUSER',
        'PASSWORD': 'TESTUSER',
    }
}

- Run migrations again to create tables in Oracle.
 
Steps to Run Locally
- Install dependencies:
pip install -r requirements.txt
- Configure database in settings.py (SQLite for local, Oracle if required).
- Apply migrations:
python manage.py migrate

- Start the server:
python manage.py runserver
- Access the app at http://127.0.0.1:8000/.
 

