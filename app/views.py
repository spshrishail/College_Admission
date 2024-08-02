from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from app.forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'index.html')

def data(request):
    return render(request,'studentform.html')

def inquiry(request):
    return render(request,'inquiry.html')

def addstudent(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addstudent')  
    else:
        form = AddStudentForm()
    return render(request, 'add_student.html', {'form': form})

def student_details(request):
    students = Student.objects.all() 
    return render(request, 'student_details.html', {'students': students})

def display_students(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        students = Student.objects.filter(branch=branch)
    else:
        students = Student.objects.none()  
    branches = Student.objects.values_list('branch', flat=True).distinct() 
    context = {
        'students': students,
        'branches': branches,
    }
    return render(request, 'display_students.html', context)

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        data=Contact(name=name,email=email,phone=phone,message=message)
        data.save()
        return render(request,'index.html',{'success':'Message send successfully'})
    return render(request,'index.html')

def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            # Return updated student data as JSON response
            data = {
                'name': student.name,
                'college': student.college,
                'place': student.place,
                'branch': student.branch,
                'puc_result': student.puc_result,
                'cet_rank': student.cet_rank,
                'category': student.category,
                'contact': student.contact,
                'total_fee': student.total_fee,
                'paid_fee': student.paid_fee,
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Form is not valid.'}, status=400)
    else:
        form = AddStudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
    
def inquirydata(request):
    if request.method == 'POST':
        form = AddInquiry(request.POST)
        if form.id==exit():
            return HttpResponse('data already exist')
        elif form.is_valid():
            form.save()
            return redirect('inquirydata')  
    else:
        form = AddInquiry()
    return render(request, 'inquirydata.html', {'form': form})

import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter


def BookCSV(request):
    courses = Student.objects.all()
    resp = HttpResponse(content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename=booked_student_data.csv'
    writer = csv.writer(resp)
    writer.writerow(['id', 'name', 'college','place','branch','puc_result','cet_rank','category','contact','totle_fee','paid_fee'])
    
    for c in courses:
        writer.writerow([c.id, c.name, c.college,c.place,c.branch,c.puc_result,c.cet_rank,c.category,c.contact,c.total_fee,c.paid_fee])
    
    return resp


def InquiryCSV(request):
    courses = Inquiry.objects.all()
    resp = HttpResponse(content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename=booked_student_data.csv'
    writer = csv.writer(resp)
    writer.writerow(['id', 'name', 'college','place','branch','puc_result','cet_rank','category','contact'])
    
    for c in courses:
        writer.writerow([c.id, c.name, c.college,c.place,c.branch,c.puc_result,c.cet_rank,c.category,c.contact])
    
    return resp

def inquiry_student_details(request):
    students=Inquiry.objects.all()
    return render(request,'inquiry_student_details.html',{'students':students })



def download_all_searched_students(request):
    branch = request.POST.get('branch')
    students = Student.objects.filter(branch=branch)
    resp = HttpResponse(content_type="text/csv")
    resp['Content-Disposition'] = 'attachment; filename=all_searched_student_data.csv'
    writer = csv.writer(resp)
    writer.writerow(['id', 'name', 'college', 'place', 'branch', 'puc_result', 'cet_rank', 'category', 'contact', 'total_fee', 'paid_fee'])
    for student in students:
        writer.writerow([student.id, student.name, student.college, student.place, student.branch, student.puc_result, student.cet_rank, student.category, student.contact, student.total_fee, student.paid_fee])

    return resp