from django.shortcuts import render, redirect,get_object_or_404 # 1. Importe o 'redirect'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm # 2. Importe nosso novo 'TarefaForm'

@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            #
            # MUDANÇA 1: Salvando com o usuário
            #
            # 'commit=False' cría o objeto na memória, mas não salva no banco.
            tarefa = form.save(commit=False)
            # Atribui o usuário logado (request.user) ao campo 'user' da tarefa
            tarefa.user = request.user
            # Agora sim, salva o objeto completo no banco
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()

    #
    # MUDANÇA 2: Filtrando a lista de tarefas
    #
    # Antes: Tarefa.objects.all()
    # Agora: Filtre apenas onde o campo 'user' é igual ao 'request.user'
    todas_as_tarefas = Tarefa.objects.filter(user=request.user).order_by('-criada_em')

    context = {
    'nome_usuario': request.user.username, # Use o nome do usuário logado!
    'tecnologias': ['Autenticação', 'ForeignKey', 'Login'],
    'tarefas': todas_as_tarefas,
    'form': form,
    }
    return render(request, 'home.html', context)

@login_required
def concluir_tarefa(request, pk):
    # 2. Modifique o 'get_object_or_404'
    # Busque a Tarefa pela 'pk' E ONDE o 'user' é o 'request.user'
    tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save() # Não se esqueça de salvar!
    return redirect('home')

@login_required
def deletar_tarefa(request, pk):
 # 3. Faça o mesmo filtro de segurança aqui
 tarefa = get_object_or_404(Tarefa, pk=pk, user=request.user)
 if request.method == 'POST':
    tarefa.delete()
    return redirect('home')
    
def register(request):
    # Se a requisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
        # Verifica se o formulário é válido (ex: senhas batem, username não existe)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco
            login(request, user) # Faz o login automático do usuário
            return redirect('home') # Redireciona para a home
    # Se a requisição for GET, o usuário apenas visitou a página
    else:
        form = UserCreationForm() # Cria um formulário de cadastro vazio

    # Prepara o contexto e renderiza o template
        context = {'form': form}
        return render(request, 'register.html', context)