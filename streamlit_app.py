import streamlit as st

st.set_page_config(page_title="Bot de Vendas - Trade Fácil", page_icon="🤖", layout="centered")

st.title("🤖 Bot de Vendas: Trade na Prática")
st.write("Aprenda a usar robôs para vender no automático, mesmo começando do zero.")

st.warning("⚠️ Aviso: Trade envolve risco. Isso é educacional, não é promessa de lucro.")

aba1, aba2, aba3, aba4 = st.tabs(["📚 Aula 1", "⚙️ Como funciona o Bot", "💰 Estratégia de R$1", "🧪 Simulador"])

with aba1:
    st.header("Aula 1: Por que as pessoas perdem?")
    st.write("- Não tem estratégia\n- Emocional\n- Sem bot")
    st.info("O bot só automatiza sua estratégia.")

with aba2:
    st.header("Como funciona um Bot de Venda")
    st.code("SE preço subir X% -> ENTÃO vender Y%", language="text")

with aba3:
    st.header("Sua Estratégia de R$1 - Inteligente!")
    st.success("Estratégia de volume!")
    preco = st.slider("Quantas pessoas compram por R$1?", 1000, 100000, 10000)
    st.metric("Faturamento só no teste", f"R$ {preco * 1:,}")

with aba4:
    st.header("Simulador de Bot")
    capital = st.number_input("Seu capital inicial (R$)", value=100.0)
    lucro_desejado = st.slider("Bot vende quando lucrar (%)", 1, 10, 3)
    if st.button("Simular venda do Bot"):
        venda = capital * (1 + lucro_desejado/100)
        st.balloons()
        st.success(f"Bot vendeu! R$ {venda:.2f}")
