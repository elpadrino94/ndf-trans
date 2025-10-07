from django.urls import path
from NDF import settings
from ndfapp import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('avis/', views.avis, name='avis'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
