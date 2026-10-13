import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy Gold", page_icon="🐉", layout="wide", initial_sidebar_state="expanded")

st.markdown(
    """
<style>
.stApp{background:#0f0f0f;color:#f5f1e8;}
.hero{
    background: radial-gradient(circle at top, #2a2210 0%, #1a1505 35%, #0f0f0f 100%);
    padding:48px 24px;border-radius:22px;text-align:center;
    border:2px solid #FFC300;box-shadow:0 0 40px #FFC30033;
    margin-bottom:24px;
}
.hero h1{color:#FFC300;font-size:42px}
.card{background:#1c1c1c;padding:22px;border-radius:16px;border:1px solid #2e2a1f;margin-top:8px;line-height:1.9;color:#f0e6d2;}
.card-pop{background:linear-gradient(135deg,#201c0f 0%,#151208 100%);border:2px solid #FFC300;padding:24px;border-radius:16px;margin-top:8px;}
.titulo{font-size:22px;font-weight:900;color:#FFC300;margin-bottom:10px;}
.dragao{background:#111;border:2px solid #FFC300;padding:16px;border-radius:16px;text-align:center;margin-bottom:14px;}
.legal{font-size:11px;opacity:0.5;text-align:center;margin-top:40px;color:#cbb88f;}
div[data-testid="stExpander"]{background:#1e1c10!important;border:1.5px solid #3a3520!important;border-radius:14px!important;margin-bottom:12px!important;}
div[data-testid="stExpander"] summary{color:#FFC300!important;font-weight:800!important;font-size:16px!important;}
.stButton > button{background:linear-gradient(135deg,#FFC300,#FFB000)!important;color:#111!important;border:2px solid #FFD700!important;font-weight:900!important;height:60px!important;border-radius:12px!important;}
</style>
    """
)

with st.sidebar:
    st.markdown('<div class="dragao"><div style="font-size:44px">🐉</div><b style="color:#FFC300">Academy Dragão GOLD</b><br><span style="font-size:12px;color:#cbb88f">Do zero ao primeiro trade.</span></div>', unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🐉 TRADE ACADEMY</h1><h3 style="color:#FFD700;letter-spacing:3px">GOLD EDITION</h3><p>Do zero ao seu primeiro trade com R$20</p></div>', unsafe_allow_html=True)

with st.expander("CAP 1 - O que é Bitcoin", expanded=True):
    st.markdown('<div class="card-pop"><div class="titulo">CAP 1 - O que é Bitcoin</div>Criado em 2008 após a crise. Só 21 milhões. Blockchain é livro público. BTC e ETH são mais seguros.</div>', unsafe_allow_html=True)

with st.expander("CAP 2 - Conta segura"):
    st.markdown('<div class="card"><div class="titulo">CAP 2 - Conta segura</div>1. Corretora grande<br>2. Senha forte<br>3. Validar e-mail<br>4. KYC<br>5. Ativar 2FA.</div>', unsafe_allow_html=True)

with st.expander("CAP 3 - PIX e Carteiras"):
    st.markdown('<div class="card"><div class="titulo">CAP 3 - PIX</div>Spot = bolso principal. Fluxo: Depositar
