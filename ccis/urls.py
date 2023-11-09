from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (credito, controladoria, secretaria, cobranca, adm, cadastro, retaguarda, financeiro, gestaoNegocios,
                    gestaoNegocios, gestaoControle, formularios, security, rh, pages, cooperar, ti, produtoServico,
                    gestaoRisco, padigital, padf, planaltina, formosa, vicente, saojoao, saosebas, marketing, )

urlpatterns = [
    path('base', pages.base, name='base'),

    path('login', security.loginPage, name='login'),
    path('conta', pages.conta, name='conta'),
    path('profile/<int:user_id>', pages.profile, name='profile'),
    path('', pages.home, name='home'),
    path('departamentos', pages.departamentos, name='departamentos'),

    path('processos_user', pages.processos_user, name='processos_user'),
    path('card_detl/<int:card_id>', pages.card_detl, name='card_detl'),
    path('enviar_resposta/<int:card_id>', pages.enviar_resposta, name='enviar_resposta'),
    path('get_messages/<int:card_id>', pages.get_messages, name='get_messages'),
    path('registrar_atendimento/<int:card_id>', pages.registrar_atendimento, name='registrar_atendimento'),
    path('encaminhar_card/<int:card_id>', pages.encaminhar_card, name='encaminhar_card'),
    path('compartilhar_card/<int:card_id>', pages.compartilhar_card, name='compartilhar_card'),
    path('transferir_card/<int:card_id>', pages.transferir_card, name='transferir_card'),
    path('presonalizar_card/<int:card_id>', pages.presonalizar_card, name='presonalizar_card'),
    path('concluir_card/<int:card_id>', pages.concluir_card, name='concluir_card'),
    path('finalizar_card/<int:card_id>', pages.finalizar_card, name='finalizar_card'),
    path('get_user_rating/<int:card_id>', pages.get_user_rating, name='get_user_rating'),
    path('avaliar_card/<int:card_id>', pages.avaliar_card, name='avaliar_card'),
    path('reabrir_card/<int:card_id>', pages.reabrir_card, name='reabrir_card'),
    path('history_request', pages.history_request, name='history_request'),
    path('get_card_details', pages.get_card_details, name='get_card_details'),
    path('notificacao_lida/<int:notification_id>', pages.notificacao_lida, name='notificacao_lida'),

    path('utilitariosHome', pages.utilitariosHome, name='utilitarios'),
    path('utilitariosCopy', pages.utilitariosCopy, name='utilitariosCopy'),

    path('malotes', pages.malotes, name='malotes'),

    path('gestaoControle', gestaoControle.home, name='gestaoControle'),
    path('contabilidade', gestaoControle.contabilidade, name='contabilidade'),
    path('relatorios', gestaoControle.relatorios, name='relatorios'),
    path('estrategico', gestaoControle.estrategico, name='estrategico'),
    path('inadimplencia', gestaoControle.inadimplencia, name='inadimplencia'),
    path('qqs', gestaoControle.qqs, name='qqs'),
    path('pesquisa', gestaoControle.pesquisa, name='pesquisa'),

    path('gestaoNegocios', gestaoNegocios.home, name='gestaoNegocios'),
    path('gestaoMetas', gestaoNegocios.gestaoMetas, name='gestaoMetas'),
    path('diaria', gestaoNegocios.diaria, name='diaria'),
    path('listasPropensos', gestaoNegocios.listasPropensos, name='listasPropensos'),
    path('pronampe', gestaoNegocios.pronampe, name='pronampe'),
    path('relatorioVisitas', gestaoNegocios.relatorioVisitas, name='relatorioVisitas'),
    path('planoMetas', gestaoNegocios.planoMetas, name='planoMetas'),
    path('lastro', gestaoNegocios.lastro, name='lastro'),
    path('credito', gestaoNegocios.credito, name='credito'),

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
    path('processos_rh', rh.processos_rh, name='processos_rh'),

    path('ti', ti.ti_home, name='ti_home'),
    path('ti/new_request_ti', ti.new_request_ti, name='new_request_ti'),
    path('ti/request_acessos_ti', ti.request_acessos_ti, name='request_acessos_ti'),
    path('ti/request_equipamentos_ti', ti.request_equipamentos_ti, name='request_equipamentos_ti'),
    path('ti/request_servicos_ti', ti.request_servicos_ti, name='request_servicos_ti'),
    path('ti/estoque', ti.estoque, name='estoque'),
    path('ti/estoque/notebook', ti.notebook, name='notebook'),
    path('ti/processos_ti', ti.processos_ti, name='processos_ti'),

    path('retaguarda_home', retaguarda.retaguarda_home, name='retaguarda_home'),
    path('new_request_retaguarda', retaguarda.new_request_retaguarda, name='new_request_retaguarda'),
    path('salvar_malote_retaguarda', retaguarda.salvar_malote_retaguarda,
           name='salvar_malote_retaguarda'),
    path('processos_retaguarda', retaguarda.processos_retaguarda,name='processos_retaguarda'),

    path('produtoServico_home', produtoServico.produtoServico_home, name='produtoServico_home'),
    path('request_produto_servico', produtoServico.request_produto_servico,
           name='request_produto_servico'),
    path('salvar_malote_PS', produtoServico.salvar_malote_PS, name='salvar_malote_PS'),
    path('processos_PS', produtoServico.processos_PS, name='processos_PS'),

    path('financeiro_home', financeiro.financeiro_home, name='financeiro_home'),
    path('new_request_financeiro', financeiro.new_request_financeiro, name='new_request_financeiro'),
    path('salvar_malote_financeiro', financeiro.salvar_malote_financeiro,
           name='salvar_malote_financeiro'),
    path('processos_financeiro', financeiro.processos_financeiro, name='processos_financeiro'),

    path('cadastro_home', cadastro.cadastro_home, name='cadastro_home'),
    path('new_request_cadastro', cadastro.new_request_cadastro, name='new_request_cadastro'),
    path('salvar_malote_cadastro', cadastro.salvar_malote_cadastro, name='salvar_malote_cadastro'),
    path('processos_cadastro', cadastro.processos_cadastro, name='processos_cadastro'),


    path('adm_home', adm.adm_home, name='adm_home'),
    path('new_request_adm', adm.new_request_adm, name='new_request_adm'),
    path('salvar_malote_adm', adm.salvar_malote_adm, name='salvar_malote_adm'),
    path('processos_adm', adm.processos_adm, name='processos_adm'),


    path('cobranca_home', cobranca.cobranca_home, name='cobranca_home'),
    path('new_request_cobranca', cobranca.new_request_cobranca, name='new_request_cobranca'),
    path('salvar_malote_cobranca', cobranca.salvar_malote_cobranca, name='salvar_malote_cobranca'),
    path('processos_cobranca', cobranca.processos_cobranca, name='processos_cobranca'),

    path('secretaria_home', secretaria.secretaria_home, name='secretaria_home'),
    path('new_request_secretaria', secretaria.new_request_secretaria, name='new_request_secretaria'),
    path('salvar_malote_secretaria', secretaria.salvar_malote_secretaria,name='salvar_malote_secretaria'),
    path('processos_secretaria', secretaria.processos_secretaria,name='processos_secretaria'),

    path('credito_home', credito.credito_home, name='credito_home'),
    path('new_request_credito', credito.new_request_credito, name='new_request_credito'),
    path('salvar_malote_credito', credito.salvar_malote_credito, name='salvar_malote_credito'),
    path('processos_credito', credito.processos_credito, name='processos_credito'),

    path('controladoria_home', controladoria.controladoria_home, name='controladoria_home'),
    path('new_request_PC', controladoria.new_request_PC, name='new_request_PC'),
    path('processos_PC', controladoria.processos_PC, name='processos_PC'),
    path('request_acessos_PC', controladoria.request_acessos_PC, name='request_acessos_PC'),

    path('gestaoRisco_home', gestaoRisco.gestaoRisco_home, name='gestaoRisco_home'),
    path('request_acessos_risco', gestaoRisco.request_acessos_risco, name='request_acessos_risco'),
    path('new_request_risco', gestaoRisco.new_request_risco, name='new_request_risco'),
    path('processos_GR', gestaoRisco.processos_GR, name='processos_GR'),

    path('paDigital_home', padigital.paDigital_home, name='paDigital_home'),
    path('new_request_PaDigital', padigital.new_request_PaDigital, name='new_request_PaDigital'),
    path('request_acessos_PaDigital', padigital.request_acessos_PaDigital, name='request_acessos_PaDigital'),
    path('processos_PD', padigital.processos_PD, name='processos_PD'),

    path('padf_home', padf.padf_home, name='padf_home'),
    path('new_request_padf', padf.new_request_padf, name='new_request_padf'),
    path('salvar_malote_padf', padf.salvar_malote_padf, name='salvar_malote_padf'),
    path('processos_padf', padf.processos_padf, name='processos_padf'),

    path('planaltina_home', planaltina.planaltina_home, name='planaltina_home'),
    path('new_request_plan', planaltina.new_request_plan, name='new_request_plan'),
    path('processos_planaltina', planaltina.processos_planaltina, name='processos_planaltina'),
    path('salvar_malote_planaltina', planaltina.salvar_malote_planaltina, name='salvar_malote_planaltina'),

    path('formosa_home', formosa.formosa_home, name='formosa_home'),
    path('new_request_formosa', formosa.new_request_formosa, name='new_request_formosa'),
    path('salvar_malote_formosa', formosa.salvar_malote_formosa, name='salvar_malote_formosa'),
    path('processos_formosa', formosa.processos_formosa, name='processos_formosa'),

    path('vicente_home', vicente.vicente_home, name='vicente_home'),
    path('new_request_vicente', vicente.new_request_vicente, name='new_request_vicente'),
    path('salvar_malote_vicente', vicente.salvar_malote_vicente, name='salvar_malote_vicente'),
    path('processos_vicente', vicente.processos_vicente, name='processos_vicente'),

    path('SJ_home', saojoao.SJ_home, name='SJ_home'),
    path('new_request_SJ', saojoao.new_request_SJ, name='new_request_SJ'),
    path('salvar_malote_SJ', saojoao.salvar_malote_SJ, name='salvar_malote_SJ'),
    path('processos_SJ', saojoao.processos_SJ, name='processos_SJ'),

    path('saosebas_home', saosebas.saosebas_home, name='saosebas_home'),
    path('new_request_saosebas', saosebas.new_request_saosebas, name='new_request_saosebas'),
    path('salvar_malote_saosebas', saosebas.salvar_malote_saosebas, name='salvar_malote_saosebas'),
    path('processos_SB', saosebas.processos_SB, name='processos_SB'),

    path('marketing_home', marketing.marketing_home, name='marketing_home'),
    path('request_acessos_MK', marketing.request_acessos_MK, name='request_acessos_MK'),
    path('new_request_market', marketing.new_request_market, name='new_request_market'),
    path('processos_MK', marketing.processos_MK, name='processos_MK'),

    path('dev', pages.dev, name='dev'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
