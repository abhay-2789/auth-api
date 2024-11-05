# views.py
from django.contrib.auth import authenticate, user_logged_in
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView, LoginView as KnoxLogoutAllView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from .serializers import UserCreationSerializer


class LoginView(KnoxLoginView):

    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        print(user)
        request.user = user
        token_limit_per_user = self.get_token_limit_per_user()
        if token_limit_per_user is not None:
            now = timezone.now()
            tokens = request.user.auth_token_set.filter(expiry__gt=now).order_by('created')
            token_cnt = tokens.count()
            if token_cnt >= token_limit_per_user:
                for cnt in range(token_cnt - token_limit_per_user + 1):
                    tokens[cnt].delete()
        token_ttl = self.get_token_ttl()
        instance, token = AuthToken.objects.create(request.user, token_ttl)
        user_logged_in.send(sender=request.user.__class__,
                            request=request, user=request.user)
        data = self.get_post_response_data(request, token, instance)
        return Response(data)


class LogoutView(KnoxLogoutView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response({
            'message': "Successfully logged"
        }, status=HTTP_200_OK)


class LogoutAllView(KnoxLogoutAllView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response({
            'message': "Successfully Logged Out"
        }, status=HTTP_200_OK)

class RegisterView(APIView):

    @staticmethod
    @csrf_exempt
    def post(request):
        serializer = UserCreationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'errors': serializer.errors
            })
        user = serializer.save()
        return Response({
            "message": "User Created Successfully"
        })


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        return Response({
            'data': "Hello World"
        })
