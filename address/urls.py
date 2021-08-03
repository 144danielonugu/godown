
from django.urls import path,include
from address import views
from django.contrib import admin
urlpatterns = [
    path("",views.home,name='home'),
    path("address",views.address,name="address"),
    path("login",views.login,name="login"),
    path("logout",views.logout),
    path("address/<id>",views.maddress,name='detail'),
    path('admin', admin.site.urls),


]
