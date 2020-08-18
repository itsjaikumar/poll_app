from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/', views.detail, name='detail'),
    path('<str:pk>/results/', views.results, name='results'),
    path('<str:pk>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name='resultsdata'),
]   