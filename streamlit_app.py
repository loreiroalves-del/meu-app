import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy Gold", page_icon="🐉", layout="wide")

st.markdown("""
<style>
.stApp{background:#0f0f0f;color:#f5f1e8;}
.hero{background:radial-gradient(circle at top,#2a2210 0%,#0f0f0f 100%);padding:40px 24px;border-radius:22px;text-align:center;border:2px solid #FFC300;margin-bottom:20px;}
.hero h1{color:#FFC300;font-size:40px}
.card{background:#1c1c1c;padding:20px;border-radius:14px;border:1px solid #2e2a1f;margin-top:8px;line-height:1.8;color:#f0e6d2;}
.card-pop{background:#201c0f;border:2px solid #FFC300;padding:20px;border-radius:14px;margin-top:8px;}
.titulo{color:#FFC300;font-weight:900;font-size:20px;margin-bottom:8px;}
.dragao{background:#111;border:2px solid #FFC300;padding:14px;border-radius:14px;text-align:center;margin-bottom:12px;}
div[data-testid="stExpander"]{background:#1e1c10!important;border:1.5px solid #3a3520!important;border-radius:12px!important;margin-bottom:10px!important;}
div[data-testid="stExpander"] summary{color:#FFC300!important;font-weight:800!important;}
.stButton > button{background:linear-gradient(135deg,#FFC300,#FFB000)!important;color:#111!important;font-weight:900!important;height:55px!important;border-radius:10px!important;}
</style>
""")

with st.sidebar:
    st.markdown("""
    <div class='dragao'>
        <div style='font-size:44px'>🐉</div>
        <b style='color:#FFC300'>Academy Dragão GOLD</b><br>
        <span style='font-size:12px;color:#cbb88f'>Do zero ao primeiro trade</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='hero'>
    <h1>🐉 TRADE ACADEMY</h1>
    <h3 style='color:#FFD700;letter-spacing:3px'>GOLD EDITION</h3>
    <p>Do zero ao seu primeiro trade com R$20</p>
</div>
""", unsafe_allow_html=True)

with st.expander("CAP 1 - O que é Bitcoin", expanded=True):
    st.markdown("""
    <div class='card-pop'>
        <div class='titulo'>CAP 1 - O que é Bitcoin</div>
        Criado em 2008. Só existirão 21 milhões. Blockchain é livro público. BTC e ETH são mais seguros para começar.
    </div>
    """, unsafe_allow_html=True)

with st.expander("CAP 2 - Conta segura"):
    st.markdown("""
    <div class='card'>
        <div class='titulo'>CAP 2 - Conta segura</div>
        1. Corretora grande<br>2. Senha forte 12+<br>3. Validar email<br>4. KYC documento<br>5. Ativar 2FA
    </div>
    """, unsafe_allow_html=True)

with st.expander("CAP 3 - PIX e Carteiras"):
    st.markdown("""
    <div class='card'>
        <div class='titulo'>CAP 3 - PIX</div>
        Spot = bolso principal. Fluxo: Depositar > BRL > PIX > teste R$10 > Transferir para Spot.
    </div>
    """, unsafe_allow_html=True)

with st.expander("CAP 4 - Primeira compra"):
    st.markdown("""
    <div class='card'>
        <div class='titulo'>CAP 4 - Primeira compra</div>
        Trade > Spot > BTC/BRL > Mercado > R$10. Bitcoin é divisível em 8 casas.
    </div>
    """, unsafe_allow_html=True)

with st.expander("CAP 5 - GRID"):
    st.markdown("""
    <div class='card-pop'>
        <div class='titulo'>CAP 5 - GRID</div>
        Compra na baixa e venda na alta dentro de intervalo. Melhor em mercado lateral.
    </div>
    """, unsafe_allow_html=True)

with st.expander("CAP 6 - Taxas"):
