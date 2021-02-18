from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('rdv/', views.rdv, name='rdv'),
    path('post_question/',views.post_question, name='post_question'),
    path('blog/',views.blog, name='blog'),
    path('map/', views.map, name='map'),
    path('user/', views.pation, name='pation'),
]