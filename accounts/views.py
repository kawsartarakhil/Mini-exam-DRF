from django.shortcuts import render
from .serailizers import RegisterSerailizer,Userserailizer
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])
def resgister_view(request):
    serailizer = RegisterSerailizer(data=request.data)
    serailizer.is_valid(raise_exception=True)
    serailizer.save()
    return Response({"message":"Registration successfull"},status=status.HTTP_201_CREATED)

@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error":"All fields are required"},status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request,username=username,password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({"refresh":str(refresh),"access":str(refresh.access_token)})

    return Response({"error":"Incorrect credintials"},status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token_view(request):
    serailizer = TokenRefreshSerializer(data=request.data)
    try:
        serailizer.is_valid(raise_exception=True)
    except Exception as err:
        return Response({"error":str(err)},status=status.HTTP_400_BAD_REQUEST)

    return Response(serailizer.data,status=status.HTTP_200_OK)

    
@api_view(["POST"])
@permission_classes([AllowAny])
def logout_view(request):
    token = request.data.get("refresh")
    refresh = RefreshToken(token)
    refresh.blacklist()
    return Response("Logout successfull",status=status.HTTP_200_OK)

