from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse


class CBV_FORM(FormView):
    template_name='CBV_FORM.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('<h1>The data is inserted</h1>')