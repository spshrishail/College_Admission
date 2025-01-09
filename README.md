# College Admission and Inquiry System

This project is a College Admission and Inquiry System built using Django. The system allows users to manage student admissions and inquiries efficiently. Additionally, it provides the functionality to download student data in CSV format.

## Features

- User authentication and authorization
- Manage student admissions
- Handle student inquiries
- Export student data to CSV file

## Requirements

- Python 3.x
- Django 3.x or later
- CSV

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/spshrishail/College_Admission.git   
   cd College_Admission
   python manage.py runserver
## Admin and User Credentials
Username: bgmit
Password: 12qw!@QW

## Directory Structure

This is the structure of the `spshrishail-College_Admission` project:
spshrishail-College_Admission/ ├── README.md # Project documentation ├── db.sqlite3 # SQLite database file ├── manage.py # Django's command-line utility ├── app/ # Application folder │ ├── init.py # App initialization │ ├── admin.py # Admin interface configuration │ ├── apps.py # App configuration │ ├── forms.py # Forms for user input │ ├── models.py # Database models │ ├── tests.py # Test cases │ ├── views.py # View functions │ ├── pycache/ # Compiled Python files (auto-generated) │ ├── migrations/ # Database migration files │ │ ├── 0001_initial.py # Initial migration │ │ ├── ... # Other migrations │ │ └── pycache/ # Compiled migration files │ ├── static/ # Static files (CSS, JS, images, etc.) │ │ └── img/ │ │ └── college # College-related images │ └── templates/ # HTML templates for the app │ ├── add_student.html │ ├── display_students.html │ ├── index.html │ ├── inquiry.html │ ├── inquiry_student_details.html │ ├── inquirydata.html │ ├── student_details.html │ ├── studentform.html │ └── registration/ │ └── login.html └── project/ # Django project folder ├── init.py # Project initialization ├── asgi.py # ASGI configuration ├── settings.py # Project settings ├── urls.py # URL routing ├── wsgi.py # WSGI configuration └── pycache/ # Compiled Python files (auto-generated)
