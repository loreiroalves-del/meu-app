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
''')

with st.sidebar:
    st.markdown('''
    <div class='dragao'>
        <div style='font-size:44px'>🐉</div>
        <b style='color:#FFC300;font-size:18px'>Academy Dragao</b><br>
        <span style='font-size:13px;color:#FFC300'>GOLD EDITION</span><br>
        <span style='font-size:12px;color:#cbb88f'>Do zero ao primeiro trade</span>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('''
<div class='hero'>
    <h1>🐉 TRADE ACADEMY</h1>
    <h3 style='color:#FFD700;letter-spacing:4px;margin-top:8px'>GOLD EDITION</h3>
    <p><b>Do zero ao seu primeiro trade com R$20. Metodo pratico, sem promessa de dinheiro facil.</b></p>
</div>
''', unsafe_allow_html=True)

with st.expander("CAP 1 - O que e Bitcoin", expanded=True):
    st.markdown('''
    <div class='card-pop'>
        <div class='titulo'>O que e Bitcoin</div>
        Criado em 2008 apos a crise dos bancos. So existirao 21 milhoes. Escassez programada.<br><br>
        <b>Blockchain:</b> Livro-caixa publico copiado em milhares de computadores.<br><br>
        <b>Volatilidade:</b> Pode cair 15% e subir 20% no mesmo dia.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 2 - Como criar conta segura"):
    st.markdown('''
    <div class='card'>
        <div class='titulo'>Conta segura</div>
        1. Corretora grande e regulamentada<br>2. E-mail + senha forte<br>3. Validacao e-mail<br>4. KYC documento<br>5. Selfie com data<br>6. Ative 2FA e guarde codigo em papel.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 3 - PIX e Carteiras"):
    st.markdown('''
    <div class='card'>
        <div class='titulo'>Onde fica seu dinheiro</div>
        <b>Carteira Spot:</b> Bolso principal.<br><b>Deposito:</b> Onde PIX cai primeiro.<br><br>
        Fluxo: Carteira > Depositar > BRL > PIX > teste R$10 > Transferir para Spot. CPF igual.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 4 - Primeira compra com R$10"):
    st.markdown('''
    <div class='card'>
        <div class='titulo'>Primeira compra</div>
        Trade > Spot > BTC/BRL > Mercado > R$10 > Comprar.<br><br>
        BTC e divisivel em 8 casas. Anote preco e taxa por 3 dias.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 5 - Estrategia GRID"):
    st.markdown('''
    <div class='card-pop'>
        <div class='titulo'>O que e GRID</div>
        GRID automatiza compra na baixa e venda na alta dentro de intervalo.<br><br>
        Quando funciona: mercado lateral. Quando fica preso: rompe intervalo por cima ou por baixo.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 6 - Taxas e Configuracao"):
    st.markdown('''
    <div class='card'>
        <div class='titulo'>Taxas</div>
        0,1% por operacao. Compra R$10 = R$0,01. Ciclo = R$0,02. 20 ciclos = R$0,40 taxa.<br><br>
        Config: Intervalo -4% a +4%, 8 a 10 grades, R$2 por grade, aritmetico.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 7 - Plano 7 dias com R$20"):
    st.markdown('''
    <div class='card-pop'>
        <div class='titulo'>Plano pratico</div>
        R$20 em 10 grades = R$2 cada. 8 ciclos x R$0,04 = R$0,32/dia lateral.<br><br>
        Dia1 Conta e 2FA, Dia2 PIX e simulador, Dia3 Deposito R$20, Dia4 GRID R$10, Dia5 Analisar, Dia6 Decidir, Dia7 Registrar.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 8 - Golpes e Riscos Reais"):
    st.markdown('''
    <div class='card'>
        <div class='titulo'>O que evitar</div>
        1. Dobrar BTC no WhatsApp<br>2. Prints so lucro<br>3. GRID nao e renda fixa<br>4. Futures 125x liquida em segundos<br>5. Emprestar conta com CPF.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("CAP 10 - Como criar seu proprio app"):
    st.markdown('''
    <div class='card-pop'>
        <div class='titulo'>Bonus</div>
        Feito com Streamlit + GitHub + Streamlit Cloud gratis.<br>
        Para vender, crie link de pagamento R$20 no Mercado Pago.<br>
        Aviso: Conteudo educacional. Nao e recomendacao de investimento.
    </div>
    ''', unsafe_allow_html=True)

with st.expander("🐉 SIMULADOR DRAGAO GOLD"):
    st.markdown('''
    <div class='card-pop'>
        <div class='titulo'>Simulador Gold</div>
        Teste ficticio para entender grade, taxa e lucro liquido.
    </div>
    ''', unsafe_allow_html=True)
    inv = st.slider("Valor ficticio", 5.0, 50.0, 20.0)
    grades = st.slider("Grades", 4, 20, 8)
    if st.button("Rodar simulacao GOLD", type="primary", use_container_width=True):
        lt = 0
        tt = 0
        for i in range(grades):
            pc = random.uniform(288000, 299500)
            pv = pc * random.uniform(1.002, 1.008)
            lb = (inv/grades)*(pv/pc-1)
            taxa = (inv/grades)*0.001*2
            ll = lb - taxa
            lt += ll
            tt += taxa
            st.write(f"Grade {i+1}: Compra R$ {pc:,.0f} -> Venda R$ {pv:,.0f} | Liquido R$ {ll:.4f}")
            time.sleep(0.08)
        st.success(f"Resultado GOLD: Bruto R$ {lt+tt:.2f} - Taxas R$ {tt:.2f} = Liquido R$ {lt:.2f}")

st.markdown('''
<div class='legal'>
🐉 Trade Academy - GOLD EDITION - Conteudo educacional Lei 9.394/96.<br>
Nao e recomendacao de investimento. Criptoativo e alto risco.<br>
Tema Dourado Premium Ativo
</div>
''', unsafe_allow_html=True)
