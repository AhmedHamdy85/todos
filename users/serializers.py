from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,max_length=50)
    first_name = serializers.CharField(required=True) 
    last_name = serializers.CharField(required=True)  

    def create(self, validated_data):
        
        try:
            password= validated_data.pop('password')
        except:
            raise ValidationError ({
                "message":"password is requierd"
            })
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],  
            last_name=validated_data['last_name'] 
        )
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','password']