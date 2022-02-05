from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer


class UserLoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

class UserSignupSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            is_superuser=False,

        )
        print(validated_data)
        print(validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


# {
#             "id": 1,
#             "last_login": "2022-02-05T07:04:29.303583Z",
#             "is_superuser": true,
            # "username": "admin",
            # "first_name": "",
            # "last_name": "",
            # "email": "",
#             "is_staff": true,
#             "is_active": true,
#             "date_joined": "2022-02-04T19:50:47.012492Z",
#             "groups": [],
#             "user_permissions": []
#         }