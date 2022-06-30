from asyncio import streams
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from api.models import Stdnt
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@csrf_exempt
def index(request):
    return render(request,"api/Index.html")

    #for in instance
def databyid(request, id):
    print("Data P is working")
    contact_data = Stdnt.objects.all() 
    fldata = Stdnt.objects.get(id = id)
    serializer = StudentSerializer(fldata)
    json_data = JSONRenderer().render(serializer.data)
    print("Data P is working")
    print(fldata)
    print(serializer)
    return HttpResponse(json_data, content_type='application/json')



# for Query set
def dataList(request):
    print("Data P is working")
    contact_data = Stdnt.objects.all() 
    # fldata = Stdnt.objects.get(id = roll)
    serializer = StudentSerializer(contact_data, many = True)
    json_data = JSONRenderer().render(serializer.data)
    print("Data P is working")
    print(contact_data) 
    print(serializer)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def create(request):
    print("create is called!!!!")
    if request.method == 'POST':
        print("post request passed")
        json_data = request.body
        print("This is json:")
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            print("Serializer pass")
            serializer.save()
            res = {'msg':'Data is Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='applicatyion/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='applicatyion/json')
    return HttpResponse("Not working Create")




# get Data 

def get_data(request):
    print("get is called!!!!")
    if request.method == 'GET':
        print("get request passed")
        json_data = request.body
        print("This is json:")
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            obj = Stdnt.objects.get(id = id)
            serializer = StudentSerializer(obj)
            # json_data = JSONRenderer().render(serializer.data)
            # res = {'msg':'Data is Retrived by id'}
            # json_data = JSONRenderer().render(json_data)
            # return HttpResponse(json_data, content_type ='applicatyion/json')
            return Response(serializer.data)

        obj = Stdnt.objects.all()
        serializer = StudentSerializer(obj , many = True)
        json_data = JSONRenderer().render(serializer.data)
        res = {'msg':'Data is Retrived all'}
        json_data = JSONRenderer().render(json_data)
        # return HttpResponse(json_data, content_type ='applicatyion/json')
        return Response(serializer.data)
    # return HttpResponse("GET not working Create")
    return Response(serializer.data)




@csrf_exempt
def update(request):
    print("update is called!!!!")
    if request.method == 'PUT':
        print("PUT request passed")
        json_data = request.body
        print("This is json:")
        print(json_data)
        stream = io.BytesIO(json_data)
        print("This is stream Byte:")
        print(stream)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        obj = Stdnt.objects.get(id=id) 
        serializer = StudentSerializer(obj,data = python_data,partial = True)
        if serializer.is_valid():
            print("Serializer pass")
            serializer.save()
            res = {'msg':'Data is Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type ='applicatyion/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type ='applicatyion/json')
    
    return HttpResponse("Not working Update Front")

@csrf_exempt  
def delete(request):
    print("update is called!!!!")
    if request.method == 'DELETE':
        print("DELETE request passed")
        json_data = request.body
        print("This is json:")
        print(json_data)
        stream = io.BytesIO(json_data)
        print("This is stream Byte:")
        print(stream)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        obj = Stdnt.objects.get(id=id) 
        obj.delete()
        res = {'msg':'Data is Deleted!!!!!'}
        json_data = JSONRenderer().render(res)

        return HttpResponse(json_data, content_type ='applicatyion/json')
    return HttpResponse("Not working Update Front")



