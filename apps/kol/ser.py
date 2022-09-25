from rest_framework import serializers
from apps.kol.models import Info as kol_info
from apps.note.models import Info as note_info

class NoteInfoSer(serializers.ModelSerializer):
    class Meta:
        model = note_info
        fields = '__all__'

class KolInfoSer(serializers.ModelSerializer):
    notes=NoteInfoSer(many=True,read_only=True)
    class Meta:
        model = kol_info
        fields = '__all__'