import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy - Dragão", page_icon="🐉", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp{background:#0f0707;color:#ffe9e9;}
.hero{
    background:radial-gradient(circle at top,#ff1a1a 0%,#8b0000 45%,#1a0505 100%);
    padding:38px 20px;border-radius:24px;text-align:center;
    border:2px solid #ff3333;box-shadow:0 0 30px #ff000066;
    margin-bottom:20px;
}
.card{
    background:#1f0f0f;padding:22px;border-radius:16px;
    border:1px solid #5a1a1a;margin-top:8px;
    line-height:1.9;font-size:15px;
}
.card-pop{
    background:linear-gradient(135deg,#3a1010 0%,#1a0808 100%);
    border:2px solid #ff4444;padding:22px;border-radius:16px;
    margin-top:8px;
}
.titulo{font-size:22px;font-weight:900;color:#ff6b6b;margin-bottom:10px;}
.dragao{background:#2a1212;border:2px dashed #ff4444;padding:14px;border-radius:16px;text-align:center;margin-bottom:12px;}
.legal{font-size:11px;opacity:0.4;text-align:center;margin-top:40px;line-height:1.6;}
div[data-testid="stExpander"]{
    background:linear-gradient(135deg,#cc0000,#5a0000)!important;
    border:2px solid #ff6666!important;
    border-radius:14px!important;
    margin-bottom:10px!important;
}
div[data-testid="stExpander"] summary{
    color:white!important;
    font-weight:800!important;
    font-size:16px!important;
}
div[data-testid="stExpander"] summary p{color:white!important;font-weight:800!important;}
.stButton > button{
    background:linear-gradient(135deg,#ff1a1a,#8b0000)!important;
    color:white!important;border:2px solid #ff9999!important;
    font-weight:900!important;height:60px!important;border-radius:12px!important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="dragao"><div style="font-size:44px">🐉</div><b>Academy Dragão</b><br><span style="font-size:13px">Do zero ao primeiro trade com segurança.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><b>🐉 O que você vai aprender</b><br><span style="font-size:13px">Bitcoin, conta segura, PIX, primeira compra, GRID, taxas, plano R$20 e como evitar golpes.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="font-size:11px;opacity:0.7">Conteúdo educacional - Lei 9.394/96<br>Não é recomendação de investimento<br>Criptoativo é renda variável de alto risco</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🐉 TRADE ACADEMY</h1>
<p><b>Do zero ao seu primeiro trade com R$20. Método prático, sem promessa de dinheiro fácil.</b><br>Aprenda com segurança, entenda taxas e riscos reais antes de começar.</p>
</div>
""", unsafe_allow_html=True)

with st.expander("CAP 1 - O que é Bitcoin", expanded=True):
    st.markdown('<div class="card-pop"><div class="titulo">O que é Bitcoin</div>Criado em 2008 após a crise dos bancos. Proposta: um dinheiro que nenhum governo pode imprimir à vontade.<br><br><b>Por que tem valor?</b> Porque milhões de pessoas aceitam e só existirão 21 milhões de unidades. Escassez programada.<br><br><b>Blockchain:</b> Um livro-caixa público copiado em milhares de computadores. Se alguém tenta fraudar, os demais recusam.<br><br><b>Volatilidade:</b> Por ser escasso e global, o preço varia forte. Pode cair 15% e subir 20% no mesmo dia.<br><br><b>Comece pelo básico:</b> BTC e ETH são os mais antigos e negociados. Moedas novas prometendo 1000% em dias têm risco altíssimo de golpe.</div>', unsafe_allow_html=True)

with st.expander("CAP 2 - Como criar conta segura"):
    st.markdown('<div class="card"><div class="titulo">Conta segura</div><b>1.</b> Escolha uma corretora grande e regulamentada. Confira o domínio oficial e o cadeado https. Nunca use links de Telegram.<br><b>2.</b> Cadastro: e-mail + senha forte (12+ caracteres).<br><b>3.</b> Validação por e-mail.<br><b>4.</b> KYC: foto do documento legível, sem flash, dados iguais ao RG.<br><b>5.</b> Selfie com documento e papel com data.<br><b>6.</b> Ative autenticação em 2 fatores (2FA) no app autenticador e guarde o código de recuperação em papel.<br><br>Corretora séria nunca pede senha ou código 2FA por mensagem.</div>', unsafe_allow_html=True)

with st.expander("CAP 3 - PIX e Carteiras"):
    st.markdown('<div class="card"><div class="titulo">Onde fica seu dinheiro</div><b>Carteira Spot:</b> Bolso principal onde ficam seus ativos após compra.<br><b>Carteira de Depósito:</b> Onde o PIX cai primeiro. Depois você transfere para Spot.<br><br><b>Fluxo de depósito:</b> Carteira > Depositar > BRL > PIX > copie a chave > faça PIX de R$10 de teste no seu banco > aguarde 1 a 3 min > Transfira para Spot.<br><br>O CPF do banco deve ser igual ao da corretora.</div>', unsafe_allow_html=True)

with st.expander("CAP 4 - Primeira compra com R$10"):
    st.markdown('<div class="card"><div class="titulo">Primeira compra</div>Trade > Spot > par BTC/BRL > ordem a Mercado > valor R$10 > Comprar.<br><br>Você verá frações de BTC na carteira Spot. Bitcoin é divisível em 8 casas decimais, não precisa comprar 1 inteiro.<br><br>Exercício: anote preço, taxa e valor por 3 dias. Isso treina emocional sem risco alto.</div>', unsafe_allow_html=True)

with st.expander("CAP 5 - Estratégia GRID"):
    st.markdown('<div class="card-pop"><div class="titulo">O que é GRID</div>GRID automatiza compra na baixa e venda na alta dentro de um intervalo que você define.<br><br>Exemplo: configura para comprar a R$299.000 e vender a R$300.000. Cria várias ordens entre esses preços e opera sozinho.<br><br><b>Quando funciona melhor?</b> Mercado lateral, indo e voltando no mesmo intervalo.<br><b>Quando fica preso?</b> Se sobe muito e sai por cima, você vende tudo e perde a alta. Se cai muito e sai por baixo, fica com o ativo desvalorizado aguardando recuperação.</div>', unsafe_allow_html=True)

with st.expander("CAP 6 - Taxas e Configuração"):
    st.markdown('<div class="card"><div class="titulo">Taxas</div>Taxa média: 0,1% por operação. Compra de R$10 = R$0,01. Venda de R$10 = R$0,01. Ciclo completo = R$0,02.<br><br>Exemplo: 20 ciclos = R$0,40 de taxa. Se lucro bruto de R$0,04 x 20 = R$0,80, líquido = R$0,40.<br><br><b>Configuração de aprendizado com R$20:</b> Intervalo -4% a +4%, 8 a 10 grades, R$2 por grade, modo aritmético.<br><br>Caminho genérico: Bots > Spot Grid > Criar > definir inferior, superior, grades e valor total.</div>', unsafe_allow_html=True)

with st.expander("CAP 7 - Plano 7 dias com R$20"):
    st.markdown('<div class="card-pop"><div class="titulo">Plano prático</div>Matemática real: R$20 dividido em 10 grades = R$2 cada. 8 ciclos x R$0,04 = R$0,32/dia em cenário lateral.<br><br><b>Dia 1:</b> Criar conta e 2FA<br><b>Dia 2:</b> Entender PIX e testar simulador<br><b>Dia 3:</b> Depósito de R$20 e compra de R$10<br><b>Dia 4:</b> Criar GRID com R$10<br><b>Dia 5:</b> Analisar taxas e operações<br><b>Dia 6:</b> Decidir se adiciona mais R$10<br><b>Dia 7:</b> Registrar aprendizados<br><br>Use apenas valores que não comprometem suas contas.</div>', unsafe_allow_html=True)

with st.expander("CAP 8 - Golpes e Riscos Reais"):
    st.markdown('<div class="card"><div class="titulo">O que evitar</div><b>1.</b> Dobrar Bitcoin por WhatsApp.<br><b>2.</b> Prints de lucro sem mostrar perdas.<br><b>3.</b> Achar que GRID é renda fixa - cai 30% acontece e fica preso.<br><b>4.</b> Futures / Margem / Alavancagem 125x - liquida em segundos. Fique no Spot.<br><b>5.</b> Emprestar conta com seu CPF.<br><b>6.</b> Operar ansioso.<br><br>Imposto: vendas acima de R$35 mil/mês têm tributação. Guarde comprovantes.</div>', unsafe_allow_html=True)

with st.expander("CAP 10 - Como criar seu próprio app"):
    st.markdown('<div class="card-pop"><div class="titulo">Bônus</div>Este app foi feito com Streamlit + GitHub + Streamlit Cloud (gratuito).<br><br>Você pode replicar para seu nicho, trocando textos. Para vender, crie link de pagamento de R$20 em gateway como Mercado Pago.<br><br>Aviso obrigatório: Conteúdo educacional. Não é recomendação de investimento. Criptoativo é de alto risco. Não indicamos corretora específica.</div>', unsafe_allow_html=True)

with st.expander("🐉 SIMULADOR DRAGÃO - Teste prático"):
    st.markdown('<div class="card-pop"><div class="titulo">Simulador</div>Teste fictício para entender mecânica de grade, taxa e lucro líquido.</div>', unsafe_allow_html=True)
    inv=st.slider("Valor fictício",5.0,50.0,20.0)
    grades=st.slider("Grades",4,20,8)
    st.caption(f"Cada grade: R$ {inv/grades:.2f} | Range exemplo: 288k a 312k | Taxa: 0,1% por operação")
    if st.button("Rodar simulação",type="primary",use_container_width=True):
        lt=0; tt=0
        for i in range(grades):
            pc=random.uniform(288000,299500); pv=pc*random.uniform(1.002,1.008)
            lb=(inv/grades)*(pv/pc-1); taxa=(inv/grades)*0.001*2; ll=lb-taxa
            lt+=ll; tt+=taxa
            st.write(f"Grade {i+1}: Compra R$ {pc:,.0f} → Venda R$ {pv:,.0f} | Bruto R$ {lb:.4f} - Taxa R$ {taxa:.4f} = Líquido R$ {ll:.4f}")
            time.sleep(0.12)
        st.success(f"Resultado: Bruto R$ {lt+tt:.2f} - Taxas R$ {tt:.2f} = Líquido R$ {lt:.2f} | Em cenário real, rompimento do intervalo pode deixar posição presa.")
        
st.markdown('<div class="legal">🐉 Trade Academy - Conteúdo educacional nos termos da Lei 9.394/96.<br>Não é recomendação de investimento. Criptoativo é renda variável de alto risco e você pode perder todo capital.<br>Não indicamos corretora específica. Não há promessa de rentabilidade.</div>', unsafe_allow_html=True)
