from models.usuario_models import Usuario
from repositories.usuario_repositories import UsuarioRepository
import os


class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadatrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def excluir_usuario(self):
        try:
            email = input("Digite o e-mail do usuário: ")
            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if usuario_cadastrado:
                senha = input("Informe a senha do usuário para exclui-lo: ")

                if senha == usuario_cadastrado.senha:
                    self.repository.excluir_usuario(usuario_cadastrado)
                    print("Usuário excluido com suceso!")
                print("Usuário não encontrado!")
                return
            else:
                print("Usuário não cadastrado!")
                return
        
        except TypeError as erro:
            print(f"Erro ao excluir usuário: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
    
    def atualizar_usuario(self):
        try:
            print("\nAtualizando os dados de um usuário.")

            email_usuario = input("Informe o email do usuário: ")
            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email_usuario)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite seu nome: ")
                usuario_cadastrado.email = input("Digite o seu email: ")
                usuario_cadastrado.senha = input("Digite sua senha: ")
                print("Usuário atualizado com sucesso!.")
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao atualizar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def pesquisar_usuario_unico(self):
        try:
            email = input("\nDigite o email do usuário: ")
            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email)

            if usuario_cadastrado:
                os.system("cls || clear")
                print(" - Dados do usuário - ")
                print(f"Usuário: {usuario_cadastrado.nome} - {usuario_cadastrado.email} - {usuario_cadastrado.senha}")
                return
            else:
                print("Usuário não encontrado!")
                return
            
        except TypeError as erro:
            print(f"Erro ao procurar o usuário: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")