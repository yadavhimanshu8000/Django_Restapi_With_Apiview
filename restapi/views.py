from django.shortcuts import render
from restapi.models import *
from restapi.serializer import * 
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class userapi(APIView):
    def get(self, request, format=None):
        views = User.objects.all()
        serializer = userserializer(views, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        views = userserializer(data=request.data)
        if views.is_valid():
            views.save()
            return Response(views.data, status=status.HTTP_201_CREATED)
        return Response(views.errors, status=status.HTTP_400_BAD_REQUEST)

class userview(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = userserializer(store)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        value = self.get_object(pk)
        serializer = userserializer(value, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        value = self.get_object(pk)
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
class postapi(APIView):
    def get(self,request,format=None):
        views = Post.objects.all()
        serializer = postserializer(views, many=True)
        return Response(serializer.data)
    
    
    def post(self,request,format=None):
        serializer = postserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class postview(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        value = self.get_object(pk)
        serializer = postserializer(value)
        return Response (serializer.data)
    
    def put(self,request,pk,format=None):
        value = self.get_object(pk)
        serializer = postserializer(value,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        value = self.get_object(pk)
        value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class followsapi(APIView):
    
    def get(self,request,format=None):
        views = Follows.objects.all()
        serializer = followsserializer(views,many=True)
        return Response (serializer.data)
    
    def post(self,request,format=None):
        serializer = followsserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
class followsview(APIView):
    def get_object(self,pk):
        try:
            return Follows.objects.get(pk=pk)
        except Follows.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        value = self.get_object(pk=pk)
        serializer = followsserializer(value)
        return Response(serializer.data)
    
    
    
   
            
        
        
        
            
            
       
        
        
        
            
        
        
        
        
    
    
