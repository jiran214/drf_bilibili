import django_filters
from apps.kol.models import Info


class KolFilter(django_filters.rest_framework.FilterSet):
    """
    kol 过滤类
    """
    followermin=django_filters.NumberFilter(field_name="follower",lookup_expr='gte')
    followermax=django_filters.NumberFilter(field_name="follower",lookup_expr='lte')
    role_type = django_filters.NumberFilter(method='role_type_filter',help_text="0：无认证 1：个人认证 2机构认证")
    title=django_filters.CharFilter(field_name='title',lookup_expr='icontains')

    #更具视频内容找up主
    notes_title=django_filters.CharFilter(field_name='notes__title',lookup_expr='icontains')

    def role_type_filter(self,queryset, name, value,):
        """
        根据认证类型筛选up主
        """
        if value ==1:
            return queryset.filter(role_type__in=[1,2,7,9],)
        elif value ==2:
            return queryset.filter(role_type__in=[3,4,5,6])
        elif value==0:
            return queryset.filter(role_type=0)
        else:
            pass


    class Meta:
        model = Info
        fields = ['sex','notes__id']
