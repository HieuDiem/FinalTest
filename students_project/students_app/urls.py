from django.urls import re_path, include
from . import views

app_name = 'students_app'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),

    re_path(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'details/(?P<student_id>[0-9]+)/$', views.detail, name='detail'),

    re_path(r'^add$', views.add, name='add'),
    re_path(r'^getAdd$', views.getAdd, name='getAdd'),

    re_path('api/', include('students_app.api.urls'))

]