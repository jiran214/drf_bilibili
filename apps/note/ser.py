from rest_framework import serializers

# from note.models import VideoInfo, Note, NoteAddInfo, Comment, DetailInfo
from apps.note.models import Info,Danmu,Comment,Danmu_hotwords,Comment_hotwords


class NoteDanmuSer(serializers.ModelSerializer):
    class Meta:
        model = Danmu
        fields = '__all__'

class CommentHotWordsSer(serializers.ModelSerializer):
    class Meta:
        model = Comment_hotwords
        fields = '__all__'

class DanmuHotWordsSer(serializers.ModelSerializer):
    class Meta:
        model = Danmu_hotwords
        fields = ['hot_word','num']


class NoteCommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class NoteInfoSer(serializers.ModelSerializer):
    danmus=NoteDanmuSer(many=True)
    comments=NoteCommentSer(many=True)
    danmu_hotword=DanmuHotWordsSer(many=True)

    class Meta:
        model = Info
        fields = '__all__'
        depth=1
#
#
# class NoteSer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'
#         depth=1
#
#
# class NoteAddInfoSer(serializers.ModelSerializer):
#     class Meta:
#         model = NoteAddInfo
#         fields = '__all__'
#
#
# class DetailInfoSer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailInfo
#         fields = '__all__'
#
#
# class CommentSer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'