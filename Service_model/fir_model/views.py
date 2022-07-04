from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser
from .models import Fir,Techtracker,Customerissue
from .serializers import FirSerializer,TechtrackerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import django_filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

def index(request):
    return HttpResponse("WELCOME TO SERVICE")


class FirAPIView(APIView):
    model = FirSerializer
    fir = Fir.objects.all()
    serializer_class = FirSerializer

    def get(self,request):
        fir = Fir.objects.all()
        serializer = FirSerializer(fir,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = FirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FirDetail(APIView):
    def get_object(self, pk):
        try:
            return Fir.objects.get(pk=pk)
        except Fir.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fir = self.get_object(pk)
        serializer = FirSerializer(fir)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fir = self.get_object(pk)
        serializer = FirSerializer(fir, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        fir = self.get_object(pk)
        Fir.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 




class TechtrackerAPIView(APIView):
    model = TechtrackerSerializer
    techtracker = Techtracker.objects.all()
    serializer_class = TechtrackerSerializer

    def get(self,request):
        techtracker = Techtracker.objects.all()
        serializer = TechtrackerSerializer(techtracker,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TechtrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TechtrackerDetail(APIView):
    def get_object(self, pk):
        try:
            return Techtracker.objects.get(pk=pk)
        except Techtracker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        techtracker = self.get_object(pk)
        serializer = TechtrackerSerializer(techtracker)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        techtracker = self.get_object(pk)
        serializer = TechtrackerSerializer(techtracker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        techtracker = self.get_object(pk)
        Techtracker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

class CustomerList(APIView):
#    permission_classes=[IsAuthenticated,]
    def post(self,request,format=None):
        customer_issue = request.data['customer_issue']
        additional_info={}
        if customer_issue:
            additionalinfos=Customerissue.objects.get(id=customer_issue).additionalinfos.all()
            additional_info={p.name:p.id for p in additionalinfos}
        return JsonResponse(data=additional_info, safe=False)
