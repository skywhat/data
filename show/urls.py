from django.conf.urls import patterns,include,url

urlpatterns=patterns('',
    url(r'^$','show.views.index',name="index"),

)
