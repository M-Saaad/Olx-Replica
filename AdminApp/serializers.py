from rest_framework import serializers
from AdminApp.models import UserLogin, UserSignup, Laptops, Mobiles, UserDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserSignup
        fields = (
            'UserID', 
            'UserFirstName',
            'UserLastName', 
            'UserContactNo',
            'UserEmail',
            'UserPassword'
            )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetail
        fields = (
            'UserEmail',
            'UserFirstName',
            'UserLastName',
            'UserContactNo'
            )

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserLogin
        fields = (
            'UserEmail',
            'UserPassword'
            )

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Laptops
        fields = (
            'UserEmail',
            'LaptopId',
            'LaptopName',
            'LaptopImage',
            'LaptopScreenSize',
            'LaptopScreenResolution',
            'LaptopRam',
            'LaptopHDD',
            'LaptopSSD', 
            'LaptopDetails',
            'LaptopPrice'
            )

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobiles
        fields = (
            'UserEmail',
            'MobileId', 
            'MobileName',
            'MobileImage',
            'MobileRom', 
            'MobileScreen', 
            'MobilePrimaryCam', 
            'MobileSalfieCam', 
            'MobileBattery',
            'MobileDetails',
            'MobilePrice'
            )