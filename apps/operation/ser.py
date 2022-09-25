from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.operation.models import NoteFav,KolFav
from apps.kol.ser import kol_info
from apps.note.models import Info as note_info

"""
InfoSer：序列化收藏笔记、kol
FavSer：插入数据的反序列化器
FavDetailSer：查看的序列化器
"""
class NoteInfoSer(serializers.ModelSerializer):

    class Meta:
        model = note_info
        fields = '__all__'

class NoteFavDetailSer(serializers.ModelSerializer):
    notes = NoteInfoSer(read_only=True)
    class Meta:
        model = NoteFav
        fields = ['user','id','notes']

class NoteFavSer(serializers.ModelSerializer):
    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = NoteFav
        fields = ['user','id','notes']

        validators = [
            UniqueTogetherValidator(
                queryset=NoteFav.objects.all(),
                fields=('user', 'notes'),
                message="已经收藏"
            )
        ]

        # extra_kwargs = {'notes': {'read_only': True}}

class KolInfoSer(serializers.ModelSerializer):

    class Meta:
        model = kol_info
        fields = '__all__'

class KolFavDetailSer(serializers.ModelSerializer):
    kols = KolInfoSer(read_only=True)
    class Meta:
        model = KolFav
        fields = ['id','kols']

class KolFavSer(serializers.ModelSerializer):

    # 获取当前登录的用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = KolFav
        fields = ['user','kols', 'id']
        validators = [
            UniqueTogetherValidator(
                queryset=KolFav.objects.all(),
                fields=('user', 'kols'),
                message="已经收藏"
            )
        ]
