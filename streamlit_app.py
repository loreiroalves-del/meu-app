import streamlit as st, random, time

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
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>💜 TRADE ACADEMY</h1>
<p>Clica no capítulo abaixo pra estudar. Tudo liberado pra teste, sem pagamento.</p>
</div>
""", unsafe_allow_html=True)
st.write("")

c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    if st.button("📘 CAP 1\nBitcoin", use_container_width=True):
        st.session_state.pagina="CAP1"
        st.rerun()
with c2:
    if st.button("📗 CAP 2\nCriar conta", use_container_width=True):
        st.session_state.pagina="CAP2"
        st.rerun()
with c3:
    if st.button("📙 CAP 3\nPix", use_container_width=True):
        st.session_state.pagina="CAP3"
        st.rerun()
with c4:
    if st.button("📕 CAP 4\n1a compra", use_container_width=True):
        st.session_state.pagina="CAP4"
        st.rerun()
with c5:
    if st.button("🎮 SIMULADOR", use_container_width=True):
        st.session_state.pagina="SIM"
        st.rerun()

c6,c7,c8,c9,c10 = st.columns(5)
with c6:
    if st.button("🤖 CAP 5\nGRID", use_container_width=True):
        st.session_state.pagina="CAP5"
        st.rerun()
with c7:
    if st.button("⚙️ CAP 6\nAvancado", use_container_width=True):
        st.session_state.pagina="CAP6"
        st.rerun()
with c8:
    if st.button("💸 CAP 7\nR$20", use_container_width=True):
        st.session_state.pagina="CAP7"
        st.rerun()
with c9:
    if st.button("🛡️ CAP 8\nGolpes", use_container_width=True):
        st.session_state.pagina="CAP8"
        st.rerun()
with c10:
    if st.button("🚀 CAP 10\nCriar app", use_container_width=True):
        st.session_state.pagina="CAP10"
        st.rerun()

st.divider()
pag = st.session_state.pagina

if pag=="INICIO":
    st.markdown("""
    <div class="card-pop">
    <div class="titulo">Como usar</div>
    Clica nos botoes roxos ali em cima para mudar de capitulo.<br>
    Cada capitulo separado no seu lugar sem misturar.<br>
    Comeca CAP 1 depois CAP 2 ate CAP 10.<br><br>
    Se no celular nao aparecer tudo arrasta os botoes pro lado.
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP1":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 1 - O que e dinheiro e Bitcoin</div>
    Dinheiro e confianca. Real vale porque todos aceitam. Bitcoin vale porque milhoes no mundo aceitam.<br>
    Blockchain e caderno publico copiado em milhares de computadores.<br>
    Bitcoin limite 21 milhoes por isso sobe e desce forte. Altcoins sao outras moedas tipo ETH.<br>
    Pra comecar foca BTC e ETH mais estaveis.<br><br>
    Tarefa: assiste 1 video 10 min sobre Bitcoin hoje.
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP2":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 2 - Criando conta na corretora</div>
    Corretora = casa de cambio de cripto. Binance maior do mundo desde 2017.<br>
    1. Google binance.com oficial<br>
    2. REGISTRAR amarelo<br>
    3. E-mail + senha forte anota caderno<br>
    4. Confirma e-mail Gmail<br>
    5. Nome CPF endereco igual RG<br>
    6. KYC foto RG frente verso + selfie segurando RG + folha Binance + data hoje luz boa<br>
    7. Espera 10 min Aprovado<br>
    8. Baixa Google Authenticator ativa 2FA anota codigo 16 letras<br><br>
    Tarefa: cria conta hoje so isso.
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP3":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 3 - Como funciona Pix na corretora (so aprendizado)</div>
    Voce NAO precisa colocar dinheiro agora se nao quiser. So aprendizado.<br><br>
    1. Binance Carteira > Depositar > Fiat > BRL > Pix<br>
    2. Aparece chave Pix aleatoria ou QR Code Copiar<br>
    3. No banco Nubank/Inter Pix copia e cola Cola chave Valor R$10 pra testar Confirma<br>
    4. Volta Binance 1-3 min aparece Carteira Spot BRL R$10<br>
    5. Se nao cair 10 min pega comprovante com ID e abre chat Suporte<br><br>
    Onde fica: Carteira Spot = dinheiro disponivel agora sem emprestimo mais seguro.<br>
    Nao clica Earn Futures Margin agora so Spot.
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP4":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 4 - Comprando Bitcoin pela primeira vez</div>
    1. Trade > Spot > escolhe BTC/BRL<br>
    2. Comprar > Mercado compra na hora<br>
    3. Total R$10 > Comprar BTC<br>
    4. Agora Carteira Spot tem BTC 0,00003 e BRL R$10<br>
    5. Deixa quieto olha 3 em 3h como sobe e desce anota caderno<br><br>
    Mercado compra na hora preco atual facil. Limite coloca preco que quer comprar quando cair.<br>
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP5":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 5 - GRID basico feira da maca</div>
    Maca R$5 voce fala compro R$4,90 10 macas e vendo R$5,10. Fica indo e voltando o dia todo ganha R$0,20 cada vez.<br>
    GRID faz isso com Bitcoin automatico.<br><br>
    Bitcoin R$300k exemplo trabalha entre 285k e 315k 10 grades.<br>
    Ganha quando lateral quicando 295k-305k 3 dias faz 30-40 trades R$0,10 junta R$3 dia.<br>
    Perde quando alta forte 350k vendeu tudo 315k perde alta ou baixa forte 200k compra tudo fica preso prejuizo.<br>
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP6":
    st.markdown("""
    <div class="card">
    <div class="titulo">CAP 6 - GRID avancado e taxas reais</div>
    Config pra R$20: Par BTC/BRL inferior
