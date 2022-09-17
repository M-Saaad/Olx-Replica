from re import S
from django.http import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AdminApp.models import Laptops, Mobiles, UserDetail
from AdminApp.serializers import UserSerializer, LoginSerializer, LaptopSerializer, MobileSerializer, UserDetailSerializer

from django.core.files.storage import default_storage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

@csrf_exempt
def userSignupApi(request):
    if request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data = users_data)
        userDetail_serializer = UserDetailSerializer(data = users_data)
        if users_serializer.is_valid() and userDetail_serializer.is_valid():
            if User.objects.filter(email=users_serializer.data["UserEmail"]).exists():
                return JsonResponse('Email Already Taken', safe=False)
            else:
                userDetail_serializer.save()
                user = User.objects.create_user(username=users_serializer.data["UserEmail"], first_name=users_serializer.data["UserFirstName"], last_name=users_serializer.data["UserLastName"], email=users_serializer.data["UserEmail"], password=users_serializer.data["UserPassword"])
                user.save()
                return JsonResponse('Registred Successfully', safe=False)
        else:
            return JsonResponse('Registred Unsuccessfully', safe=False)

def userLoginApi(request):
    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        login_serializer = LoginSerializer(data = login_data)
        if login_serializer.is_valid():
            user = authenticate(username=login_serializer.data["UserEmail"], password=login_serializer.data["UserPassword"])
            if user is not None:
                return JsonResponse('Login Successful', safe=False)
            else:
                return JsonResponse('Invalid Login', safe=False)
        else:
            return JsonResponse('Login Failed', safe=False)

def userDetailApi(request):
    if request.method == 'POST':
        userDetail = UserDetail.objects.all()
        userEmail = (JSONParser().parse(request))["UserEmail"]
        userDetail_serializer = UserDetailSerializer(userDetail, many=True)
        for item in userDetail_serializer.data:
            if userEmail == item["UserEmail"]:
                apiResponse = item["UserContactNo"]
            else:
                apiResponse = "No User Found!"
        return JsonResponse(apiResponse, safe=False)

def laptopApi(request, id=0):
    if request.method == 'GET':
        laptops = Laptops.objects.all()
        laptops_serializer = LaptopSerializer(laptops, many=True)
        return JsonResponse(laptops_serializer.data, safe=False)
    elif request.method == 'POST':
        laptops_data = JSONParser().parse(request)
        laptops_serializer = LaptopSerializer(data = laptops_data)
        if laptops_serializer.is_valid():
            laptops_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        laptops_data = JSONParser().parse(request)
        laptop = Laptops.objects.get(LaptopId = laptops_data['LaptopId'])
        laptops_serializer = LaptopSerializer(laptop, data = laptops_data)
        if laptops_serializer.is_valid():
            laptops_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        laptop = Laptops.objects.get(LaptopId = id)
        laptop.delete()
        return JsonResponse("Deleted Seccessfully", safe=False)

@csrf_exempt
def mobileApi(request, id=0):
    if request.method == 'GET':
        mobiles = Mobiles.objects.all()
        mobiless_serializer = MobileSerializer(mobiles, many=True)
        return JsonResponse(mobiless_serializer.data, safe=False)
    elif request.method == 'POST':
        mobiles_data = JSONParser().parse(request)
        mobiles_serializer = MobileSerializer(data = mobiles_data)
        if mobiles_serializer.is_valid():
            mobiles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        mobiles_data = JSONParser().parse(request)
        mobile = Mobiles.objects.get(MobileId = mobiles_data['MobileId'])
        mobile_serializer = MobileSerializer(mobile, data = mobiles_data)
        if mobile_serializer.is_valid():
            mobile_serializer.save()
            return JsonResponse("Update Sucessfully", safe=False)
        return JsonResponse('Failed to Update', safe=False)
    elif request.method == 'DELETE':
        mobile = Mobiles.objects.get(MobileId = id)
        mobile.delete()
        return JsonResponse("Deleted Seccessfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    filename = default_storage.save(file.name, file)
    return JsonResponse("http://localhost:8000/Photos/" + filename, safe=False)