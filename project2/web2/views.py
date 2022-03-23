from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from web2.models import Registration



class ReceiveView(View):
    template_name = "web2/home.html"

    
    @csrf_exempt
    def post(self, request):
        tontine = request.POST["tontine"]
        email = request.POST["email"]
        address = request.POST["address"]
        Registration.objects.create(tontine=tontine, email=email, address=address)
        return JsonResponse({"message":"Connecte post"})
