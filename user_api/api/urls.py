from django.urls import path,  include
from rest_framework.routers import DefaultRouter

from user_api.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

router = DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('status', ProfileStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),
]
