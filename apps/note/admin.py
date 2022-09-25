from django.contrib import admin

# Register your models here.
from apps.note.models import Info


class NoteManager(admin.ModelAdmin):
    list_display = ['aid','bvid','cid','copyright','ctime','des','duration','dynamic','mid','name','face','pic','pub_location','pubdate','short_link','view_n','danmaku','reply','favorite','coin','share','like_n']

admin.site.register(Info,NoteManager)