# Heart Disease Prediction Front-End

Este projeto é um front-end desenvolvido em **Streamlit** para interagir com uma API de predição de doenças cardíacas. O sistema permite cadastrar novos pacientes, listar pacientes cadastrados e deletar registros existentes, além de exibir os resultados da predição de doenças cardíacas em português.

## Funcionalidades

- **Cadastrar Paciente**: Formulário para inserir os dados de um novo paciente e realizar a predição de doenças cardíacas através da API.
- **Listar Pacientes**: Exibe a lista de pacientes cadastrados, incluindo idade, sexo, pressão arterial, colesterol, tipo de dor no peito, depressão do segmento ST e diagnóstico da presença ou ausência de doença cardíaca.
- **Deletar Paciente**: Permite a remoção de um paciente a partir de seu nome.

## Tecnologias Utilizadas

- **Streamlit**: Framework usado para construir a interface web do front-end.
- **Requests**: Biblioteca usada para fazer requisições HTTP à API.

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior.
- pip (gerenciador de pacotes do Python).
- A API de predição de doenças cardíacas deve estar em execução localmente ou acessível via URL.

### Passos para Instalação

1. Clone o repositório:

git clone https://github.com/usuario/seu-repositorio-front.git

2. Acesse o diretório do projeto:

cd seu-repositorio-front

3. Instale as dependências listadas no `requirements.txt`:

pip install -r requirements.txt

4. Modifique a URL base da API no arquivo `app.py` se necessário:

BASE_URL = 'http://127.0.0.1:5000'

5. Execute a aplicação Streamlit:

streamlit run app.py

6. Acesse a aplicação em seu navegador:

http://localhost:8501

## Como Usar

### Cadastrar Paciente

1. Escolha a opção **Cadastrar Paciente** no menu lateral.
2. Preencha os dados do paciente, como nome, idade, sexo, pressão arterial, colesterol, tipo de dor no peito e depressão do segmento ST.
3. Clique em **Cadastrar**.
4. O resultado da predição será exibido diretamente na página, indicando se há **presença** ou **ausência** de doença cardíaca.

### Listar Pacientes

1. Escolha a opção **Listar Pacientes** no menu lateral.
2. A lista de pacientes cadastrados será exibida com todas as informações relevantes e o diagnóstico de doenças cardíacas.

### Deletar Paciente

1. Escolha a opção **Deletar Paciente** no menu lateral.
2. Insira o nome do paciente a ser removido e clique em **Deletar**.
3. Se o paciente for encontrado e removido, uma mensagem de sucesso será exibida.

## Estrutura do Projeto

```bash
.
├── app.py                      # Arquivo principal da aplicação Streamlit
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação do projeto
└── ...
```

## Dependências

- **Streamlit**: Para construir a interface do front-end.
- **Requests**: Para realizar chamadas HTTP à API.