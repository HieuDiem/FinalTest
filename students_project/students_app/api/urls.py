from django.urls import re_path, include
from .views import (StuListApiView, StuDetailApiView)

urlpatterns=[
    re_path('', StuListApiView.as_view()),
    re_path('<int:student_id>/', StuDetailApiView.as_view()),
]