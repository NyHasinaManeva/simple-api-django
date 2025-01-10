from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Note
from .serializer import NoteSerializer

@api_view(["GET"])
def note(req):
    if req.method=="GET":
        try:
            notes = Note.objects.all()
            serializers = NoteSerializer(notes,many=True)
            return Response(serializers.data)
        except Note.DoesNotExist:
            return Response("N'existe pas",status=status.HTTP_404_NOT_FOUND)
    


