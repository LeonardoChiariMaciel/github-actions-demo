# GitHub Actions Demo

![CI](../../actions/workflows/ci.yml/badge.svg)

Pequena biblioteca em Python (`calculadora`) com testes de unidade em `pytest`,
executados automaticamente pelo GitHub Actions a cada commit.

## Matriz de testes

| Sistema operacional | Python 3.11 | Python 3.12 | Python 3.13 |
|---------------------|:-----------:|:-----------:|:-----------:|
| Ubuntu              | ✔           | ✔           | ✔           |
| macOS               | ✔           | ✔           | ✔           |
| Windows             | ✔           | ✔           | ✔           |

## Rodar localmente

```bash
pip install -r requirements.txt
python -m pytest -v
```
