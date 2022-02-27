from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
# from .permission import IsAuthor
from .serializers import UserSerializer
from .models import CustomUser

import re
import uuid


def generate_session_token(length=35):
    uid = uuid.uuid4()
    return str(uid)


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send a post request with valid paramenter only'})

    username = request.POST['email']
    password = request.POST['password']

    print(username)
    print(password)

# validation part
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'error': 'Enter a valid email'})

    if len(password) < 3:
        return JsonResponse({'error': 'Password needs to be at least of 3 char'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': "Previous session exists!"})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid Email'})


def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create' : [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            # Return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            # If action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
        