from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import Session
from sqlalchemy.orm import Session
from models.usuario_models import Usuario


def main():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)
        while True:


            print("\n=== SENAI SOLUTION ===")
            print("Código  |   Função")
            print("1 - Adicionar usuário")
            print("2 - Pesquisar um usuário")
            print("3 - Atualizar dados de um usuário")
            print("4 - Excluir um usuário")
            print("5 - Exibir todos os usuários cadastrados")
            print("0 - Sair")
            opcao = int(input("\nEscolha uma opção: "))

            match (opcao):
                case 1:
                    print("\nAdicionar usuário")
                    nome = input("Digite o nome do usuário: ")
                    email = input("Digite o email do usuário: ")
                    senha = input("Digite a senha do usuário: ")

                    service.criar_usuario(nome=nome, email=email, senha=senha)

                case 2:
                    print("\nPesquisar dados de apenas um usuário")
                    email = input("Digite o email do usuário que será consultado: ")

                    usuario = session.query(Usuario).filter_by(email = email).first()

                    if usuario:
                        print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")
                    else:
                        print(f"Usuário não existe")

                case 3:
                    print("\nAtualizar dados de um usuário")
                    email = input("Digite o email do usuário que deseja atualizar: ")

                    usuario = session.query(Usuario).filter_by(email=email).first()

                    if usuario:
                        usuario.nome = input("Digite seu nome: ")
                        usuario.email = input("Digite seu e-mail: ")
                        usuario.senha = input("Digite sua senha: ")

                    else:
                        print("Usuário não encontrado. ")

                case 4:
                    print("\nExcluindo os dados de um usuário.")
                    email = input("Digite o e-mail do usuário que será excluido: ")

                    usuario = session.query(Usuario).filter_by(email=email).first()

                    if usuario:
                        session.delete(usuario)
                        session.commit()
                        print(f"Usuário {usuario.nome} excluido com sucesso!")
                    else:
                        print("Usuário não encontrado.")

                case 5:
                    print("Exibir todos od usuários cadatrados")
                    lista_usuarios = service.listar_todos_usuarios()
                    for usuario in lista_usuarios:
                        print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

                case 0:
                    print("Sair")

                case _:
                    print(f"Opção inválida - Tente novamente")


            if __name__ == "__main__":
                main()
