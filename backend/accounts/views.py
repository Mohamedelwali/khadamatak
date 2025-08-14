from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import Profile
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ProfileSerializer , MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


User = get_user_model()

# عرض كل البروفايلات مع إمكانية الفلترة بالـ role (admin فقط)
class ProfilesListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = Profile.objects.all()
        role = self.request.query_params.get('role')  # مثال: /api/accounts/profiles/?role=worker
        if role:
            queryset = queryset.filter(role=role)
        return queryset


# تحديث بيانات البروفايل للمستخدم الحالي
class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


# عرض البروفايل الخاص بالمستخدم الحالي
class MyProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


# عرض بيانات المستخدم الحالي (في حالة لو محتاجين بيانات أكتر)
class MeView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
