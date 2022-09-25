# Create your views here.
from rest_framework import mixins, viewsets
from apps.operation.ser import NoteFavSer,KolFavSer,KolFav,NoteFav,NoteFavDetailSer,KolFavDetailSer


class NoteFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = NoteFavSer

    def get_serializer_class(self):
        if self.action == "list":
            return NoteFavDetailSer
        elif self.action == 'create':
            return NoteFavSer
        else:
            return NoteFavSer

    def get_queryset(self):
        return NoteFav.objects.filter(user=self.request.user)

class KolFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = KolFavSer

    def get_serializer_class(self):
        if self.action == "list":
            return KolFavDetailSer
        elif self.action == 'create':
            return KolFavSer
        else:
            return KolFavSer

    def get_queryset(self):
        return KolFav.objects.filter(user=self.request.user)