from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('updatepwd/', views.updatepwd),
    path('info/', views.info),
    path('logout/', views.logout_view)
]