from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from apps.note.ser import Info,Danmu,Comment,Danmu_hotwords,Comment_hotwords,\
    NoteInfoSer,NoteDanmuSer,NoteCommentSer,DanmuHotWordsSer,CommentHotWordsSer

from django.views.decorators.cache import cache_page
from apps.note import tasks

#celery
from celery.result import AsyncResult

class CustomSearchFilter(filters.SearchFilter):
    """
    定制化搜索
    """

    def get_search_fields(self, view, request):
        filed_search=('title', 'des', 'comment','tag')
        search_fileds=[]
        try:
            type=request.query_params.get('keyword_search_type')
            print(type)
            # if type is not None:
            #     type = int(type)
            # else:
            #     return response

            while type > 0:
                i = 1 # 位数
                if type & 1 == 1:
                    if i==2 or i==3:
                        #身份鉴权
                        if not request.user:
                            break
                    search_fileds.append(filed_search[i-1])
                type = type >>1
                i+=1

        except Exception as e:
            print(e)

        # print(request.user)
        # return super(CustomSearchFilter, self).get_search_fields(view, request)
        print(search_fileds)
        return search_fileds

class NotePagination(PageNumberPagination):
    """
    自定义分页类
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100
    # ordering = ['bv']

# Create your views here.

class NoteInfoViewSet(CacheResponseMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """

    """
    data = {
        "cid": 1,
        "aid": 1,
        "bv": "BV1****1b7pv",
        "title": "测试稿件1",
        "cover": "41544f38.jpg",
        "tid": 230,
        "no_reprint": 1,
        "desc": "11111111",
        "tag": "生活记录,音乐",
        "copyright": 1,
        # "ctime": 1637208454,
        # "ptime": 1637208509
    }
    # 认证权限
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [VipPermission]
    throttle_classes = [AnonRateThrottle]

    queryset = Info.objects.all()
    serializer_class = NoteInfoSer
    pagination_class = NotePagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    # content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS

    # filter_class= NoteFilter
    search_fields = ('',)
    ordering_fields = ('view_n','danmaku','reply','favorite','coin','share','like_n')

    # def get_queryset(self):

    @method_decorator(cache_page(15))
    def dispatch(self, request, *args, **kwargs):
        # res = tasks.add.delay(2,2)
        # print({'status': res.status, 'task_id': res.task_id})
        # print(AsyncResult(res.task_id).result)
        return super().dispatch(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Comment.objects.all()
    serializer_class = NoteCommentSer

class CommentHotWordsViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Comment_hotwords.objects.all()
    serializer_class = CommentHotWordsSer

class DanmuHotWordsViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Danmu_hotwords.objects.all()
    serializer_class = DanmuHotWordsSer



