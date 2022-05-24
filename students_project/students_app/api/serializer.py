from rest_framework import serializers
from students_app.models import Students

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ["id", "name", "age", "address", "mobile_number"]