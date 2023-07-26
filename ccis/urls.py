from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView
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
    path('setor_home', views.setor_home, name='setor_home'),

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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),
         name='password_reset'),
    path('reset_password/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),

    path('rh/processo-seletivo', views.pro_seletivo, name='pro-seletivo'),
    path('rh/ferias', views.ferias, name='ferias'),
    path('rh/anbima', views.anbima, name='anbima'),
    path('rh/colaboradores', views.colaboradores, name='colaboradores'),
    path('rh/usuario', views.usuario, name='usuario'),
    path('dev', views.dev, name='dev'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


