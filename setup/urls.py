from django.contrib import admin
from django.urls import path
from escola.views import alunos

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('alunos/', alunos, name='alunos'),
]
