from django.contrib import auth
from django.db.models import fields
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer 
from django.contrib import auth 
from pages import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = auth.get_user_model
        fields = ('id','email','username','password','first_name','last_name','phone')

        
class ppUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ppUser
        fields = '__all__'
        read_only_fields = ['id','yt']

class followEventSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.followEvent
        fields = '__all__'

class viewing2Serializers(serializers.ModelSerializer):
    class Meta:
        model = models.viewing2
        fields = '__all__'

class feedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.feedback
        fields = '__all__'

class photoLikedSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.photoLiked
        fields = '__all__'

class photoLiked2Serializers(serializers.ModelSerializer):
    class Meta:
        model = models.photoLiked2
        fields = '__all__'

class photoBlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.photoBlock
        fields = '__all__'

class photoBlock2Serializers(serializers.ModelSerializer):
    class Meta:
        model = models.photoBlock2
        fields = '__all__'

class photoSaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.photoSave
        fields = '__all__'