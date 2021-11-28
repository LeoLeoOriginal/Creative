"""LeoArts002 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lobby.views import lob
from Home.views import home
from Pulseras.views import pul
from Purchase.views import pur
from Us.views import us
from Offer.views import of
from Proximamente.views import pro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lob),
    path('home/', home),
    path('home/pulsera/', pul),
    path('pulsera/', pul),
    path('home/us/', us),
    path('us/', us),
    path('home/pulsera/pur/<style>', pur),
    path('pur/<style>', pur),
    path('home/pulsera/of/', of),
    path('of/',of),
    path('soon/',pro),
    path('home/soon/',pro)
]
