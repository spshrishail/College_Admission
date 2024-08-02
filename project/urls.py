"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("inquiry",inquiry,name='inquiry'),
    path('',home,name='index'),
    path('studentform/',data,name='studentform'),
    path('addstudent',addstudent,name='addstudent'),
    path('student_details',student_details,name='student_details'),
    path('display_students',display_students,name='display_students'),
    path('update_student/<int:student_id>/', update_student, name='update_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('inquirydata',inquirydata,name='inquirydata'),
    path('BookCSV',BookCSV,name='BookCSV'),
    path('InquiryCSV',InquiryCSV,name='InquiryCSV'),
    path('inquiry_student_details',inquiry_student_details,name='inquiry_student_details'),
    path('download_all_searched_students/', download_all_searched_students, name='download_all_searched_students'),
]
