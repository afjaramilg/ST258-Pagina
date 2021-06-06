
from warnings import simplefilter
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import test_model
from .serializers import Simple_serializer
#@csrf_exempt
#def simple(request):
#    #perform something
#    method = request.method.lower()
#    if method == "get":
#        return JsonResponse({"data": [1, 2, 3, 4, 5]})
#    elif method == "post":
#        return JsonResponse({"data": "Data posted succesfully"})
#    elif method == "put":
#        return JsonResponse({"data": "Data updated succesfully"})
#    
#    return JsonResponse({"method" : request.method})

class Simple(APIView):

    def post(self, request):
        serializer = Simple_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({
            "data": serializer.data
        })

    def get(self, request):
        content = test_model.objects.all()
        return JsonResponse({
            "data": Simple_serializer(content, many=True).data
        })


    def put(self, request, *args, **kwargs):
        model_id = kwargs.get('id', None)
        if not model_id:
            return JsonResponse({
                "error": "Method /PUT/ NOT ALLOWED"
            })
        try:
            instance = test_model.objects.get(id=model_id)
        except:
            return JsonResponse({
                "error": "Object does not exist"
            })
        serializer = Simple_serializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({
            "data": serializer.data
        })