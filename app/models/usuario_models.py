from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()


class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # Definindo características dac lasse.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


    def _verifcar_nome_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O que está sendo solicitado, deve ser um texto.")

    def _verificar_nome_vazio(self, nome):
        if not nome.strip():
            raise ValueError("O que está sendo solicitado, está vazio!")
    
    def _verificar_nome_vazio(self, valor):
        # try:
            self._verifcar_nome_invalido(valor)
            self._verificar_nome_vazio(valor)
        # except TypeError as erro:
        #     print(f"Erro: {erro}")
        # except Exception as erro:
        #     print(f"Erro inesperado: {erro}")
            self.nome = valor
            return self.nome

    def _verificar_email_usuario(self, email):
        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)

        self.email = email
        return self.email 
    
    def _verificar_senha_usuario(self, senha):
        self._verificar_senha_invalida(senha)
        self._verificar_senha_vazio(senha)

        self.senha = senha
        return self.senha
    
    def _verificar_email_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("O que está sendo solicitado está inválido!")
        
    def _verificar_email_vazio(self, email):
        if not email.strip():
            raise TypeError("O que está sendo solicitado está vazio!")

    def _verificar_senha_invalida(self, senha):
        if not isinstance(senha, str):
            raise TypeError("O que está sendo solicitado está inválido!")
        
    def _verificar_senha_vazio(self, senha):
        if not senha.strip():
            raise TypeError("O que está sendo solicitado  está vazio")

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
