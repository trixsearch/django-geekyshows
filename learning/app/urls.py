from django.urls import path
from app.views import (template_tutorial as temptut,home,models_tutorial as modelt,student_registration as sturegis)

urlpatterns = [
    path('', home,name="home"),
    path('temp/', temptut,name="temp_tutorial"),
    path('modl/',modelt,name="modeltut"),
    path('register/student',sturegis,name="studentregister")
]