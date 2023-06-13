from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('login', views.loginPage, name='login'),
    path('usuario', views.usuario, name='usuario'),
    path('conta/<int:user_id>', views.conta, name='conta'),
    path('solicitacao', views.solicitacao, name='solicitacao'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('documentos/<int:user_id>', views.documentos, name='documentos'),

    path('logout', views.logout_view, name='logout'),
    path('new_login_page', views.new_login_page, name='new_login_page'),
    path('redefinir_senha', views.redefinir_senha, name='redefinir_senha'),
    path('inativar_usuario/<int:user_id>', views.inativar_usuario, name='inativar_usuario'),

    path('formMidia', views.formMidia, name='formMidia'),
    path('formDep', views.formDep, name='formDep'),
    path('formEnd', views.formEnd, name='formEnd'),
    path('formEsc', views.formEsc, name='formEsc'),
    path('formCert', views.formCert, name='formCert'),
    path('formProf', views.formProf, name='formProf'),
    path('formBanc', views.formBanc, name='formBanc'),
    path('formOut', views.formOut, name='formOut'),

    path('rg', views.rg, name='rg'),
    path('cnh', views.cnh, name='cnh'),
    path('cpf', views.cpf, name='cpf'),
    path('reservista', views.reservista, name='reservista'),
    path('titulo', views.titulo, name='titulo'),
    path('clt', views.clt, name='clt'),
    path('residencia', views.residencia, name='residencia'),
    path('certidao', views.certidao, name='certidao'),
    path('admissional', views.admissional, name='admissional'),
    path('periodico', views.periodico, name='periodico'),

    path('dev', views.dev, name='dev'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


