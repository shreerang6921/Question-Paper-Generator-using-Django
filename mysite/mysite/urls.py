from django.contrib import admin
from django.urls import path, include
from mysite import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index, name='index'),
    path('generatePaper', views.generatePaper,name='generatePaper'),
    path('about',views.about,name='about'),
    path('loginapp/', include('loginapp.urls')),
    path('addQuestion',views.addQuestion, name='addQuestion'),
    path('getQuestion',views.getQuestion, name='getQuestion'),
    path('delete',views.delete, name='delete'),
    path('deleteQuestion',views.deleteQuestion, name='deleteQuestion'),
    path('deleteSuccess',views.deleteSuccess, name='deleteSuccess'),
]
