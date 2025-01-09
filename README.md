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

## Directory structure:
└── spshrishail-College_Admission/
    ├── README.md
    ├── db.sqlite3
    ├── manage.py
    ├── app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   ├── __pycache__/
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_student_delete_studentdata.py
    │   │   ├── 0003_alter_student_id.py
    │   │   ├── 0004_student_dynamic_fields.py
    │   │   ├── 0005_remove_student_dynamic_fields_alter_student_college_and_more.py
    │   │   ├── 0006_alter_student_branch.py
    │   │   ├── 0007_inquiry.py
    │   │   ├── 0008_inquiry_date.py
    │   │   ├── 0009_student_date.py
    │   │   ├── 0010_alter_inquiry_date_alter_student_date.py
    │   │   ├── 0011_alter_inquiry_date_alter_student_date.py
    │   │   ├── 0012_alter_student_paid_fee.py
    │   │   ├── 0013_contact.py
    │   │   ├── 0014_contact_date.py
    │   │   ├── 0015_remove_contact_date.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   ├── static/
    │   │   └── img/
    │   │       └── college
    │   └── templates/
    │       ├── add_student.html
    │       ├── display_students.html
    │       ├── index.html
    │       ├── inquiry.html
    │       ├── inquiry_student_details.html
    │       ├── inquirydata.html
    │       ├── student_details.html
    │       ├── studentform.html
    │       └── registration/
    │           └── login.html
    └── project/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── __pycache__/
