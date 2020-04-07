from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail')
    # url(r'^news/(?P<word>\d+)/$', views.news_detail, name='news_detail')
    # url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail')

]
