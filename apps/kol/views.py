# Create your views here.
# from django_filters import filters

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from apps.kol.filters import KolFilter
from apps.kol.models import Info
from apps.kol.ser import KolInfoSer


class KolPagination(PageNumberPagination):
    """
    自定义分页类
    """
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100
    # ordering = ['bv']


class CustomSearchFilter(filters.SearchFilter):
    """
    定制化搜索
    """

    def get_search_fields(self, view, request):
        filed_search=('user_name', 'mid', 'sign','tag')
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
                    if i==3 or i==4:
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

# Create your views here.
class KolInfoViewSet(CacheResponseMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    """

    """

    # 认证权限
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser, IsAuthenticated]
    # throttle_classes = [AnonRateThrottle]
    pagination_class = KolPagination

    queryset = Info.objects.all()
    serializer_class = KolInfoSer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # filter_fields=['user_name','title']
    filter_class = KolFilter
    # 根据用户权限选择mid、name、sign、认证信息、标签作为动态搜索条件
    search_fields = ['']
    # 还可根据互动数据和指数排序
    ordering_fields = ('follower', 'play_view')
