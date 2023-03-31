from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('conta', views.conta, name='conta'),
    path('usuario', views.usuario, name='usuario'),
    path('solicitacao', views.solicitacao, name='solicitacao'),
    path('profile', views.profile, name='profile'),
    path('formLogin', views.formLogin, name='formLogin'),
    path('formDadosPessoais', views.formDadosPessoais, name='formDadosPessoais'),
    path('formDependentes', views.formDependentes, name='formDependentes'),
    path('formEnd', views.formEnd, name='formEnd'),
    path('formEscolaridade', views.formEscolaridade, name='formEscolaridade'),
    path('formCertif', views.formCertif, name='formCertif'),
    path('formProficional', views.formProficional, name='formProficional'),
    path('formDadosBancarios', views.formDadosBancarios, name='formDadosBancarios'),
    path('formMidia', views.formMidia, name='formMidia'),
    path('formOutros', views.formOutros, name='formOutros'),
    path('dev', views.dev, name='dev'),
    path('base', views.base, name='base'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

