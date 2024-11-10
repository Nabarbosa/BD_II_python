from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from ..config.database import db

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
    
        self.nome = self.__verificar_nome_usuario(nome)
        self.email = self.__verificar_email_usuario(email)
        self.senha = self.__verificar_senha_usuario(senha)
 
 
    def __verificar_nome_usuario(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O que está sendo solicitado deve ser um texto!")
        
        if not nome.strip():
            raise ValueError("O que está sendo solicitado está vazio!")
        
        return nome
        

    def __verificar_email_usuario(self, email):
        if not isinstance(email, str):
            raise TypeError("O que está sendo solicitado deve ser um texto!")
        
        if not email.strip():
            raise ValueError("O que está sendo solicitado está vazio!")
        
        return email
        

    def __verificar_senha_usuario(self, senha):
        if not isinstance(senha, str):
            raise TypeError("O que está sendo solicitado deve ser um texto!")
        
        if not senha.strip():
            raise ValueError("O que está sendo solicitado está vazio!")
        
        return senha


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
