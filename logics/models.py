from dataclasses import field
from pyexpat import model
from django.db import models
from rest_framework import serializers

# Create your models here.
class Plan(models.Model):
    price = models.TextField()
    details = models.TextField()

    def __ste__(self):
        return self.price



class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('price', 'details')


class Irigation(models.Model):
    index = models.IntegerField()
    plot = models.CharField(max_length = 5)
    startTime = models.CharField(max_length = 15)
    endTime = models.CharField(max_length = 15)
    Runby = models.CharField(max_length = 10)
    
    def __str__(self):
        return str(self.index)

class IrigationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irigation
        fields = ('index','plot','startTime','endTime','Runby')