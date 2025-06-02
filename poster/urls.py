from django.urls import path , include 
from poster.View.poster_view import PostModelViewSet 

from poster.View.membership_view import MembershipPlanViewSet


from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('registers',PostModelViewSet,basename='poster_urls')
router.register('membership',MembershipPlanViewSet,basename='membership_urls')



urlpatterns = [
    path('', include(router.urls)),
]
