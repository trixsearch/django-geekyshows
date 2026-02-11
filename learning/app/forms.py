from django import forms

class RegisterStudent(forms.Form):
    student_name = forms.CharField()
    student_roll=forms.IntegerField()
    student_email=forms.EmailField()
    student_city=forms.CharField()
    student_phone=forms.IntegerField()