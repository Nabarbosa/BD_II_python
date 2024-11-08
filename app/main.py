from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session
from models.usuario_models import Usuario
import os

def main():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)

        def listar_usuario():
            print("Listando todos usuários cadastrados")
            lista_usuarios = service.listar_todos_usuarios()
            for usuario in lista_usuarios:
                print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")
                

        while True:
            # os.system("cls || clear")
            print("\n=== SENAI SOLUTION ===")
            print("\nCódigo\t|\tFunção")
            print("  1\t|  Adicionar usuário")
            print("  2\t|  Pesquisar um usuário")
            print("  3\t|  Atualizar dados de um usuário")
            print("  4\t|  Excluir um usuário")
            print("  5\t|  Exibir todos os usuários cadastrados")
            print("  0\t|  Sair")

            opcao = int(input("\nEscolha uma opção: "))

            match(opcao):
                case 1:
                    os.system("cls || clear")
                    print("\nAdicionar usuário")
                    nome = input("Digite o nome do usuário: ")
                    email = input("Digite o email do usuário: ")
                    senha = input("Digite a senha do usuário: ")

                    service.criar_usuario(nome=nome, email=email, senha=senha)

                case 2:
                    os.system("cls || clear")
                    listar_usuario()
                    print("\nPesquisando usuário...")
                    service.pesquisar_usuario_unico()

                case 3:
                    os.system("cls || clear")
                    listar_usuario()
                    service.atualizar_usuario()

                case 4:
                    os.system("cls || clear")
                    listar_usuario()
                    print("\nExcluindo usuário...")
                    service.excluir_usuario()

                case 5:
                    os.system("cls || clear")
                    listar_usuario()

                case 0:
                    os.system("cls || clear")
                    print(f"Sair...")
                    break

                case _:
                    os.system("cls || clear")
                    print(f"Opção inválida - Tente novamente")


if __name__ == "__main__":
    os.system("cls || clear")
    main()
