# api_mathChalenge

Esta aplicação é uma api que realiza operações matemáticas simples sendo elas soma e média de números inteiros de uma lista.

A unica biblioteca usada de terceiros foi a `flask` que é uma biblioteca para criação de apis com python.

### requerimentos:
- python 3.8+
- flask

## Descrição de estrutura de pastas
a estrutura das pastas está organizada da seguinte maneira:
- api_mathChalenge: pasta raiz.
  - Nessa pasta estão os arquivos de `.gitignore` e o `README.md`.
- api_mathChalenge/api: pasta onde está o código da aplicação.
  - Nessa pasta se encontra o `main.py` que é o arquivo principal da aplicação definindo as rotas da api.
- api_mathChalenge/api/src: pasta onde está a biblioteca de funções.
  - Nessa pasta se encontra o `library.py` que é o arquivo com as funções que serão utilizadas na aplicação.

## Descrição de funcionamento de funções da biblioteca

- `def sumNumbrs(numbers: list[int]) -> int:` 
  - Função que recebe uma lista de números inteiros e retorna a soma de todos os números da lista com o auxílio da função `def sum(a: int, b : int) -> int:`.
- `def sum(a: int, b : int) -> int:`
  - Função que recebe dois números inteiros e retorna a soma deles.
- `def average(numbres: list[int]) -> float:`
  - Função que recebe uma lista de números inteiros e retorna a média de todos os números da lista com o auxílio da função `def sumNumbrs(numbers: list[int]) -> int:` e `def divide(a: int, b : int) -> float:`.
- `def divide(a: int, b : int) -> float:`
  - Função que recebe dois números inteiros e retorna a divisão deles.