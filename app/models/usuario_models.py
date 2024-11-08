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
            raise TypeError("O nome deve ser um texto")
        
    def _verificar_nome_vazio(self, valor):
        try:
            self._verifcar_nome_invalido(valor)
            self._verificar_nome_vazio(valor)
        except TypeError as erro:
            print(f"Erro: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
        self.nome = valor
        return self.nome

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
