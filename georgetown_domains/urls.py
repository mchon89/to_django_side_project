"""mywebsite URL Configuration

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


from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('python3/', views.python3_default, name='python3_default'),
    path('python3/<int:number>/', views.python3, name='python3'),
    path('tableau/', views.tableau_default, name='tableau_default'),
    path('tableau/<int:number>/', views.tableau, name='tableau'),
    path('ggplot2/', views.ggplot2, name='ggplot2'),
    path('network/', views.network_default, name='network_default'),
    path('network/<int:number>/', views.network, name='network'),
    path('plotly/', views.plotly_default, name='plotly_default'),
    path('plotly/<int:number>/', views.plotly, name='plotly'),
    path('leaflet/', views.leaflet_default, name='leaflet_default'),
    path('leaflet/<int:number>/', views.leaflet, name='leaflet'),
    path('wordcloud/', views.wordcloud, name='wordcloud'),
    path('takehome/', views.takehome_default, name='takehome_default'),
    path('takehome/<int:number>/', views.takehome, name='takehome')
]



