import os
from urllib import request
from uuid import uuid4

from django.contrib.auth.hashers import make_password, check_password

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

# Create your views here.
class Join(APIView):

    def get(self, request):
        return Response(status=200)
    def post(self, request):
         # todo 회원가입
         # TODO : 유효성 검사
        '''
            - user_name             : 사용자 이름
            - user_email            : 사용자 이메일
            - user_password         : 사용자 비밀번호
            - user_login_id         : 사용자 로그인 아이디
        '''
        user_name = request.data.get('user_name')
        user_email = request.data.get('user_email')
        user_password = request.data.get('user_password')
        user_login_id = request.data.get('user_login_id')
        print("회원가입 정보를 가저왔음 by post")

        User.obects.create(user_name=user_name,
                           user_email=user_email,
                           user_password=make_password(user_password),
                           user_login_id=user_login_id)
        return Response(status=200)
