import pytest
from src.edificio import Edificio


@pytest.fixture
def edificio_teste() -> Edificio:
    """Cria um edifício padrão para realizar os testes"""
    return Edificio(8, [30, 2, 0, 42, 10, 11, 11, 9])


def test_mudanca(edificio_teste: Edificio) -> None:
    """"Teste para verificar se a função mudança funciona para um andar não-extremo"""

    edificio_teste.mudanca(3, 5)
    assert edificio_teste.pessoas_por_andar == [30, 2, 5, 42, 10, 11, 11, 9]


def test_mudanca_primeiro_andar(edificio_teste: Edificio) -> None:
    """Teste para verificar se a função mudança funciona para o primeiro andar"""

    edificio_teste.mudanca(1, 100)
    assert edificio_teste.pessoas_por_andar == [100, 2, 0, 42, 10, 11, 11, 9]


def test_mudanca_ultimo_andar(edificio_teste: Edificio) -> None:
    """Teste para verificar se a função mudança funciona para o último andar"""

    edificio_teste.mudanca(8, 63)
    assert edificio_teste.pessoas_por_andar == [30, 2, 0, 42, 10, 11, 11, 63]


def test_censo(edificio_teste: Edificio) -> None:
    """Teste para verificar se a função censo funciona para um andar-limite não-extremo"""

    assert edificio_teste.censo(5) == 84


def test_censo_primeiro_andar(edificio_teste: Edificio) -> None:
    """Teste para verificar se a função censo funciona quando o andar-limite é o primeiro andar"""

    assert edificio_teste.censo(1) == 30


def test_censo_ultimo_andar(edificio_teste: Edificio) -> None:
    """Teste para verificar se a função censo funciona quando o andar-limite é o último andar"""

    assert edificio_teste.censo(8) == 115
