"""
URL configuration for RenderData project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # FunctionBasedView urls
    path('fbv_insert/',fbv_insert,name='fbv_insert'),

    # ClsBasedView urls
    path('Render_data/',Render_data.as_view(),name='Render_data'),
    path('Cbv_insert/',Cbv_insert.as_view(),name='Cbv_insert'),
    path('Template/',Template.as_view(),name='Template'),
    # Class Based View with Direct TemplateView
    path('syeraa/',TemplateView.as_view(template_name='syeraa.html'),name='syeraa'),
    
    
]
