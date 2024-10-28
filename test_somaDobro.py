import pytest

@pytest.fixture
def listaDobro():
    return [1, 2, 3, 4, 5, 1]

def soma_dobro(listaDobro):
    return sum(x * 2 for x in listaDobro)

def test_soma_dobro(listaDobro):
    resultado = soma_dobro(listaDobro)
    assert soma_dobro(listaDobro) == 32