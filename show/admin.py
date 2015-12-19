from django.contrib import admin
from show.models import mode
from show.models import data

# Register your models here.

class mode_admin(admin.ModelAdmin):
    list_display=('recordId','sportMode','heartRate','altOffset','planeOffset')

class data_admin(admin.ModelAdmin):
    list_display=('timeStamp','latitude','longitude','speed','pointDist','isIntegerKM',)
    list_filter=('timeStamp','latitude','longitude','speed','altitude','deviceX','deviceY','deviceZ','isIntegerKM','pointDist')
    search_fields=('timeStamp','latitude','longitude','speed','altitude','deviceX','deviceY','deviceZ','isIntegerKM','pointDist')
    

admin.site.register(mode,mode_admin)
admin.site.register(data,data_admin)
