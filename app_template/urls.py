from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from app_template.View.app_template_api_view import AppTemplateModelViewSet

router = DefaultRouter() 

router.register(r'app-templates', AppTemplateModelViewSet, basename='app_template')





urlpatterns = [
    path('', include(router.urls)),
]
