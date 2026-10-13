import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy Gold Edition", page_icon="🐉", layout="wide", initial_sidebar_state="expanded")

st.markdown('''
<style>
.stApp{background:#0f0f0f;color:#f5f1e8;}
.hero{background:radial-gradient(circle at top,#2a2210 0%,#0f0f0f 100%);padding:40px 24px;border-radius:20px;text-align:center;border:2px solid #FFC300;margin-bottom:24px;}
.hero h1{color:#FFC300;font-size:38px;margin:0;}
.card{background:#1c1c1c;padding:20px;border-radius:14px;border:1px solid #2e2a1f;margin-top:8px;line-height:1.8;color:#f0e6d2;font-size:15px;}
.card-pop{background:linear-gradient(135deg,#201c0f 0%,#151208 100%);border:2px solid #FFC300;padding:20px;border-radius:14px;margin-top:8px;line-height:1.8;color:#f0e6d2;}
.titulo{color:#FFC300;font-weight:900;font-size:20px;margin-bottom:10px;}
.dragao{background:#111;border:2px solid #FFC300;padding:16px;border-radius:14px;text-align:center;margin-bottom:14px;}
.legal{font-size:11px;opacity:0.5;text-align:center;margin-top:40px;color:#cbb88f;line-height:1.6;}
div[data-testid="stExpander"]{background:#1e1c10!important;border:1px solid #3a3520!important;border-radius:12px!important;margin-bottom:10px!important;}
div[data-testid="stExpander"] summary{color:#FFC300!important;font-weight:800!important;font-size:16px!important;}
.stButton > button{background:linear-gradient(135deg,#FFC300,#FFB000)!important;color:#111!important;font-weight:900!important;height:60px!important;border-radius:12px!important;}
</style>
''', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('''
    <div class='dragao'>
        <div style='font-size:44px'>🐉</div>
        <b style='color:#FFC300;font-size:18px'>Academy Dragao</b><br>
        <span style='font-size:13px;color:#FFC300'>GOLD EDITION</span>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('''
<div class='hero'>
    <h1>🐉 TRADE ACADEMY</h1>
    <h3 style='color:#FFD700;letter-spacing:4px'>GOLD EDITION</h3>
    <p><b>Do zero ao seu primeiro trade com R$20</b></p>
</div>
''', unsafe_allow_html=True)

with st.expander("CAP 1 - O que e Bitcoin", expanded=True):
    st.markdown('''<div class='card-pop'><div class='titulo'>O que e Bitcoin</div>Criado em 2008. So 21 milhoes. Blockchain e livro publico. BTC e ETH mais seguros.</div>''', unsafe_allow_html=True)

with st.expander("CAP 2 - Conta segura"):
    st.markdown('''<div class='card'><div class='titulo'>Conta segura</div>1. Corretora grande<br>2. Senha forte<br>3. Email validado<br>4. KYC<br>5. 2FA ativo</div>''', unsafe_allow_html=True)

with st.expander("CAP 3 - PIX"):
    st.markdown('''<div class='card'><div class='titulo'>PIX e Carteiras</div>Spot e bolso principal. Fluxo: Depositar > BRL > PIX > teste R$10 > Transferir.</div>''', unsafe_allow_html=True)

with st.expander("CAP 4 - Primeira compra"):
    st.markdown('''<div class='card'><div class='titulo'>Primeira compra</div>Trade > Spot > BTC/BRL > Mercado > R$10. BTC divisivel em 8 casas.</div>''', unsafe_allow_html=True)

with st.expander("CAP 5 - GRID"):
    st.markdown('''<div class='card-pop'><div class='titulo'>GRID</div>Compra na baixa e venda na alta dentro de intervalo. Melhor em lateral.</div>''', unsafe_allow_html=True)

with st.expander("CAP 6 - Taxas"):
    st.markdown('''<div class='card'><div class='titulo'>Taxas</div>0,1% por operacao. Config: -4% a +4%, 8 grades, R$2 cada.</div>''', unsafe_allow_html=True)

with st.expander("CAP 7 - Plano 7 dias"):
    st.markdown('''<div class='card-pop'><div class='titulo'>Plano</div>Dia1 Conta, Dia2 Simulador, Dia3 Deposito R$20, Dia4 GRID, Dia5 Analisar, Dia6 Decidir, Dia7 Registrar.</div>''', unsafe_allow_html=True)

with st.expander("CAP 8 - Golpes"):
    st.markdown('''<div class='card'><div class='titulo'>Golpes</div>Evite: dobrar BTC no zap, prints so lucro, futures 125x, emprestar conta.</div>''', unsafe_allow_html=True)

with st.expander("SIMULADOR GOLD"):
    inv = st.slider("Valor", 5.0, 50.0, 20.0)
    grades = st.slider("Grades", 4, 20, 8)
    if st.button("Rodar GOLD", use_container_width=True):
        total = 0
        for i in range(grades):
            pc = random.uniform(288000, 299500)
            pv = pc * random.uniform(1.002, 1.008)
            lucro = (inv/grades)*(pv/pc-1) - (inv/grades)*0.002
            total += lucro
            st.write(f"Grade {i+1}: R$ {lucro:.4f}")
        st.success(f"Total GOLD R$ {total:.2f}")
