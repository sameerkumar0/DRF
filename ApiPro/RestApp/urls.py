from django.urls import path
from . import views
urlpatterns=[
    # path('',views.student,name="student"),

    # api endpoints
    path('student',views.StudentsView,name="student")

]