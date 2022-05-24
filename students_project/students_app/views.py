from django.shortcuts import render

from .models import Students
from django.template import loader
from django.http import Http404, HttpResponse
from .form import addStudent

# Create your views here.

def index(request):
    student_list = Students.objects.all()
    template = loader.get_template('students_app/index.html')
    context = {
        'student_list': student_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, student_id):
    try:
        info_student = Students.objects.filter(pk=student_id)
    except Students.DoesNotExist:
        raise Http404('Student is not found')
    return render(request, 'students_app/detail.html', {'info_student': info_student})


def add(request):
    cont = {'uf':addStudent}
    return render(request, 'students_app/add.html', cont )

def getAdd(request):
    if request.method == 'POST':
        uf = addStudent(request.POST)
        if uf.is_valid():
            saveUF = Students(
                id = uf.cleaned_data['id'],
                name = uf.cleaned_data['name'],
                age = uf.cleaned_data['age'],
                address = uf.cleaned_data['address'],
                mobile_number = uf.cleaned_data['mobile_number']
            )
            saveUF.save()
            return HttpResponse('save success')

        else:
            return HttpResponse('form not value')
    else:
        return HttpResponse('not POST')