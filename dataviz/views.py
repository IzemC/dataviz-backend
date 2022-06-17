from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import YPSerializer, GZSerializer
from .models import YPModel, GZModel
 
from . import pagination

class GZViewSet(viewsets.ModelViewSet):

    queryset = GZModel.objects.all()
    serializer_class = GZSerializer
    pagination_class = pagination.DefaultPagination

    @action(detail=False, methods=['get'])
    def get_all(self, request):
        res = GZModel.objects.all()
        serializer = self.get_serializer(res, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        GZModel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class YPViewSet(viewsets.ModelViewSet):

    queryset = YPModel.objects.all()
    serializer_class = YPSerializer
    pagination_class = pagination.DefaultPagination

    @action(detail=False, methods=['get'])
    def get_all(self, request):
        res = YPModel.objects.all()
        serializer = self.get_serializer(res, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        YPModel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)