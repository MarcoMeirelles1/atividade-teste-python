import pytest

@pytest.fixture
def listaS():
    return [1, 2, 3, 4, 5, 1]

def soma(listaS):
    return sum(listaS)

def multiplicacao(listaS):
    resultado = 1
    for numero in listaS:
        resultado *= numero
    return resultado

def test_soma(listaS):
    assert soma(listaS) == 16

def test_multiplicacao(listaS):
    assert multiplicacao(listaS) == 120

def index(listaS):
    return listaS[0], listaS[3]

def test_index(listaS):
    assert index(listaS) == (1, 4)

def soma_dobro(listaS):
    return sum(x * 2 for x in listaS)

def test_soma_dobro(listaS):
    assert soma_dobro(listaS) == 32
