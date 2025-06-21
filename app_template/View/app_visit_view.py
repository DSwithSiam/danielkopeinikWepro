from  rest_framework.viewsets import ModelViewSet 

from app_template.Model.app_visit_model import AppVisitModel

from app_template.Serialiizer.app_visit_serializer import (
    CreateAppVisitSerializer,
    GetAppVisitSerializer
)
from rest_framework.permissions import IsAuthenticated


class  AppVisitModelViewSet(ModelViewSet):

    queryset = AppVisitModel.objects.select_related('user','template')

    permission_classes= [IsAuthenticated]


    def get_serializer_class(self):
        
        if self.action in ('create','update','partial_update','destroy'):
            return CreateAppVisitSerializer
        
        return GetAppVisitSerializer
    
    
    
    def perform_create(self,serializer):

        serializer.save(user=self.request.user)
    
    