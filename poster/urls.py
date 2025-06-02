from django.urls import path , include 
from poster.View.poster_view import PostModelViewSet 


from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('registers',PostModelViewSet,basename='poster_urls')



urlpatterns = [
    path('', include(router.urls)),
]
