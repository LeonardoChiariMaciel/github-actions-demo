"""Operações matemáticas básicas."""


def somar(a, b):
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a, b):
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


def dividir(a, b):
    """Retorna a divisão de a por b. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def fatorial(n):
    """Retorna o fatorial de n (n >= 0)."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("O fatorial só é definido para inteiros não negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def eh_primo(n):
    """Retorna True se n for um número primo."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def media(valores):
    """Retorna a média aritmética de uma lista de números."""
    if not valores:
        raise ValueError("A lista não pode ser vazia")
    return sum(valores) / len(valores)
