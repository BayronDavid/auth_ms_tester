from rest_framework                       import status, views
from rest_framework.response              import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import generics

from AuthApp.models.user                    import User
from AuthApp.serializers.userSerializer import UserSerializer, UserPassengerSerializer, UserDriverSerializer, AllUsersSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        
        if request.data.get('typeAccount') == 'P':
            serializer = UserPassengerSerializer(data=request.data)
        elif request.data.get('typeAccount') == 'D':
            serializer = UserDriverSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True) 
        serializer.save() 

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData) 
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("ERROR", e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AllUsersSerializer
