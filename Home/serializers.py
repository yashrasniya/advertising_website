from rest_framework import serializers
from .models import *

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class Hoarding_data(serializers.ModelSerializer):
    images=serializers.SerializerMethodField()

    class Meta:
        model = Hoarding
        fields = '__all__'

    def get_images(self,obj):
        oo=obj.images.all()
        d=[]
        for i in oo:
            if i.img:
                d.append(i.img.url)
        return d

