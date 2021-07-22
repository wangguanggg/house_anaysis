from django.urls import path
from . import views
urlpatterns = [
    path('showbypage/', views.showbypage),
    path('show/', views.show),
    path('add/', views.add),
    path('delete/', views.delete),
    path('modify/', views.modify)
]