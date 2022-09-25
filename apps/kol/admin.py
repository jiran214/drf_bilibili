from django.contrib import admin

# Register your models here.
from apps.kol.models import Info


class KolManager(admin.ModelAdmin):
    list_display=['mid','user_name','sex','face','face_nft','sign','rank_n','user_level','silence','fans_badge','role_type','title','des','is_type','birthday','following','follower','play_view','likes']

admin.site.register(Info,KolManager)