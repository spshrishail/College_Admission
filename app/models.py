from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    branch = models.CharField(
        max_length=50,
        choices=[
            ('CSE', 'CSE'),
            ('ECE', 'ECE'),
            ('AIML', 'AIML'),
            ('Civil', 'Civil'),
            ('Mech', 'Mech'),
            ('Mech/Civil', 'Mech/Civil'),
            ('Mech/AIML', 'Mech/AIML'),
            ('Mech/ECE', 'Mech/ECE'),
            ('Mech/CSE', 'Mech/CSE'),
            ('Civil/AIML', 'Civil/AIML'),
            ('Civil/ECE', 'Civil/ECE'),
            ('Civil/CSE', 'Civil/CSE'),
            ('AIML/ECE', 'AIML/ECE'),
            ('AIML/CSE', 'AIML/CSE'),
            ('ECE/CSE', 'ECE/CSE'),
        ]
    )
    puc_result = models.IntegerField()
    cet_rank = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=4)
    contact = models.IntegerField()
    total_fee = models.IntegerField()
    paid_fee = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically set to current date/time on creation

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    branch = models.CharField(
        max_length=50,
        choices=[
            ('CSE', 'CSE'),
            ('ECE', 'ECE'),
            ('AIML', 'AIML'),
            ('Civil', 'Civil'),
            ('Mech', 'Mech'),
            ('Mech/Civil', 'Mech/Civil'),
            ('Mech/AIML', 'Mech/AIML'),
            ('Mech/ECE', 'Mech/ECE'),
            ('Mech/CSE', 'Mech/CSE'),
            ('Civil/AIML', 'Civil/AIML'),
            ('Civil/ECE', 'Civil/ECE'),
            ('Civil/CSE', 'Civil/CSE'),
            ('AIML/ECE', 'AIML/ECE'),
            ('AIML/CSE', 'AIML/CSE'),
            ('ECE/CSE', 'ECE/CSE'),
        ]
    )
    puc_result = models.IntegerField()
    cet_rank = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=4)
    contact = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
    