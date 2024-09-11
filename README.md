# api_mathChalenge


A **Math Challenge API** é uma API simples que fornece operações matemáticas, como soma e média de uma lista de números inteiros.

## Endpoints

### 1. `/sum` (POST)
Calcula a soma de uma lista de números inteiros fornecidos no corpo da requisição.

- **URL**: `/sum`
- **Método**: `POST`
- **Parâmetros no Corpo**:  
  - `data`: Lista de números inteiros. Exemplo:
    ```json
    {
      "data": [1, 2, 3, 4]
    }
    ```

  - **Resposta de Sucesso** (`200 OK`):
    ```json
    {
      "sum": 10
    }
    ```
  - **Respostas de Erro** (`400 Bad Request`):
    - **Erro 1**: Quando o valor fornecido é apenas um valor inteiro fora de uma lista.
		```json
		[
		"Invalid value: input must be a list of integer values",
		"'int' object is not iterable"
		]
		```
    - **Erro 2**: Quando o valor fornecido é uma lista de números inteiros  com uma string ou char no meio, uma lista de strings ou char ou apenas uma string ou char.
		```json
		[
		"Invalid value: input must be a list of integer values",
		"unsupported operand type(s) for +: 'int' and 'str'"
		]
		```

### 2. `/average` (POST)
Calcula a média de uma lista de números inteiros fornecidos no corpo da requisição.

- **URL**: `/average`
- **Método**: `POST`
- **Parâmetros no Corpo**:  
  - `data`: Lista de números inteiros. Exemplo:
    ```json
    {
      "data": [1, 2, 3, 4]
    }
    ```

  - **Resposta de Sucesso** (`200 OK`):
    ```json
    {
      "average": 2.5
    }
    ```
  - **Resposta de Erro** (`400 Bad Request`):
    - **Erro 1**: Quando o valor fornecido é apenas um valor inteiro fora de uma lista.
		```json
		[
		"Invalid value: input must be a list of integer values",
		"'int' object is not iterable"
		]
		```
    - **Erro 2**: Quando o valor fornecido é uma lista de números inteiros  com uma string ou char no meio, uma lista de strings ou char ou apenas uma string ou char.
		```json
		[
		"Invalid value: input must be a list of integer values",
		"unsupported operand type(s) for +: 'int' and 'str'"
		]
		```
    - **Erro 3**: Quando o valor fornecido é uma lista vazia no endpoint.
		```json
		[
		"Invalid value: input must be a list of integer values",
		"division by zero"
		]

		```

---

## Executando a API

### 1. Clonando o Repositório

```bash
git clone https://github.com/aleffericlys/api_mathChalenge.git
cd api_mathChalenge
```
### 2. Dependencias
- Python 3.10: Limguagem de programação utilizada.
- Flask: Framework web para criar a API.
- Insomnia: Ferramenta para testar a API.
### 3. Instalando as Dependências

```bash
pip install -r requirements.txt
```
### 4. Executando a API

Execute o arquivo `main.py` para iniciar a API.
```bash
python api/main.py
```
A API estará rodando em: `http://localhost:3000`

## Testando a API com insominia
Aqui estão exemplos de como testar os endpoints usando o Insomnia:

### 1. `/sum`
- Metodo: POST
- URL: `http://localhost:3000/sum`
- Body:
  ```json
  {
	"data": [1, 2, 3, 4]
  }
  ```
- Response:
  ```json
  {
	"sum": 10
  }
  ```
### 2. `/average`
- Metodo: POST
- URL: `http://localhost:3000/average`
- Body:
  ```json
  {
	"data": [1, 2, 3, 4]
  }
  ```
- Response:
  ```json
  {
  	"average": 2.5
  }
  ``` 


## Descrição de estrutura de pastas
a estrutura das pastas está organizada da seguinte maneira:

```bash
/api_mathChalenge
│
├── /api        # Pasta da biblioteca de funções
│   ├── /src        # Pasta da biblioteca de funções
│   │   └── library.py      # Biblioteca com as funções de soma e média
│   │   
│   ├── /tests   # Pasta de testes unitários
│   │   └── test_library.py # Testes unitários
│   │   
│   └── main.py       # Arquivo principal da API
├── requirements.txt    # Arquivo de dependências
├── .gitignore       # Arquivo de configuração do git
└── README.MD        # Documentação da API

```
- `api_mathChalenge`: pasta raiz.
  - Nessa pasta estão os arquivos de `.gitignore`, `README.md` e o `requirements.txt`.
- `api_mathChalenge/api`: pasta onde está o código da aplicação.
  - Nessa pasta se encontra o `main.py` que é o arquivo principal da aplicação definindo as rotas da api e as pastas `src` e `tests`.
- `api_mathChalenge/api/src`: pasta onde está a biblioteca de funções.
  - Nessa pasta se encontra o `library.py` que é o arquivo com as funções que serão utilizadas na aplicação.
-  `api_mathChalenge/api/tests`: pasta onde estão os testes unitários.
   - Nessa pasta se encontra o `test_library.py` que é o arquivo com os testes unitários das classes biblioteca.

## Descrição de funcionamento de funções da biblioteca
A biblioteca é composta por 2 classes e 4 funções, sendo elas:
- `class Numbers` com as sguintes funções:
  - `def sum(numbers: list[int]) -> int:` 
    - Função que recebe uma lista de números inteiros e retorna a soma de todos os números da lista com o auxílio da função `def sum(a: int, b : int) -> int:` de `class Number`.
  - `def average(numbres: list[int]) -> float:`
    - Função que recebe uma lista de números inteiros e retorna a média de todos os números da lista com o auxílio da função `def sum(numbers: list[int]) -> int:` de `class Numbers` e `def divide(a: int, b : int) -> float:` de `class Number`.
- `class Number` com as sguintes funções: 
  - `def sum(a: int, b : int) -> int:`
    - Função que recebe dois números inteiros e retorna a soma deles.
  - `def divide(a: int, b : int) -> float:`
    - Função que recebe dois números inteiros e retorna a divisão deles.
  

