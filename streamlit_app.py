import streamlit as st

st.set_page_config(page_title="Meu App", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0a0a0a; }
    h1 { color: white !important; }
    [data-testid="stMetricValue"] { color: #22ff88 !important; }
    .stButton>button { background: #22ff88; color: black; font-weight: bold; width: 100%; border-radius: 12px; border: none; height: 50px; }
</style>
""", unsafe_allow_html=True)

st.title("MEU-APP")
st.caption("App criado e publicado direto do iPhone 📱")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Performance")
    st.metric("Usuários", "1.2k", "+12%")
    st.metric("Status", "Online", "✅")
    st.divider()
    if st.button("🚀 Lançar Fogos"):
        st.balloons()
        st.success("Tá funcionando!")

with col2:
    try:
        st.image("43d95551-ce31-cbb5-d7cf-e132c79897f7.png", use_container_width=True)
    except:
        st.info("👆 Sua imagem do GitHub vai aparecer aqui. Se não aparecer, o nome do arquivo no GitHub tá diferente.")
        st.markdown("### Imagem Preview")
        st.markdown("> Coloca a imagem na raiz do repositório com o nome exato pra carregar.")

st.divider()
