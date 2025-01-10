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
        
@api_view(["POST"])
def new_note(req):
    if req.method=="POST":
        note = req.data
        serializer = NoteSerializer(data = note)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET","PUT","DELETE"])
def detail_note(req,slug):
    try:
        note=Note.objects.get(slug=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=="GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif req.method=="DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif req.method=="PUT":
        serializer = NoteSerializer(note,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



    


