from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user_api.models import Profile
from user_api.api.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
