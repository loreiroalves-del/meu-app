import streamlit as st

st.set_page_config(page_title="Meu App", page_icon="🚀")

st.title("🚀 Meu App está no ar!")
st.write("Deu certo! Agora seu app é seu.")

nome = st.text_input("Qual seu nome?")
if nome:
    st.success(f"Bem-vindo, {nome}!")

st.write("---")
st.write("O que você quer colocar aqui? Me fala que eu mudo pra você.")
