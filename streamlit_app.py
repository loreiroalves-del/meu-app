import streamlit as st

st.set_page_config(page_title="Meu App", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0a0a0a; }
    h1, h2, h3 { color: white !important; }
    [data-testid="stMetricValue"] { color: #22ff88 !important; }
    .stButton>button { background: #22ff88; color: black; font-weight: bold; width: 100%; border-radius: 12px; border: none; height: 50px; }
</style>
""", unsafe_allow_html=True)

st.title("MEU-APP")
st.caption("App criado e publicado direto do iPhone 📱")
st.divider()

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.subheader("📊 Performance")
    c1, c2 = st.columns(2)
    c1.metric("Usuários", "1.2k", "+12%")
    c2.metric("Status", "Online", "✅")
    st.divider()
    if st.button("🚀 Lançar Fogos"):
        st.balloons()
        st.success("Funcionando!")

with col2:
    st.image("43d95551-ce31-cbb5-d7cf-e132c79897f7.png", use_container_width=True)

st.divider()
st.markdown("<p style='text-align:center'>Feito com ❤️ direto de Fortaleza</p>", unsafe_allow_html=True)
