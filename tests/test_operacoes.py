import pytest

from calculadora import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    fatorial,
    eh_primo,
    media,
)


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 2) == 3.5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)


def test_fatorial():
    assert fatorial(0) == 1
    assert fatorial(5) == 120


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-3)


@pytest.mark.parametrize("n, esperado", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (25, False),
])
def test_eh_primo(n, esperado):
    assert eh_primo(n) is esperado


def test_media():
    assert media([1, 2, 3, 4]) == 2.5


def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])
