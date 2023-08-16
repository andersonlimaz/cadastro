from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        # Depois de salvar o novo usuário, redirecione para a página de listagem de usuários
        return redirect('listar_usuarios')  # 'listar_usuarios' é o nome da URL

    # Se o método não for POST, apenas exiba a página de listagem de usuários
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
