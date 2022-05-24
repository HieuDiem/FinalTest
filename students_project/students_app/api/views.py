from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from students_app.models import Students
from .serializer import StuSerializer

class StuListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

#  get the list of Student
    def get(self, request, *args, **kwargs):
        students = Students.objects.filter(student = request.student.id)
        serializer = StuSerializer(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
#  add 
    def post(self, request, *args, **kwargs ):
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address'),
            'mobile_number': request.data.get('mobile_number')
        }
        serializer = StuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StuDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, student_id):
        try:
            return Students.objects(id=student_id)
        except Students.DoesNotExist:
            return None

    def get(self, student_id, *args, **kwargs):
        stu_instance = self.get_object(student_id)
        if not stu_instance:
            return Response(
                {"res":"Object with todo id does not exists"},
                status = status.HTTP_400_BAD_REQUEST
            )

        serializer = StuSerializer(stu_instance)
        return Response(serializer.data, status=status.HTTP_200_OK) 


# edit
    def put(self, request, student_id, *args, **kwargs):
        stu_instance = self.get_object(student_id)
        if not stu_instance:
            return Response(
                {"res": "Object student id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'id': request.data.get('id'),
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address'),
            'mobile_number': request.data.get('mobile_number')
        }
        serializer = StuSerializer(instance = stu_instance, data=data, partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete
    def delete(self, student_id):
        stu_instance = self.get_object(student_id)
        if not stu_instance:

            return Response(
                {"res": "Object doesn't not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        stu_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )