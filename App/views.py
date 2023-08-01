from django.shortcuts import render

# Create your views here.
from django.views.generic import  View,TemplateView
from django.http import HttpResponse
from App.forms import *

# Rednering data using CBV
class Render_data(View):
    def get(self,request):
        d={'name':'Narasimha'}
        return render(request,'Render_data.html',d)

# Inserting data using FBV
def fbv_insert(request):
    d={'SFO':StudentForm()}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h1><b> FBV-Data Inserted </b></h1></center>')
    return render(request,'fbv_insert.html',d)

# Inserting data using CBV
class Cbv_insert(View):
    def get(self,request):
        d={'SFO':StudentForm()}
        return render(request,'Cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save() 
            return HttpResponse('<center><h1><b> CBV-Data Inserted </b></h1></center>')
        return render(request,'Cbv_insert.html')
    
class Template(TemplateView):
    template_name='Template.html'