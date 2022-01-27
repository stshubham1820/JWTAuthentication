from dataclasses import fields
import imp
from rest_framework import serializers
from .models import *
class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Studpersonal
        fields = '__all__'
