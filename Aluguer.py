import streamlit as st

st.title("Loja de Aluguer de Jogos")

# Lista de jogos disponíveis
jogos = ["EA FC 26", "Minecraft 2", "GTA VI", "The Witcher 4", "Call of Duty MW4"]

# Seção para selecionar um jogo
st.header("Selecione um jogo para alugar")
jogo_selecionado = st.selectbox("Jogos disponíveis:", jogos)

# Seção para inserir informações do cliente
st.header("Informações do Cliente")
nome_cliente = st.text_input("Nome do Cliente")
dias_aluguer = st.number_input("Dias de Aluguer", min_value=1, max_value=30, step=1)

# Botão para confirmar o aluguel
if st.button("Confirmar Aluguer"):
    if nome_cliente and jogo_selecionado:
        st.success(f"Aluguer confirmado para {nome_cliente}!")
        st.write(f"Jogo: {jogo_selecionado}")
        st.write(f"Dias de Aluguer: {dias_aluguer}")
    else:
        st.error("Por favor, preencha todas as informações.")