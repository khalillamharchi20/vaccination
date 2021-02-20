from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

#app_name="rendu_vous"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('rdv/', views.rdv, name='rdv'),
    path('post_question/',views.post_question, name='post_question'),
    path('blog/',views.blog, name='blog'),
    path('map/', views.map, name='map'),
    path('user/<str:pk>', views.user, name='user'),
    # path('pdf/', views.render_pdf_view, name='pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)