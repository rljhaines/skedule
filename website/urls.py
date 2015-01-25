from django.conf.urls import patterns, include, url
from rest_framework import generics, serializers
from website.models import Greeting 

class GreetingSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Greeting
        fields = ('id', 'text')

class GreetingList(generics.ListCreateAPIView):
    model=Greeting
    serializer_class = GreetingSerializer

class GreetingDetails(generics.RetrieveAPIView):
    model=Greeting
    serializer_class = GreetingSerializer

urlpatterns = patterns('',
   url(r'^greeting/$', GreetingList.as_view()),
   url(r'^greeting/(?P<pk>\d+)/$', GreetingDetails.as_view()),

)
