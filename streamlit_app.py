import streamlit as st
st.set_page_config(page_title="Trade Academy", page_icon="📈")
menu = st.sidebar.radio("AULAS", ["Inicio","O que e Trade","Como Comecar","Analise","Risco","Simulador"])
if menu=="Inicio":
    st.title("📈 Trade Academy")
    st.write("Aprenda trade do zero, sem furada.")
    st.info("Use o menu lateral")
elif menu=="O que e Trade":
    st.header("O que e Trade?")
    st.write("Comprar e vender ativos pra lucrar na diferenca.")
    st.write("Day Trade: mesmo dia. Swing: dias/semanas (melhor pra iniciante). Position: meses.")
elif menu=="Como Comecar":
    st.header("Passo a passo")
    st.write("1- Abra conta em corretora (Clear/XP/Binance) gratis")
    st.write("2- Treine no simulador")
    st.write("3- Comece com R$100-300")
    st.write("4- Nunca arrisque +2% por operacao")
elif menu=="Analise":
    st.header("Analise Tecnica")
    st.write("Vela VERDE subiu, VERMELHA caiu.")
    st.write("SUPORTE=chao (compra), RESISTENCIA=teto (venda)")
    st.write("Media 9 acima da 21 = alta")
elif menu=="Risco":
    st.header("Gerenciamento")
    cap=st.slider("Seu capital R$",100,10000,1000)
    st.metric("Perda max por trade",f"R$ {cap*0.02}")
    st.write("Sempre use STOP LOSS!")
elif menu=="Simulador":
    st.header("Simulador")
    c=st.number_input("Preco compra",30.0)
    a=st.slider("Preco atual",25.0,35.0,31.5)
    q=st.number_input("Qtd",100)
    l=(a-c)*q
    if l>=0: st.success(f"LUCRO R$ {l:.2f}")
    else: st.error(f"PREJUIZO R$ {l:.2f}")
