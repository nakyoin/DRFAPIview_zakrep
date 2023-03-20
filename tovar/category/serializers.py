from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance
    #
    #     return Response({'post': serializer.data })

    def put (self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method lalala"})

        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({'error': 'lalalal'})

        serializer = ProdSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'delete not allowed'})

        w = Product.objects.get(pk=pk)
        w.delete()

        return Response({'post': 'delete post' + str(pk)})

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'



