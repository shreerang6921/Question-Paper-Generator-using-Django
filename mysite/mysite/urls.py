from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('generatePaper', views.generatePaper,name='generatePaper'),
    path('about',views.about,name='about'),
    path('loginapp/', include('loginapp.urls')),
]
