import streamlit as st
import requests

# Definindo a URL base da API
BASE_URL = 'http://127.0.0.1:5000'

# Função para traduzir o resultado da predição
def traduzir_diagnostico(diagnostico):
    if diagnostico == "Presence":
        return "Presença de doença cardíaca"
    elif diagnostico == "Absence":
        return "Ausência de doença cardíaca"
    return "Diagnóstico desconhecido"

# Função para chamar a API e cadastrar um novo paciente
def cadastrar_paciente():
    # Criar formulário para entrada de dados do paciente
    st.title('Cadastro de Paciente')
    
    with st.form(key='form_paciente', clear_on_submit=True):
        name = st.text_input('Nome do Paciente').strip()  # strip() para remover espaços extras
        age = st.number_input('Idade', min_value=0, max_value=120, step=1)
        sex = st.selectbox('Sexo', options=['M', 'F'])
        BP = st.number_input('Pressão Arterial', min_value=40, max_value=400, step=1)
        cholesterol = st.number_input('Colesterol', min_value=20, max_value=600, step=1)
        chest_pain_type = st.selectbox('Tipo de Dor no Peito', options=['1 - Sem dor', '2 - Pouca dor', '3 - Dor moderada', '4 - Muita dor'])
        ST_depression = st.number_input('Depressão do Segmento ST', min_value=0.0, max_value=10.0, step=0.1)
        submit_button = st.form_submit_button('Cadastrar')

    # Se o formulário foi enviado, realizar a requisição à API
    if submit_button:
        # Converter o sexo para True (M) ou False (F)
        sex = 'true' if sex == 'M' else 'false'

        # Montar os dados como um dicionário de dados para formulário
        paciente_data = {
            'name': name,
            'age': str(age),  # Converter os valores numéricos para string
            'sex': sex,
            'BP': str(BP),
            'cholesterol': str(cholesterol),
            'chest_pain_type': chest_pain_type.split()[0],  # Captura apenas o número do tipo de dor
            'ST_depression': str(ST_depression)
        }

        # Enviar os dados como formulário
        response = requests.post(f'{BASE_URL}/paciente', data=paciente_data)

        if response.status_code == 200:
            paciente_cadastrado = response.json()
            diagnostico = paciente_cadastrado['heart_disease']

            # Traduzir o diagnóstico para português
            diagnostico_traduzido = traduzir_diagnostico(diagnostico)
            
            st.success(f"Paciente {name} cadastrado(a) com sucesso!")
            st.write(f"Diagnóstico do paciente: **{diagnostico_traduzido}**")
        elif response.status_code == 409:
            st.error("Paciente já existente na base.")
        else:
            st.error("Erro ao cadastrar o paciente.")


# Função para traduzir os dados do paciente
def traduzir_pacientes(pacientes):
    pacientes_traduzidos = []
    
    for paciente in pacientes:
        # Traduzir os dados na ordem especificada
        paciente_traduzido = {
            "Nome do Paciente": paciente['name'],
            "Idade": paciente['age'],
            "Sexo": "M" if paciente['sex'] else "F",  # Apresentar M ou F para o sexo
            "Pressão Arterial": paciente['BP'],
            "Colesterol": paciente['cholesterol'],
            "Tipo de Dor no Peito": paciente['chest_pain_type'],
            "Depressão do Segmento ST": paciente['ST_depression'],
            "Diagnóstico": "Presença de doença cardíaca" if paciente['heart_disease'] == "Presence" else "Ausência de doença cardíaca"
        }
        pacientes_traduzidos.append(paciente_traduzido)
    return pacientes_traduzidos

# Função para carregar pacientes da API
def carregar_pacientes():
    response = requests.get(f'{BASE_URL}/pacientes')
    if response.status_code == 200:
        return response.json().get('pacientes', [])
    else:
        return []

# Função para listar os pacientes cadastrados
def listar_pacientes():
    st.title('Pacientes Cadastrados')

    # Atualizar a lista de pacientes ao entrar na aba
    st.session_state['pacientes_data'] = carregar_pacientes()

    pacientes_data = st.session_state['pacientes_data']

    if pacientes_data:
        for paciente in pacientes_data:
            st.write(f"**Nome:** {paciente['name']}")
            st.write(f"**Idade:** {paciente['age']}")
            st.write(f"**Sexo:** {'M' if paciente['sex'] else 'F'}")
            st.write(f"**Pressão Arterial:** {paciente['BP']}")
            st.write(f"**Colesterol:** {paciente['cholesterol']}")
            st.write(f"**Tipo de Dor no Peito:** {paciente['chest_pain_type']}")
            st.write(f"**Depressão do Segmento ST:** {paciente['ST_depression']}")
            st.write(f"**Diagnóstico:** {'Presença' if paciente['heart_disease'] == 'Presence' else 'Ausência'} de doença cardíaca")
            st.markdown("---")
    else:
        st.warning("Não há pacientes cadastrados.")

# Função para deletar um paciente pelo nome
def deletar_paciente():
    st.title('Deletar Paciente')

    with st.form(key='form_deletar', clear_on_submit=True):
        name = st.text_input('Nome do Paciente').strip()
        submit_button = st.form_submit_button('Deletar')

    if submit_button:
        if name:
            response = requests.delete(f'{BASE_URL}/paciente', params={'name': name})
            if response.status_code == 200:
                st.success(f"Paciente {name} deletado(a) com sucesso!")
                # Limpar o estado para forçar o recarregamento dos pacientes
                if 'pacientes_data' in st.session_state:
                    del st.session_state['pacientes_data']
            else:
                st.error(f"Erro ao deletar o paciente {name}.")
        else:
            st.error("Por favor, insira o nome do paciente.")

# Interface do Streamlit
st.sidebar.title("Menu")
opcao = st.sidebar.selectbox("Escolha uma opção", ['Cadastrar Paciente', 'Listar Pacientes', 'Deletar Paciente'])

if opcao == 'Cadastrar Paciente':
    cadastrar_paciente()
elif opcao == 'Listar Pacientes':
    listar_pacientes()
elif opcao == 'Deletar Paciente':
    deletar_paciente()