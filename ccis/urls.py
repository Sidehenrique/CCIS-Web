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
from .views import gestaoNegocios
from .views import retaguarda
from .views import produtoServico
from .views import financeiro
from .views import cadastro
from .views import adm
from .views import cobranca
from .views import secretaria
from .views import credito

urlpatterns = [
      path('base', pages.base, name='base'),

      path('login', security.loginPage, name='login'),
      path('conta', pages.conta, name='conta'),
      path('profile/<int:user_id>', pages.profile, name='profile'),
      path('', pages.home, name='home'),
      path('departamentos', pages.departamentos, name='departamentos'),

      path('processos', pages.processo, name='processos'),
      path('card_detl/<int:card_id>', pages.card_detl, name='card_detl'),

      path('utilitariosHome', pages.utilitariosHome, name='utilitarios'),
      path('utilitariosCopy', pages.utilitariosCopy, name='utilitariosCopy'),

      path('malotes', pages.malotes, name='malotes'),

      path('gestaoControle', gestaoControle.home, name='gestaoControle'),
      path('contabilidade', gestaoControle.contabilidade, name='contabilidade'),
      path('relatorios', gestaoControle.relatorios, name='relatorios'),
      path('estrategico', gestaoControle.estrategico, name='estrategico'),
      path('inadimplencia', gestaoControle.inadimplencia, name='inadimplencia'),
      path('lastro', gestaoControle.lastro, name='lastro'),
      path('qqs', gestaoControle.qqs, name='qqs'),
      path('pesquisa', gestaoControle.pesquisa, name='pesquisa'),

      path('gestaoNegocios', gestaoNegocios.home, name='gestaoNegocios'),
      path('gestaoMetas', gestaoNegocios.gestaoMetas, name='gestaoMetas'),
      path('diaria', gestaoNegocios.diaria, name='diaria'),
      path('listasPropensos', gestaoNegocios.listasPropensos, name='listasPropensos'),
      path('pronampe', gestaoNegocios.pronampe, name='pronampe'),
      path('relatorioVisitas', gestaoNegocios.relatorioVisitas, name='relatorioVisitas'),
      path('planoMetas', gestaoNegocios.planoMetas, name='planoMetas'),

      path('coopera', cooperar.coopera, name='coopera'),
      path('relacionamento', cooperar.relacionamento, name='relacionamento'),
      path('simulador', cooperar.simulador, name='simulador'),
      path('tabela', cooperar.tabela, name='tabela'),
      path('india', cooperar.india, name='india'),
      path('portifolio', cooperar.portifolio, name='portifolio'),
      path('capital', cooperar.capital, name='capital'),
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
      path('new_request_rh', rh.new_request_rh, name='new_request_rh'),
      path('salvar_malote_rh', rh.salvar_malote_rh, name='salvar_malote_rh'),

      path('ti', ti.ti_home, name='ti_home'),
      path('ti/new_request', ti.new_request, name='new_request'),
      path('ti/request_acessos_ti', ti.request_acessos_ti, name='request_acessos_ti'),
      path('ti/request_equipamentos_ti', ti.request_equipamentos_ti, name='request_equipamentos_ti'),
      path('ti/request_servicos_ti', ti.request_servicos_ti, name='request_servicos_ti'),
      path('ti/estoque', ti.estoque, name='estoque'),
      path('ti/solicit', ti.solicit, name='solicit'),
      path('ti/estoque/notebook', ti.notebook, name='notebook'),

      path('retaguarda_home', retaguarda.retaguarda_home, name='retaguarda_home'),
      path('new_request_retaguarda', retaguarda.new_request_retaguarda, name='new_request_retaguarda'),
      path('salvar_malote_retaguarda', retaguarda.salvar_malote_retaguarda, name='salvar_malote_retaguarda'),

      path('produtoServico_home', produtoServico.produtoServico_home, name='produtoServico_home'),
      path('request_produto_servico', produtoServico.request_produto_servico, name='request_produto_servico'),
      path('salvar_malote_PS', produtoServico.salvar_malote_PS, name='salvar_malote_PS'),

      path('financeiro_home', financeiro.financeiro_home, name='financeiro_home'),
      path('new_request_financeiro', financeiro.new_request_financeiro, name='new_request_financeiro'),
      path('salvar_malote_financeiro', financeiro.salvar_malote_financeiro, name='salvar_malote_financeiro'),

      path('cadastro_home', cadastro.cadastro_home, name='cadastro_home'),
      path('new_request_cadastro', cadastro.new_request_cadastro, name='new_request_cadastro'),
      path('salvar_malote_cadastro', cadastro.salvar_malote_cadastro, name='salvar_malote_cadastro'),

      path('adm_home', adm.adm_home, name='adm_home'),
      path('new_request_adm', adm.new_request_adm, name='new_request_adm'),
      path('salvar_malote_adm', adm.salvar_malote_adm, name='salvar_malote_adm'),

      path('cobranca_home', cobranca.cobranca_home, name='cobranca_home'),
      path('new_request_cobranca', cobranca.new_request_cobranca, name='new_request_cobranca'),
      path('salvar_malote_cobranca', cobranca.salvar_malote_cobranca, name='salvar_malote_cobranca'),

      path('secretaria_home', secretaria.secretaria_home, name='secretaria_home'),
      path('new_request_secretaria', secretaria.new_request_secretaria, name='new_request_secretaria'),
      path('salvar_malote_secretaria', secretaria.salvar_malote_secretaria, name='salvar_malote_secretaria'),

      path('credito_home', credito.credito_home, name='credito_home'),
      path('new_request_credito', credito.new_request_credito, name='new_request_credito'),
      path('salvar_malote_credito', credito.salvar_malote_credito, name='salvar_malote_credito'),



      path('dev', pages.dev, name='dev'),

      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
