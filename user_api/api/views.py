from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from user_api.models import Profile, ProfileStatus
from user_api.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer
from user_api.api.permissions import UpdateOwnProfile, UpdateOwnProfleStatus


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return  profile_object


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, UpdateOwnProfile,]


class ProfileStatusViewSet(viewsets.ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, UpdateOwnProfleStatus]

    def perform_create(self, serialier):
        user_profile = self.request.user.profile
        serialier.save(user_profile=user_profile)
