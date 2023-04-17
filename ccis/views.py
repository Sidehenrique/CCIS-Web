from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import modelFormDadosPessoais, modelFormDependentes, modelFormEnderecoContato, ModelFormOutros, ModelFormMidia
from .forms import modelFormEscolaridade , modelFormCertificacao, modelFormProfissional, modelFormDadosBancarios




def loginPage(request):
   return render(request, 'ccis/login.html')

def conta(request):
   mensagem = "Por favor preencha todos os campos obrigatórios"
   button = 'Voltar'

   context = {
      'mensagem': mensagem,
      'bttn': button,
   }

   return render(request, 'ccis/conta.html', context)

def usuario(request):
   return render(request, 'ccis/usuario.html')

def solicitacao(request):
   return render(request, 'ccis/solicitacao.html')

def profile(request):
   return render(request, 'ccis/profile.html')

def base(request):
   return render(request, 'ccis/base.html')

def formLogin(request):
   if request.method == 'POST':
      username = request.POST.get('login')
      password = request.POST.get('senha')

      statusName = 'is-valid'
      statusSenha = 'is-valid'

      user = authenticate(request, username=username, password=password)

      if user is not None:
         login(request, user)
         return redirect('conta')

      else:

         statusName = 'is-invalid'
         statusSenha = 'is-invalid'

         context = {
            'username': username,
            'password': password,
            'statusName': statusName,
            'statusSenha': statusSenha

         }
         messages.add_message(request=request, message='Usuario ou senha incorretos', level=messages.ERROR)
         return render(request, 'ccis/login.html', context)
   return render(request, 'ccis/login.html')


def dev(request):

   form = modelFormDadosBancarios(),modelFormDadosPessoais()

   if request.method == 'POST':

      form = modelFormDadosPessoais(request.POST, request.FILES)
      form = modelFormDadosBancarios(request.POST, request.FILES)

      if form.is_valid():
         form.save()
         return HttpResponse("Salvo com sucesso")

      else:
         return HttpResponse("não passou")

   elif request.method == 'GET':
      return render(request, 'ccis/dev.html', {'form': form})
  
def conta2(request):

   dadosPessoais = modelFormDadosPessoais()
   dependentes = modelFormDependentes()
   contatoEndereco = modelFormEnderecoContato()
   escolaridade = modelFormEscolaridade()
   certificacao = modelFormCertificacao()
   profissional = modelFormProfissional()
   dadosBancarios = modelFormDadosBancarios()
   outros = ModelFormOutros()
   midia = ModelFormMidia()

   return render(request, 'ccis/conta2.html', {'form': dadosPessoais,
                                               'dependentes':dependentes,
                                               'contatoEndereco':contatoEndereco,
                                               'escolaridade':escolaridade,
                                               'certificacao':certificacao,
                                               'profissional':profissional,
                                               'dadosBancarios':dadosBancarios,
                                               'outros':outros,
                                               'midia':midia,})




# def formDadosPessoais(request):
#    form = Dadospessoais()
#
#    if request.method == 'POST':
#
#       nome = request.POST.get('nome')
#       sexo = request.POST.get('sexo')
#       civil = request.POST.get('civil')
#       cor = request.POST.get('cor')
#       nascimento = request.POST.get('nascimento')
#       naturalidade = request.POST.get('naturalidade')
#       sanguineo = request.POST.get('sanguineo')
#       nomePai = request.POST.get('nomePai')
#       nomeMae = request.POST.get('nomeMae')
#       cpf = request.POST.get('cpf')
#       rg = request.POST.get('rg')
#       expedidor = request.POST.get('expedidor')
#       cnh = request.POST.get('cnh')
#       validade = request.POST.get('validade')
#       categoria = request.POST.get('categoria')
#       titulo = request.POST.get('titulo')
#       zona = request.POST.get('zona')
#       secao = request.POST.get('secao')
#       ctps = request.POST.get('ctps')
#       serie = request.POST.get('serie')
#       data = request.POST.get('data')
#       reservista = request.POST.get('reservista')
#       ra = request.POST.get('ra') # < -------- campo faltando RA da reservista
#       serieReservista = request.POST.get('serieReservista')
#       pis = request.POST.get('pis')
#       cns = request.POST.get('cns')
#       pcd = request.POST.get('pcd')
#
#       # context = {
#       #    'nome': nome,
#       #    'sexo': sexo,
#       #    'civil': civil,
#       #    'cor': cor,
#       #    'nascimento': nascimento,
#       #    'naturalidade': naturalidade,
#       #    'sanguineo': sanguineo,
#       #    'nomePai': nomePai,
#       #    'nomeMae': nomeMae,
#       #    'cpf': cpf,
#       #    'rg': rg,
#       #    'expedidor': expedidor,
#       #    'cnh': cnh,
#       #    'validade': validade,
#       #    'categoria': categoria,
#       #    'titulo': titulo,
#       #    'zona': zona,
#       #    'secao': secao,
#       #    'ctps': ctps,
#       #    'serie': serie,
#       #    'data': data,
#       #    'reservista': reservista,
#       #    'ra': ra,
#       #    'serieReservista': serieReservista,
#       #    'pis': pis,
#       #    'cns': cns,
#       #    'pcd': pcd,
#       #
#       # }
#
#       mensagem = 'Dados Cadastrados com Sucesso!'
#       button = 'Voltar'
#
#       context = {
#          'show_modal': True,
#          'mensagem': mensagem,
#          'bttn': button,
#       }
#
#       db = Dadospessoais(nomecompleto=nome, cpf=cpf, rg=rg, expedidor=expedidor, sexo=sexo, datanascimento=nascimento,
#                         estadocivil=civil, nomepai=nomePai, nomemae=nomeMae, ctps=ctps, datactps=data, seriectps=serie,
#                         corraca=cor, tiposanguineo=sanguineo, naturalidade=naturalidade, cnh=cnh, categoria=categoria,
#                         validadecnh=validade, titulodeeleitor=titulo, zona=zona, secao=secao, pis=pis, reservista=reservista,
#                         seriereservista=serieReservista, carteiranacionaldesaude=cns, pessoacomdeficiencia=pcd)
#       db.save()
#
#       return render(request, 'ccis/conta.html', context)
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formDependentes(request):
#    form = Dependentes()
#
#    if request.method == 'POST':
#       nome = request.POST.get('depNome')
#       cpf = request.POST.get('depCPF')
#       nascimento = request.POST.get('depNascimento')
#       relacao = request.POST.get('depRelacao')
#       email = request.POST.get('depEmail')
#       contato = request.POST.get('depContato')
#
#       db = Dependentes(nomecompleto=nome, relacao=relacao, datanascimento=nascimento,
#                        cpf=cpf, contato=contato, email=email)
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formEnd(request):
#    form = Enderecoecontato()
#
#    if request.method == 'POST':
#       endereco = request.POST.get('eEndereco')
#       bairro = request.POST.get('eBairro')
#       cidade = request.POST.get('eCidade')
#       cep = request.POST.get('eCEP')
#       estado = request.POST.get('eEstado')
#       ramal = request.POST.get('eRamal')
#
#       emailCorp = request.POST.get('eEmailCorp')
#       telCorp = request.POST.get('eTelCorp')
#       celCorp = request.POST.get('eCelCorp')
#       emailP = request.POST.get('eEmailP')
#       telP = request.POST.get('eTelP')
#       celP = request.POST.get('eCelP')
#
#       nome = request.POST.get('emNome') #<------------------ Campo faltando
#       contato = request.POST.get('emContato')
#       relacao = request.POST.get('emRelacao')
#
#       db = Enderecoecontato(endereco=endereco, bairro=bairro, cidade=cidade, estado=estado, cep=cep, emailcorporativo=emailCorp,
#                             telefonepessoal=telP, telefonecorporativo=telCorp, celularcorporativo=celCorp, celularpessoal=celP,
#                             ramal=ramal, emailpessoal=emailP, contatodeemergencia=contato, relacao=relacao)
#
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formEscolaridade(request):
#    form = Escolaridade()
#
#    if request.method == 'POST':
#       entidade = request.POST.get('esEntidade')
#       aria = request.POST.get('esAria')
#       grau = request.POST.get('esGrau')
#       inicio = request.POST.get('esInicio') #< ----------campo faltando
#       conclusao = request.POST.get('esConclusão')
#       lingua = request.POST.get('esLingua')
#       nivel = request.POST.get('esNivel')
#
#       db = Escolaridade(escolaridade=grau, entidadedeensino=entidade, areadeensino=aria, dataconclusao=conclusao,
#                         idiomaprimario=lingua, nivelprimario=nivel)
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formCertif(request):
#    form = Certificacao()
#
#    if request.method == 'POST':
#       nome = request.POST.get('cNome')
#       org = request.POST.get('cOrg')# <----------------campos faltando
#       dataEm = request.POST.get('cDataEm')# <----------------campos faltando
#       dataEx = request.POST.get('cDataEx')
#
#       db = Certificacao(certificacao=nome, dataconclusao=dataEx)
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formProficional(request):
#    form = Profissional()
#
#    if request.method == 'POST':
#       cargo = request.POST.get('proCargo')
#       area = request.POST.get('proArea')
#       paUnidade = request.POST.get('proPaUnidade')
#       colaborador = request.POST.get('proColaborador')
#       custo = request.POST.get('proCusto')
#       matricula = request.POST.get('proMatricula')
#       empregador = request.POST.get('proEmpregador')
#       superior = request.POST.get('proSuperior')
#       pagamento = request.POST.get('proFolha')
#       admissao = request.POST.get('proAdm')
#       desligamento = request.POST.get('proDes')
#       situacao = request.POST.get('proSituacao')
#       entrada = request.POST.get('proEntrada')
#       saida = request.POST.get('proSaida')
#
#       db = Profissional(cargo=cargo, area=area, paunidade=paUnidade, colaborador=colaborador, centrodecusto=custo,
#                         matricula=matricula, empregador=empregador, superiorimediato=superior, folhadepagamento=pagamento,
#                         admissao=admissao, desligamento=desligamento, situacao=situacao, horarioentrada=entrada,
#                         horariosaida=saida)
#
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formDadosBancarios(request):
#    form = Dadosbancarios()
#
#    if request.method == 'POST':
#       conta = request.POST.get('Dconta')
#       digito = request.POST.get('Ddigito')
#       banco = request.POST.get('Dbanco')
#       agencia = request.POST.get('Dagencia')
#       tipoConta = request.POST.get('Dtipoconta')
#       modalidade = request.POST.get('Dmodalidade')
#       pix = request.POST.get('Dpix')
#
#       db = Dadosbancarios(banco=banco, tipodeconta=tipoConta, modalidade=modalidade, agencia=agencia, conta=conta,
#                           digitodaconta=digito, chavepix=pix)
#
#       db.save()
#       return render(request, 'ccis/conta.html')
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formMidia(request):
#       form = Dadospessoais()
#
#       if request.method == 'POST':
#          foto = request.POST.get('foto')
#          background = request.POST.get('background')
#
#          print(foto, background)
#
#          db = Dadospessoais(avatar=foto, canvas=background,)
#          db.save()
#
#          return render(request, 'ccis/conta.html')
#
#       elif request.method == 'GET':
#          return render(request, 'ccis/conta.html', {'form': form})
#
#
# def formOutros(request):
#    form = Outros()
#
#    if request.method == 'POST':
#       camiseta = request.POST.get('Ocamiseta')
#
#       db = Outros(camiseta=camiseta)
#       db.save()
#
#       return render(request, 'ccis/conta.html')
#
#    elif request.method == 'GET':
#       return render(request, 'ccis/conta.html', {'form': form})



