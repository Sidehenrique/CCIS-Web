from ccis.models import dadosPessoais, dependentes, enderecoContato, profissional, dadosBancarios

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, \
    ModelFormMidia, modelFormEscolaridade, modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios


dados = dadosPessoais.objects()
profi = profissional.objects.select_related('dadosPessoais').all()
contatos = enderecoContato.objects.select_related('dadosPessoais').all()

print(dados, profi, contatos)

