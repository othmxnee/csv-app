import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class CSVUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        # The name 'file' corresponds to the name of the file input in the form
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        
        persons = []
        for row in reader:
            person, created = Person.objects.update_or_create(
                email=row['email'],
                defaults={
                    'full_name': row['full_name'],
                    'matricule': row['matricule'],
                    'password': row['matricule'],  # Assuming the password is the same as matricule
                }
            )
            persons.append(person)
        
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
