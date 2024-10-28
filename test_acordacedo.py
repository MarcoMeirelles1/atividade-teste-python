import pytest
from atv_acordacedo import acordar_cedo, tempo_exercicio, tem_exercicio 

def test_acordar_cedo():
    assert acordar_cedo(5) == 'Você é um guerreiro'
    assert acordar_cedo(7) == 'Tente novamente amanhã'

def test_tempo_exercicio():
    assert tempo_exercicio(70, 3) == 69
    assert tempo_exercicio(70, 1) == None  

def test_tem_exercicio():
    assert tem_exercicio('Corrida') == True
    assert tem_exercicio('Descanso') == False