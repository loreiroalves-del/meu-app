import streamlit as st

st.set_page_config(page_title="Trade na Prática", page_icon="🤖")
LINK_1 = "https://mpago.la/1mfEXkt"
LINK_20 = "https://mpago.la/1jN2tXo"

if "pago1" not in st.session_state: st.session_state.pago1 = False
if "pago20" not in st.session_state: st.session_state.pago20 = False

st.title("🤖 Trade na Prática")

if not st.session_state.pago1:
    st.header("Bot de Trade por apenas R$1")
    st.write("Aprenda a usar o bot e lucrar todo dia.")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # troca seu video
    st.link_button("💳 PAGAR R$1 E COMEÇAR", LINK_1, use_container_width=True)
    senha = st.text_input("Já pagou R$1? Digite TRADE1:")
    if st.button("Liberar acesso de R$1"):
        if senha.upper() == "TRADE1":
            st.session_state.pago1 = True
            st.rerun()
        else:
            st.error("Senha errada. É TRADE1")

elif not st.session_state.pago20:
    st.success("✅ Acesso de R$1 liberado!")
    st.subheader("Aula 1 - Como usar o bot")
    st.write("Seu conteúdo de R$1 aqui...")
    st.subheader("Aula 2 - Estratégia R$15/dia")
    st.write("Seu conteúdo de R$1 aqui...")
    
    st.divider()
    st.header("🔥 OFERTA VIP - Quer criar um bot igual a mim?")
    st.write("Eu te ensino a criar um bot inteligente igual a esse que responde tudo, igual o ChatGPT, e que você pode vender.")
    st.write("**De R$97 por R$20 hoje.**")
    st.link_button("🚀 QUERO PAGAR R$20 E APRENDER A CRIAR", LINK_20, use_container_width=True)
    senha2 = st.text_input("Já pagou os R$20? Digite TRADE20:")
    if st.button("Liberar Módulo VIP"):
        if senha2.upper() == "TRADE20":
            st.session_state.pago20 = True
            st.rerun()
        else:
            st.error("Senha VIP errada. É TRADE20")

else:
    st.balloons()
    st.success("👑 VOCÊ É VIP! Acesso total liberado!")
    st.header("Módulo VIP - Como criar seu bot inteligente")
    st.write("Aula 1: Como criei esse site no Streamlit")
    st.code("import streamlit as st\nst.title('Meu Bot')", language="python")
    st.write("Aula 2: Como colocar para vender no Mercado Pago")
    st.write("Aula 3: Como fazer o bot responder igual eu (usando OpenAI)")
    st.write("Parabéns! Agora você pode criar e vender o seu próprio bot!")
