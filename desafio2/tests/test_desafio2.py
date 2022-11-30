from src.edificio import Edificio


def test_mudanca():
    """"Teste para verificar se a função mudança funciona para um andar não-extremo"""

    predio_teste1 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    predio_teste1.mudanca(3, 5)
    assert predio_teste1.pessoas_por_andar == [30, 2, 5, 42, 10, 11, 11, 9]


def test_mudanca_primeiro_andar():
    """Teste para verificar se a função mudança funciona para o primeiro andar"""

    predio_teste2 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    predio_teste2.mudanca(1, 100)
    assert predio_teste2.pessoas_por_andar == [100, 2, 0, 42, 10, 11, 11, 9]


def test_mudanca_ultimo_andar():
    """Teste para verificar se a função mudança funciona para o último andar"""

    predio_teste3 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    predio_teste3.mudanca(8, 63)
    assert predio_teste3.pessoas_por_andar == [30, 2, 0, 42, 10, 11, 11, 63]


def test_censo():
    """Teste para verificar se a função censo funciona para um andar-limite não-extremo"""
    predio_teste4 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    assert predio_teste4.censo(5) == 84


def test_censo_primeiro_andar():
    """Teste para verificar se a função censo funciona quando o andar-limite é o primeiro andar"""
    predio_teste5 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    assert predio_teste5.censo(1) == 30


def test_censo_ultimo_andar():
    """Teste para verificar se a função censo funciona quando o andar-limite é o último andar"""

    predio_teste6 = Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])
    assert predio_teste6.censo(8) == 115
