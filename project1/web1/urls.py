from django.urls import path
from web1.views import FormView

urlpatterns = [
    path('', FormView.as_view(), name="home"),
    
]