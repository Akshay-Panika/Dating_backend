from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ye login kiye hue user ki profile return karega
        return self.request.user.profile