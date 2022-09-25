import time
import django_filters
from apps.note.models import Info


class NoteFilter(django_filters.rest_framework.FilterSet):
    """
    kol 过滤类
    """

    # 视频数据








    view_n_max =django_filters.NumberFilter(field_name="view_n",lookup_expr='lte')
    view_n_min =django_filters.NumberFilter(field_name="view_n",lookup_expr='gte')
    danmaku_max =django_filters.NumberFilter(field_name="danmaku",lookup_expr='lte')
    danmaku_min =django_filters.NumberFilter(field_name="danmaku",lookup_expr='gte')
    reply_max =django_filters.NumberFilter(field_name="reply",lookup_expr='lte')
    reply_min =django_filters.NumberFilter(field_name="reply",lookup_expr='gte')
    favorite_max =django_filters.NumberFilter(field_name="favorite",lookup_expr='lte')
    favorite_min =django_filters.NumberFilter(field_name="favorite",lookup_expr='gte')
    coin_max = django_filters.NumberFilter(field_name="coin",lookup_expr='lte')
    coin_min = django_filters.NumberFilter(field_name="coin",lookup_expr='gte')
    share_max = django_filters.NumberFilter(field_name="share",lookup_expr='lte')
    share_min = django_filters.NumberFilter(field_name="share",lookup_expr='gte')
    like_n_max = django_filters.NumberFilter(field_name="like_n",lookup_expr='lte')
    like_n_min = django_filters.NumberFilter(field_name="like_n",lookup_expr='gte')

    # 热门标签过滤
    # title=django_filters.CharFilter(field_name='title',lookup_expr='icontains')

    # 基础信息：时长(单位：秒)、类型、团队、活动、观众性别
    duration_min = django_filters.NumberFilter(field_name="duration",lookup_expr='gte')
    duration_max = django_filters.NumberFilter(field_name="duration",lookup_expr='lte')

    # 发布时间
    pubdate = django_filters.NumberFilter(method="pubdate_filter",help_text="发布时间多少天以内")
    # 高级筛选

    def pubdate_filter(self,queryset, name, value,):
        """
        1、天数
        time.time() + 86400 * 7  # 当前时间的后7天
        # 2、小时
        time.time() + 3600 * 7  # 当前时间的后7小时
        # 3、分钟
        time.time() + 60 * 7  # 当前时间的后7分钟
        """
        ts = time.time() - 86400 * int(value)
        print(ts)
        return queryset.filter(pubdate__gte=ts)

    class Meta:
        model = Info
        fields = ['tid','tname','copyright']
