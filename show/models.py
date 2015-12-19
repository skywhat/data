from django.db import models

# Create your models here.

class mode(models.Model):
    recordId=models.CharField(max_length=10,primary_key=True)
    sportMode=models.IntegerField()
    heartRate=models.IntegerField()
    altOffset=models.FloatField()
    planeOffset=models.FloatField()
    def __unicode__(self):
        return self.recordId


class data(models.Model):
    timeStamp=models.DateTimeField(primary_key=True)
    Mode=models.ForeignKey(mode)
    altitude=models.FloatField()
    deviceX=models.FloatField()
    deviceY=models.FloatField()
    deviceZ=models.FloatField()
    isIntegerKM=models.IntegerField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    pointDist=models.FloatField()
    speed=models.FloatField()
