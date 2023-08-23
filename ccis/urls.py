from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('base', views.base, name='base'),
    path('login', views.loginPage, name='login'),
    path('conta', views.conta, name='conta'),
    path('solicitacao', views.solicitacao, name='solicitacao'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('documentos', views.documentos, name='documentos'),
    path('departamentos', views.departamentos, name='departamentos'),

    path('coopera', views.coopera, name='coopera'),
    path('relacionamento', views.relacionamento, name='relacionamento'),
    path('simulador', views.simulador, name='simulador'),
    path('tabela', views.tabela, name='tabela'),
    path('india', views.india, name='india'),
    path('portifolio', views.portifolio, name='portifolio'),
    path('basileia', views.basileia, name='basileia'),

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

    path('security/password_reset', views.password_reset, name='password_reset'),
    path('security/password_done', views.password_done, name='password_done'),

    path('rh', views.rh_home, name='rh_home'),
    path('rh/dashboard', views.rh_dash, name='rh_dashboard'),
    path('rh/processo-seletivo', views.pro_seletivo, name='pro-seletivo'),
    path('rh/ferias', views.ferias, name='ferias'),
    path('rh/anbima', views.anbima, name='anbima'),
    path('rh/colaboradores', views.colaboradores, name='colaboradores'),
    path('rh/usuario', views.usuario, name='usuario'),

    path('ti', views.ti_home, name='ti_home'),


    path('dev', views.dev, name='dev'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


