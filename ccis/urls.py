from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('login', views.loginPage, name='login'),
    path('conta', views.conta, name='conta'),
    path('usuario', views.usuario, name='usuario'),
    path('solicitacao', views.solicitacao, name='solicitacao'),
    path('profile', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),


    path('dev', views.dev, name='dev'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


