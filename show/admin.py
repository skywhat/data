from django.contrib import admin
from show.models import rid_table
from show.models import data1
from django.contrib.admin.views.main import ChangeList
#for custom the filter
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

#from show.custom_admin import MultiDeleteModelAdmin
# Register your models here.

class SpeedFilter(SimpleListFilter):
    title=_('input a value for speed limit.')
    parameter_name='speed'

    def lookups(self,request,model_admin):
        return super(SpeedFilter,
                self).lookups(request,model_admin)

    def queryset(self,request,queryset):
            return queryset.filter(speed__gt=int(self.value()))


class data1_admin(admin.ModelAdmin):
    list_display=('timeStamp','latitude','longitude','speed',)
    #list_filter=('timeStamp','latitude','longitude','speed','altitude','altOffset','planeOffset','deviceX','deviceY','deviceZ','heartRate','isIntegerKM','pointDist','sportMode',)
    list_filter=(SpeedFilter,)
    search_fields=('timeStamp','latitude','longitude','speed','altitude','altOffset','planeOffset','deviceX','deviceY','deviceZ','heartRate','isIntegerKM','pointDist','sportMode',)
'''
    c=ChangeList(request,
                self.model,
                self.list_display,
                self.list_display_links,
                self.list_filter,
                self.data_hierarchy,
                self.search_fields,
                self.list_select_related,
                self.list_per_page,
                self.list_max_show_all,
                self.list_editable,
                self
            )
    filtered_query_set=c.get_query_set(request)
'''
admin.site.register(rid_table)
admin.site.register(data1,data1_admin)
