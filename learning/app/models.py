from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    email=models.EmailField(max_length=200)
    city=models.CharField(max_length=100)
    phone=models.IntegerField() 

    # def __str__(self):
    #     # yaha jo bhi value dalenge , us naam sey entry dikhegi models k ander Admin Portal me
    #     return str(self.name)
    
class Result(models.Model):
    stu_class=models.CharField(max_length=50)
    marks=models.IntegerField()
    # agar is tarike sey nahi karna hai toh Model Admin Class admin.py mein likh dete hai
    # yaha mein Simple or normal way sey karke dikhaya hu
    def __str__(self):
        return str(self.stu_class)
    
class Teacher(models.Model):
    t_name = models.CharField(max_length=150)
    t_number = models.IntegerField()
    t_email = models.EmailField()
    
    def __str__(self):
        return str(self.t_name)