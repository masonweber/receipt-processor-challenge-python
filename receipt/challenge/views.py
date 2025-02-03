from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.forms import CharField
from django.core.validators import RegexValidator
from requests import PreparedRequest, Request
from rest_framework import serializers
from .receipt import Receipt
from openapi_core import OpenAPI
from openapi_core.contrib.requests import RequestsOpenAPIRequest

openapi = OpenAPI.from_file_path('api.yml')

# Create validators
sd_validator = RegexValidator(r"^[\\w\\s\\-]+$")
price_validator = RegexValidator(r"^\\d+\\.\\d{2}$")
# Serializers for request validation
class ItemSerializer(serializers.Serializer):
    shortDescription = serializers.CharField(required=True, validators=[sd_validator])
    price = serializers.CharField(required=True, validators=[price_validator])
# class ProcessSerializer(serializers.Serializer):



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the challenge index.")

def process(request):
    my_request = convert_request(request)
    print(type(my_request))
    try:
        print("try")
        openapi.validate_request(my_request)
        print("success")
    except Exception as e:
        print(e)
        print(e.__cause__)
        result = "nope"
    return HttpResponse(result)
    '''
    if request.method == 'POST':
        return HttpResponse("uuid")
    else:
        try:
            print("serialize ")
            item = ItemSerializer({"price":"hello", "shortDescription":"Lays Chips"})
        except:
            print("invalid")
        return HttpResponse(str(item["price"]))
    '''

def points(request, id):
    return HttpResponse(5)

def convert_request(request):
    temp = Request(request.method, request.scheme + "://" + request.get_host() + request.path, request.headers, request.FILES, request.body, None, None, request.COOKIES, None, None)
    return RequestsOpenAPIRequest(temp.prepare())