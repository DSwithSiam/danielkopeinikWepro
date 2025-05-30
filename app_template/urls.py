from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from app_template.View.app_template_api_view import AppTemplateModelViewSet

from app_template.View.product_view import ProductModelViewSet

router = DefaultRouter() 

router.register(r'app-templates', AppTemplateModelViewSet, basename='app_template')
router.register(r'products',ProductModelViewSet,basename='product_base')





urlpatterns = [
    path('', include(router.urls)),
]
