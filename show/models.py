from django.db import models

# Create your models here.
class rid_table(models.Model):
    recordId=models.IntegerField(default=0,primary_key=True)
    table_name=models.CharField(max_length=16)
    def __unicode__(self):
        return self.table_name

class data1(models.Model):
    altOffset=models.DecimalField(decimal_places=16,max_digits=26)
    altitude=models.DecimalField(decimal_places=16,max_digits=26)
    deviceX=models.DecimalField(decimal_places=16,max_digits=26)
    deviceY=models.DecimalField(decimal_places=16,max_digits=26)
    deviceZ=models.DecimalField(decimal_places=16,max_digits=26)
    heartRate=models.IntegerField()
    isIntegerKM=models.IntegerField()
    latitude=models.DecimalField(decimal_places=16,max_digits=26)
    longitude=models.DecimalField(decimal_places=16,max_digits=26)
    planeOffset=models.DecimalField(decimal_places=16,max_digits=26)
    pointDist=models.DecimalField(decimal_places=16,max_digits=26)
    speed=models.DecimalField(decimal_places=16,max_digits=26)
    sportMode=models.IntegerField()
    timeStamp=models.DateTimeField(primary_key=True)



