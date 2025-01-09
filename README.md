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
## Directory Structure

spshrishail-College_Admission/
|
├── README.md                    
|
├── db.sqlite3                  
|
├── manage.py                   
|
├── app/                        
|   |
|   ├── __init__.py            
|   ├── admin.py               
|   ├── apps.py                
|   ├── forms.py               
|   ├── models.py              
|   ├── tests.py               
|   ├── views.py               
|   ├── __pycache__/           
|   |
|   ├── migrations/            
|   |   ├── 0001_initial.py    
|   |   ├── ... (other migrations)
|   |   └── __pycache__/       
|   |
|   ├── static/                
|   |   └── img/
|   |       └── college        
|   |
|   └── templates/             
|       ├── add_student.html
|       ├── display_students.html
|       ├── index.html
|       ├── inquiry.html
|       ├── inquiry_student_details.html
|       ├── inquirydata.html
|       ├── student_details.html
|       ├── studentform.html
|       └── registration/
|           └── login.html
|
└── project/                    
    ├── __init__.py            
    ├── asgi.py                
    ├── settings.py            
    ├── urls.py                
    ├── wsgi.py                
    └── __pycache__/           

