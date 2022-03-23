from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.views import View
from web1.forms import TontineForm
import requests



class FormView(View):
    template_name = "web1/form.html"
    forms_class = TontineForm
    

    def get(self, request):
        form = self.forms_class()
        return render(request, self.template_name, context={
            "form":form
        })

    @csrf_exempt
    def post(self, request):
        form = self.forms_class(data=request.POST)
        data = request.POST
        if form.is_valid():
            req = requests.post("http://127.0.0.1:8001/", data)
            print(req.text)
            return redirect("home")
        else:
            return render(request, self.template_name, context={
            "form":form
        })


