from django import forms
from .models import Student,Inquiry

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AddInquiry(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'