from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import FarpostAd, User
from serializers import FarpostAdSer

class RegisterAPIView(APIView):
    def post(self, request):
        try:
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        try:
            user = authenticate(
                username=request.data['username'],
                password=request.data['password']
            )
            if user:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
class FarpostAdAPIView(APIView):
    @login_required
    def get(self, request, ad_id):
        try:
            ad = FarpostAd.objects.get(ad_id=ad_id)
            serializer = FarpostAdSer(ad)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FarpostAd.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)