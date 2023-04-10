from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.loginPage, name='login'),
    path('conta', views.conta, name='conta'),
    path('usuario', views.usuario, name='usuario'),
    path('solicitacao', views.solicitacao, name='solicitacao'),
    path('profile', views.profile, name='profile'),
    path('formLogin', views.formLogin, name='formLogin'),



    path('dev', views.dev, name='dev'),
    path('conta2', views.conta2, name='conta2'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

