
from  rest_framework.viewsets import ModelViewSet 

from poster.Model.poster_model import PosterModel 
from poster.Serializer.poster_serializer  import (

    CreatePosterSerializer,
    GetPosterModelSerializer
)



class PostModelViewSet(ModelViewSet):

    queryset = PosterModel.objects.select_related('app_template')

    def get_serializer_class(self):

        if self.action in ['create','update','partial-update','destroy']:
            return CreatePosterSerializer
        
        return GetPosterModelSerializer