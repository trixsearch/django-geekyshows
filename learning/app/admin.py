from django.contrib import admin
from .models import Profile,Result

# # Ye Simple Tareeka hai Model ko register karne ka isme __str__ method sey cheezein dikhengi
# admin.site.register(Profile)
# yaha per jis bhi model ko likhenge voh Admin Portal mein App Name k neeche likha aa jayega
admin.site.register(Result)

# Jab humko ek sey zyada fields register karni padhti hai toh hum ModelAdmin Class ka use karte hai
# isme pahle toh Class banakar fields define karni padhti hai 
# fir usko register karna padhta hai 
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','name','roll','city')

admin.site.register(Profile,ProfileAdmin)