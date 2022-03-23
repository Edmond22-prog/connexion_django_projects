from django.urls import path, include

from web2.views import ReceiveView

urlpatterns = [
    path('', ReceiveView.as_view(), name="home"),
    
]