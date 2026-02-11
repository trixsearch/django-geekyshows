from django.contrib import admin
from .models import Profile,Result,Teacher

# # Ye Simple Tareeka hai Model ko register karne ka isme __str__ method sey cheezein dikhengi
# admin.site.register(Profile)
# yaha per jis bhi model ko likhenge voh Admin Portal mein App Name k neeche likha aa jayega
admin.site.register(Result)

# Jab humko ek sey zyada fields register karni padhti hai toh hum ModelAdmin Class ka use karte hai
# isme pahle toh Class banakar fields define karni padhti hai 
# fir usko register karna padhta hai 
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','name','roll','city')
# iske baad code mein kahi bhi humko register karne k liye aise likhna padega
admin.site.register(Profile,ProfileAdmin)

# hum chahe toh ek or tarike sey register kar sakte hai decorator ka prayog karke
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','t_name')