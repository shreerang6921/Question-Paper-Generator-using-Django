from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from mysite import views
from .views import GeneratePdf

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.index, name='index'),
    path('generatePaper', views.generatePaper,name='generatePaper'),
    path('about',views.about,name='about'),
    path('loginapp/', include('loginapp.urls')),
    path('addQuestion',views.addQuestion, name='addQuestion'),
    path('addSuccess',views.addSuccess, name='addSuccess'),
    path('delete',views.delete, name='delete'),
    path('deleteQuestion',views.deleteQuestion, name='deleteQuestion'),
    path('deleteSuccess',views.deleteSuccess, name='deleteSuccess'),
    # path('generatePaper2', views.generatePaper2, name='generatePaper2'),
    path('pdf/paper.html', GeneratePdf.as_view()),
]
