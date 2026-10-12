import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy", page_icon="💜", layout="wide")

if "pagina" not in st.session_state:
    st.session_state.pagina = "INICIO"

st.markdown("""
<style>
.stApp{background:#0b0a12;color:#eee;}
.hero{background:radial-gradient(circle at top,#7c3aed 0%,#1a1625 60%,#0b0a12 100%);padding:40px 20px;border-radius:28px;text-align:center;border:2px solid #7c3aed;}
.card{background:#1e1b2e;padding:24px;border-radius:18px;border:1px solid #3a3450;margin-bottom:14px;line-height:1.9;}
.card-pop{background:linear-gradient(135deg,#2a1f4a 0%,#1e1b2e 100%);border:2px solid #a78bfa;padding:24px;border-radius:18px;margin-bottom:14px;}
.titulo{font-size:24px;font-weight:900;color:#d8b4fe;}
.legal{font-size:11px;opacity:0.4;text-align:center;margin-top:40px;}
/* BOTAO ROXO BEM VISIVEL */
.stButton > button{
background:#7c3aed !important;
color:white !important;
border:2px solid #a78bfa !important;
font-weight:900 !important;
font-size:14px !important;
border-radius:12px !important;
height:60px !important;
}
.stButton > button:hover{
background:#a78bfa !important;
color:black !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>💜 TRADE ACADEMY</h1>
<p>Clica no capitulo abaixo para estudar. Tudo liberado para teste.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    if st.button("CAP 1\nBitcoin", use_container_width=True):
        st.session_state.pagina = "CAP1"
        st.rerun()
with c2:
    if st.button("CAP 2\nCriar conta", use_container_width=True):
        st.session_state.pagina = "CAP2"
        st.rerun()
with c3:
    if st.button("CAP 3\nPix", use_container_width=True):
        st.session_state.pagina = "CAP3"
        st.rerun()
with c4:
    if st.button("CAP 4\n1a compra", use_container_width=True):
        st.session_state.pagina = "CAP4"
        st.rerun()
with c5:
    if st.button("SIMULADOR", use_container_width=True):
        st.session_state.pagina = "SIM"
        st.rerun()

c6,c7,c8,c9,c10 = st.columns(5)
with c6:
    if st.button("CAP 5\nGRID", use_container_width=True):
        st.session_state.pagina = "CAP5"
        st.rerun()
with c7:
    if st.button("CAP 6\nAvancado", use_container_width=True):
        st.session_state.pagina = "CAP6"
        st.rerun()
with c8:
    if st.button("CAP 7\nR$20", use_container_width=True):
        st.session_state.pagina = "CAP7"
        st.rerun()
with c9:
    if st.button("CAP 8\nGolpes", use_container_width=True):
        st.session_state.pagina = "CAP8"
        st.rerun()
with c10:
    if st.button("CAP 10\nCriar app", use_container_width=True):
        st.session_state.pagina = "CAP10"
        st.rerun()

st.divider()
pag = st.session_state.pagina

if pag == "INICIO":
    st.markdown("""
    <div class="card-pop">
    <div class="titulo">Como usar</div>
    Clica nos botoes ROXOS acima para mudar de capitulo.<br>
    Agora com letra branca bem visivel.<br>
    Comeca CAP 1 depois CAP 2 ate CAP 10.
    </div>
    """, unsafe_allow_html=True)
elif pag == "CAP1":
    st.markdown("""<div class="card"><div class="titulo">CAP 1 - O que e Bitcoin</div>Dinheiro e confianca. Bitcoin vale porque milhoes aceitam.<br>Blockchain e caderno publico copiado em milhares de PCs.<br>Bitcoin limite 21 milhoes, sobe e desce forte.</div>""", unsafe_allow_html=True)
elif pag == "CAP2":
    st.markdown("""<div class="card"><div class="titulo">CAP 2 - Criar conta</div>1. binance.com oficial<br>2. REGISTRAR<br>3. E-mail + senha forte<br>4. Confirma e-mail<br>5. KYC foto RG + selfie<br>6. Ativa 2FA Google Authenticator</div>""", unsafe_allow_html=True)
elif pag == "CAP3":
    st.markdown("""<div class="card"><div class="titulo">CAP 3 - Como funciona Pix (so aprendizado)</div>Voce NAO precisa colocar dinheiro agora.<br>1. Binance Carteira > Depositar > BRL > Pix<br>2. Copia chave<br>3. Banco Pix copia e cola R$10 teste<br>4. Volta Binance 1-3 min cai em Spot</div>""", unsafe_allow_html=True)
elif pag == "CAP4":
    st.markdown("""<div class="card"><div class="titulo">CAP 4 - Primeira compra</div>1. Trade > Spot > BTC/BRL<br>2. Comprar > Mercado<br>3. Total R$10 > Comprar BTC<br>4. Deixa quieto olha 3 em 3h</div>""", unsafe_allow_html=True)
elif pag == "CAP5":
    st.markdown("""<div class="card"><div class="titulo">CAP 5 - GRID basico</div>Feira: maca R$5 compra R$4,90 vende R$5,10 ganha R$0,20.<br>GRID faz isso com Bitcoin automatico.</div>""", unsafe_allow_html=True)
elif pag == "CAP6":
    st.markdown("""<div class="card"><div class="titulo">CAP 6 - GRID avancado e taxas</div>Config R$20: BTC/BRL inferior -4% superior +4% grades 8-10 R$2 por grade.<br>Taxa 0,1% por operacao.<br>Trade > Bots > Spot Grid > Criar > 288000 312000 10 grades R$20.</div>""", unsafe_allow_html=True)
elif pag == "CAP7":
    st.markdown("""<div class="card"><div class="titulo">CAP 7 - Plano 7 dias com R$20</div>R$20 /10 = R$2 grade. R$0,04 x 8 = R$0,32 dia.<br>Dia 1 conta<br>Dia 2 deposita olha<br>Dia 3 compra R$10 BTC<br>Dia 4 GRID<br>Dia 5 ve operacoes<br>Dia 6 mais R$10 ou para<br>Dia 7 anota tudo</div>""", unsafe_allow_html=True)
elif pag == "CAP8":
    st.markdown("""<div class="card"><div class="titulo">CAP 8 - Golpes</div>1. Dobrar Bitcoin WhatsApp golpe<br>2. Print lucro falso<br>3. GRID nao magico<br>4. NAO Futures 125x<br>5. Anota tudo</div>""", unsafe_allow_html=True)
elif pag == "CAP10":
    st.markdown("""<div class="card"><div class="titulo">CAP 10 - BONUS Criar seu app e vender R$20</div>Ferramentas gratis: Streamlit + GitHub + Streamlit Cloud.<br>Copia codigo troca textos.<br>Cobrar: Mercado Pago R$20 Pix verifica e-mail via API.<br>Divulga TikTok mostrando simulador R$7,81.</div>""", unsafe_allow_html=True)
elif pag == "SIM":
    st.markdown("""<div class="card-pop"><div class="titulo">Simulador R$7,81</div>Treina sem dinheiro real.</div>""", unsafe_allow_html=True)
    inv = st.slider("Valor ficticio", 5.0, 50.0, 7.81)
    st.metric("Ficticio", f"R$ {inv:.2f}", "+R$ 0,32 hoje exemplo")
    if st.button("RODAR SIMULACAO AGORA", type="primary", use_container_width=True):
        barra = st.progress(0)
        for i in range(8):
            barra.progress((i+1)*12)
            st.write(f"Trade {i+1}: Comprou R$ {random.uniform(299200,299800):.2f} -> Vendeu R$ {random.uniform(300200,300800):.2f} | Lucro R$ 0,0{random.randint(2,9)}")
            time.sleep(0.4)
        st.balloons()
        st.success("Isso e GRID: pouquinho muitas vezes.")

st.markdown('<div class="legal">Trade Academy - Botoes roxos visiveis agora.</div>', unsafe_allow_html=True)
