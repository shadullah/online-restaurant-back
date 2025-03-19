from django.contrib.auth import authenticate,logout
from .models import User
from .serializers import UserSerializer,LoginSerializer

from rest_framework import mixins,viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

    def create(self, req):
        serializer = self.get_serializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        if 'password' in req.data:
            user.set_password(req.data['password'])
            user.save()
            return Response("User Registered successfully")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, req, *args, **kwages):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=req.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()

        if 'password' in req.data:
            user.set_password(req.data['password'])
            user.save()
        return Response(serializer.data)

    @action(detail=False , methods=['GET'])
    def profile(self, request):
        user=request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access':str(refresh.access_token),
                'user_id':user.id,
                'email':user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    permission_classes=(AllowAny,)

    def post(self, req):
        try:
            req.user.auth_token.delete()
        except:
            pass
        logout(req)
        return Response({"message":"Logout Successful"})