from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User
from users.serializers import UserSerializer

class RegisterView(APIView):

	def post(self, request):
		# receives the parsed content of request body with key 'user'
		user = request.data.get('user')

		serializer = UserSerializer(data=user)

		# checks if all fields required in serializer are given
		if serializer.is_valid():

			# calls the create() in UserSerializer which creates a new User object
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)