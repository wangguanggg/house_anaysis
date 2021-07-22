from django.urls import path
from . import views
urlpatterns = [
    path('showsell/', views.showsell_view),
    path('showsellbypage/', views.showsell_bypage),
    path("dropsell/",views.dropsell),
    path("modifysell/", views.modifysell),
    path("findsellbymsg/", views.findsellbymsg),

    path("showrest/", views.showrest_view),
    path("showrestbypage/", views.showrest_bypage),
    path("droprest/",views.droprest),
    path("modifyrest/", views.modifyrest),
    path("findrestbymsg/", views.findrestbymsg),

    path("charts/", views.echart),
    path("gethistdata/", views.gethistdata),
    path("getpiedata/", views.getpiedata),
    path("getlinedata/", views.getlinedata),
    path("getscatterdata/", views.getscatterdata),
]