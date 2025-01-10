from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializers):
    class Meta:
        model = Note
        fiels = ('id','title','body','slug','created','updated')
