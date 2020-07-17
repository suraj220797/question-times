from django.urls import path

from user_api.api.views import ProfileList

urlpatterns = [
    path('profiles', ProfileList.as_view(), name = 'profile-list'),
]
