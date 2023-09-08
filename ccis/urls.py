from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ti
from .views import cooperar
from .views import pages
from .views import rh
from .views import security
from .views import formularios
from .views import gestaoControle


urlpatterns = [
    path('base', pages.base, name='base'),

    path('login', security.loginPage, name='login'),
    path('conta', pages.conta, name='conta'),
    path('solicitacao', pages.solicitacao, name='solicitacao'),
    path('profile/<int:user_id>', pages.profile, name='profile'),
    path('', pages.home, name='home'),
    path('documentos', pages.documentos, name='documentos'),
    path('departamentos', pages.departamentos, name='departamentos'),
    path('gestaoMetas', pages.gestaoMetas, name='gestaoMetas'),

    path('utilitarios', pages.utilitarios, name='utilitarios'),

    path('gestaoControle', gestaoControle.home, name='gestaoControle'),
    path('contabilidade', gestaoControle.contabilidade, name='contabilidade'),
    path('comissionamento', gestaoControle.comissionamento, name='comissionamento'),
    path('estrategico', gestaoControle.estrategico, name='estrategico'),
    path('inadimplencia', gestaoControle.inadimplencia, name='inadimplencia'),
    path('lastro', gestaoControle.lastro, name='lastro'),
    path('qqs', gestaoControle.qqs, name='qqs'),
    path('pesquisa', gestaoControle.pesquisa, name='pesquisa'),

    path('coopera', cooperar.coopera, name='coopera'),
    path('relacionamento', cooperar.relacionamento, name='relacionamento'),
    path('simulador', cooperar.simulador, name='simulador'),
    path('tabela', cooperar.tabela, name='tabela'),
    path('india', cooperar.india, name='india'),
    path('portifolio', cooperar.portifolio, name='portifolio'),
    path('basileia', cooperar.basileia, name='basileia'),
    path('dados', cooperar.dadosConsolidados, name='dados'),

    path('logout', security.logout_view, name='logout'),
    path('new_login_page', pages.new_login_page, name='new_login_page'),
    path('redefinir_senha', security.redefinir_senha, name='redefinir_senha'),
    path('inativar_usuario/<int:user_id>', security.inativar_usuario, name='inativar_usuario'),

    path('formMidia', formularios.formMidia, name='formMidia'),
    path('formDep', formularios.formDep, name='formDep'),
    path('formEnd', formularios.formEnd, name='formEnd'),
    path('formEsc', formularios.formEsc, name='formEsc'),
    path('formCert', formularios.formCert, name='formCert'),
    path('formProf', formularios.formProf, name='formProf'),
    path('formBanc', formularios.formBanc, name='formBanc'),
    path('formOut', formularios.formOut, name='formOut'),

    path('rg', formularios.rg, name='rg'),
    path('cnh', formularios.cnh, name='cnh'),
    path('cpf', formularios.cpf, name='cpf'),
    path('reservista', formularios.reservista, name='reservista'),
    path('titulo', formularios.titulo, name='titulo'),
    path('clt', formularios.clt, name='clt'),
    path('residencia', formularios.residencia, name='residencia'),
    path('certidao', formularios.certidao, name='certidao'),
    path('admissional', formularios.admissional, name='admissional'),
    path('periodico', formularios.periodico, name='periodico'),

    path('security/password_reset', security.password_reset, name='password_reset'),
    path('security/password_done', security.password_done, name='password_done'),

    path('rh', rh.rh_home, name='rh_home'),
    path('rh/dashboard', rh.rh_dash, name='rh_dashboard'),
    path('rh/processo-seletivo', rh.pro_seletivo, name='pro-seletivo'),
    path('rh/ferias', rh.ferias, name='ferias'),
    path('rh/anbima', rh.anbima, name='anbima'),
    path('rh/colaboradores', rh.colaboradores, name='colaboradores'),
    path('rh/usuario', pages.usuario, name='usuario'),

    path('ti', ti.ti_home, name='ti_home'),
    path('ti/new_request', ti.new_request, name='new_request'),

    path('dev', pages.dev, name='dev'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


