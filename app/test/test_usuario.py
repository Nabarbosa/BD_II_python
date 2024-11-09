import pytest
from app.models.usuario_models import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("Marta", "marta@gmail.com", "123")

def test_usuario_nome(usuario_valido):
    assert usuario_valido.nome == "Marta"

def test_usuario_nome(usuario_valido):
    assert usuario_valido.email == "marta@gmail.com"

def test_usuario_senha(usuario_valido):
    assert usuario_valido.senha == "123"

def test_nome_usuario_invalido(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado deve ser um texto."):
        Usuario(10, "marta@gmail.com", "123")

def test_nome_usuario_vazio(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado está vazio!"):
        Usuario(" ", "marta@gmail.com", "123") 

def test_email_usuario_invalido(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado deve ser um texto."):
        Usuario("Marta", 10, "123")

def test_email_usuario_vazio(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado está vazio!"):
        Usuario("Marta", "", "123") 

def test_senha_usuario_invalido(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado deve ser um texto."):
        Usuario("Marta", "marta@gmail.com", 123)

def test_senha_usuario_vazio(usuario_valido):
    with pytest.raises(TypeError, match="O que está sendo solicitado está vazio!"):
        Usuario("Marta", "marta@gmail.com", "") 

