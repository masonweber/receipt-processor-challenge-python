import json
import uuid
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError
from requests import PreparedRequest, Request

from challenge.process import ingest, score

from openapi_core import OpenAPI
from openapi_core.contrib.requests import RequestsOpenAPIRequest

openapi = OpenAPI.from_file_path('request_validate.yml')

# Create your views here.

def process(request):  

    try:
        my_request = convert_request(request) # Reformat Django request for OpenAPI validate method
        openapi.validate_request(my_request) # Validate Message
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        # generate new uuid
        id = ingest(str(uuid.uuid4()), json.loads(request.body))
        return HttpResponse("{'id': '" + str(id) + "'}", content_type="application/json")

    except Exception as e:
        print("Error:", e)
        print("Cause:", e.__cause__)
        error = HttpResponseBadRequest("The receipt is invalid.")
        return error

    return HttpResponseServerError()

def points(request, id):

    try:
        r_score = score(id)
        return HttpResponse("{'points': " + str(r_score) + "}", content_type="application/json")
    except Exception as e:
        print("Error:", e)
        print("Cause:", e.__cause__)
        error = HttpResponseNotFound("No receipt found for that ID.")
        return error

    return HttpResponseServerError()


def convert_request(request):
    temp = Request(request.method, request.scheme + "://" + request.get_host() + request.path, request.headers, request.FILES, request.body, None, None, request.COOKIES, None, None)
    return RequestsOpenAPIRequest(temp.prepare())

