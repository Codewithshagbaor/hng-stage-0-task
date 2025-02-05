from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timezone

# Create your views here.


user_date = {
        "email": "dxtlive@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(),
        "github_url": "https://github.com/Codewithshagbaor/hng-stage-0-task.git"
    }
class getUserDate(APIView):
    def get(self, request):
        return Response(user_date, status=status.HTTP_200_OK)