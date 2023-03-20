from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Cart
from django.forms.models import model_to_dict
from .serializers import ProdSerializer, CartSerializer


class ProdApiView(APIView):

    def post(self, request):
        serializer = ProdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post' : serializer.data})


    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            w = Product.objects.all()
            return Response({'posts': ProdSerializer(w, many=True).data})
        w = Product.objects.get(pk=pk)
        return Response({'posts': ProdSerializer(w).data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id is required'})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error': 'object not found'})

        serializer = ProdSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'id is required'})

        w = Product.objects.get(pk=pk)
        w.delete()

        return Response({'post': 'delete post' + str(pk)})

class CartApi(APIView):
    def get(self, request):
        cartproducts = Cart.objects.all()
        serializer = CartSerializer(cartproducts, many=True)
        return Response({'cartproducts': serializer.data})





