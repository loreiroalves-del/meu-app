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
.sub{font-weight:800;color:#a78bfa;margin-top:16px;}
.legal{font-size:11px;opacity:0.4;text-align:center;margin-top:40px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>💜 TRADE ACADEMY</h1><p>Clica no capítulo abaixo pra estudar. Tudo liberado pra teste, sem pagamento.</p></div>', unsafe_allow_html=True)
st.write("")

c1,c2,c3,c4,c5 = st.columns(5)
with c1:
    if st.button("📘 CAP 1\nBitcoin", use_container_width=True): st.session_state.pagina="CAP1"; st.rerun()
with c2:
    if st.button("📗 CAP 2\nCriar conta", use_container_width=True): st.session_state.pagina="CAP2"; st.rerun()
with c3:
    if st.button("📙 CAP 3\nPix", use_container_width=True): st.session_state.pagina="CAP3"; st.rerun()
with c4:
    if st.button("📕 CAP 4\n1ª compra", use_container_width=True): st.session_state.pagina="CAP4"; st.rerun()
with c5:
    if st.button("🎮 SIMULADOR", use_container_width=True): st.session_state.pagina="SIM"; st.rerun()

c6,c7,c8,c9,c10 = st.columns(5)
with c6:
    if st.button("🤖 CAP 5\nGRID básico", use_container_width=True): st.session_state.pagina="CAP5"; st.rerun()
with c7:
    if st.button("⚙️ CAP 6\nGRID avançado", use_container_width=True): st.session_state.pagina="CAP6"; st.rerun()
with c8:
    if st.button("💸 CAP 7\nR$20", use_container_width=True): st.session_state.pagina="CAP7"; st.rerun()
with c9:
    if st.button("🛡️ CAP 8\nGolpes", use_container_width=True): st.session_state.pagina="CAP8"; st.rerun()
with c10:
    if st.button("🚀 CAP 10\nCriar app", use_container_width=True): st.session_state.pagina="CAP10"; st.rerun()

st.divider()
pag = st.session_state.pagina

if pag=="INICIO":
    st.markdown("""
    <div class="card-pop">
    <div class="titulo">👋 Como usar agora</div>
    Clica nos botões roxos ali em cima ☝️ pra mudar de capítulo.<br>
    Cada capítulo é separado, no seu lugar, sem misturar.<br>
    Começa CAP 1 depois CAP 2 até CAP 10.<br><br>
    Se no celular não aparecer tudo, arrasta os botões pro lado.
    </div>
    """, unsafe_allow_html=True)

elif pag=="CAP1":
    st.markdown('<div class="card"><div class="titulo">📘 CAP 1 - O que é dinheiro e Bitcoin</div>Dinheiro é confiança. Real vale porque todos aceitam. Bitcoin vale porque milhões no mundo aceitam. Blockchain é caderno público copiado em milhares de computadores. Bitcoin limite 21 milhões, por isso sobe e desce forte. Altcoins são outras moedas tipo ETH. Pra começar foca BTC e ETH mais estáveis.<br><br><b>Tarefa:</b> assiste 1 vídeo 10 min sobre Bitcoin hoje.</div>', unsafe_allow_html=True)

elif pag=="CAP2":
    st.markdown('<div class="card"><div class="titulo">📗 CAP 2 - Criando conta na corretora</div>Corretora = casa de câmbio de cripto. Binance maior do mundo desde 2017.<br>1. Google binance.com oficial<br>2. REGISTRAR amarelo<br>3. E-mail + senha forte anota caderno<br>4. Confirma e-mail Gmail<br>5. Nome CPF endereço igual RG<br>6. KYC foto RG frente verso + selfie segurando RG + folha Binance + data hoje luz boa<br>7. Espera 10 min Aprovado<br>8. Baixa Google Authenticator ativa 2FA anota código 16 letras<br><br><b>Tarefa:</b> cria conta hoje só isso.</div>', unsafe_allow_html=True)

elif pag=="CAP3":
    st.markdown('<div class="card"><div class="titulo">📙 CAP 3 - Como funciona Pix na corretora (só aprendizado, não precisa colocar agora)</div>1. Binance Carteira > Depositar > Fiat > BRL > Pix<br>2. Aparece chave Pix aleatória ou QR Code Copiar<br>3. No banco Nubank/Inter Pix copia e cola Cola chave Valor R$10 pra testar Confirma<br>4. Volta Binance 1-3 min aparece Carteira Spot BRL R$10<br>5. Se não cair 10 min pega comprovante com ID e abre chat Suporte<br><br>Onde fica: Carteira Spot = dinheiro disponível agora sem empréstimo mais seguro. Não clica Earn Futures Margin agora só Spot.<br><br><b>Tarefa:</b> só lê. Quando seguro deposita R$10 pra testar.</div>', unsafe_allow_html=True)

elif pag=="CAP4":
    st.markdown('<div class="card"><div class="titulo">📕 CAP 4 - Comprando Bitcoin pela primeira vez</div>1. Trade > Spot > escolhe BTC/BRL<br>2. Comprar > Mercado compra na hora<br>3. Total R$10 > Comprar BTC<br>4. Agora Carteira Spot tem BTC 0,00003 e BRL R$10<br>5. Deixa quieto olha 3 em 3h como sobe e desce anota caderno<br><br>Mercado compra na hora preço atual fácil. Limite coloca preço que quer comprar quando cair.<br><br><b>Tarefa:</b> quando tiver R$10 na corretora compra R$10 BTC e deixa 1 dia oscilando.</div>', unsafe_allow_html=True)

elif pag=="CAP5":
    st.markdown('<div class="card"><div class="titulo">🤖 CAP 5 - GRID básico feira da maçã</div>Maçã R$5 você fala compro R$4,90 10 maçãs e vendo R$5,10. Fica indo e voltando o dia todo ganha R$0,20 cada vez. 10 idas = R$2. GRID faz isso com Bitcoin automático.<br><br>Bitcoin R$300k exemplo trabalha entre 285k e 315k 10 grades. Ordens compra 286.5k 289.5k venda 301.5k 304.5k. Cai pra 289.5k compra sobe pra 292.5k vende lucro.<br><br>Ganha quando lateral quicando 295k-305k 3 dias faz 30-40 trades R$0,10 junta R$3 dia. Perde quando alta forte 350k vendeu tudo 315k perde alta ou baixa forte 200k compra tudo fica preso prejuízo.<br><br><b>Tarefa:</b> roda simulador 3 vezes R$7,81.</div>', unsafe_allow_html=True)

elif pag=="CAP6":
    st.markdown('<div class="card"><div class="titulo">⚙️ CAP 6 - GRID avançado e taxas reais</div>Config pra R$20: Par BTC/BRL inferior preço atual -4% (300k -> 288k) superior +4% (312k) grades 8-10 modo aritmético investimento R$20 /10 = R$2 por grade sem stop loss.<br><br>Taxa: Binance 0,1% por operação. Compra R$10 paga R$0,01 vende R$10 paga R$0,01 ciclo R$0,02 20 ciclos dia R$0,40 taxa. Luc
