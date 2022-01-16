from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /article/5/
    path('<int:project_id>/', views.detail, name='detail'),
]