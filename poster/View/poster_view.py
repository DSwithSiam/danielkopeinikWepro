
from  rest_framework.viewsets import ModelViewSet 

from poster.Model.poster_model import PosterModel 
from poster.Serializer.poster_serializer  import (

    CreatePosterSerializer,
    GetPosterModelSerializer
)



class PostModelViewSet(ModelViewSet):

    queryset = PosterModel.objects.select_related('app_template')
    pagination_class = None 

    def get_serializer_class(self):

        if self.action in ['create','update','partial-update','destroy']:
            return CreatePosterSerializer
        
        return GetPosterModelSerializer
    

    def get_queryset(self):
        queryset = super().get_queryset()


        app_template = self.request.query_params.get('app_template')

        if app_template:

            queryset = queryset.filter(app_template=app_template)

        queryset = queryset.order_by('-created_at')

        
        return queryset