import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy DRAGAO", page_icon="🐉", layout="wide", initial_sidebar_state="expanded")

if "pagina" not in st.session_state:
    st.session_state.pagina = "INICIO"
if "xp" not in st.session_state:
    st.session_state.xp = 0

st.markdown("""
<style>
.stApp{background:#0f0707;color:#ffe9e9;}
.hero{
    background:radial-gradient(circle at top,#ff1a1a 0%,#8b0000 45%,#1a0505 100%);
    padding:42px 20px;border-radius:28px;text-align:center;
    border:2px solid #ff3333;box-shadow:0 0 35px #ff000088;
}
.card{
    background:#1f0f0f;padding:24px;border-radius:18px;
    border:1px solid #5a1a1a;margin-bottom:16px;
    line-height:2.0;font-size:15px;
}
.card-pop{
    background:linear-gradient(135deg,#3a1010 0%,#1a0808 100%);
    border:2px solid #ff4444;padding:24px;border-radius:18px;
    margin-bottom:16px;box-shadow:0 0 20px #ff000055;
}
.titulo{font-size:26px;font-weight:900;color:#ff6b6b;margin-bottom:8px;}
.dragao{
    background:#2a1212;border:2px dashed #ff4444;
    padding:16px;border-radius:16px;text-align:center;margin-bottom:12px;
}
.legal{font-size:11px;opacity:0.35;text-align:center;margin-top:40px;line-height:1.6;}
/* BOTAO VERMELHO FOGO */
.stButton > button{
    background:linear-gradient(135deg,#ff1a1a,#8b0000)!important;
    color:white!important;
    border:2px solid #ff9999!important;
    font-weight:900!important;
    font-size:14px!important;
    border-radius:14px!important;
    height:68px!important;
    box-shadow:0 4px 18px #ff000088!important;
    white-space:pre-line!important;
}
.stButton > button:hover{
    background:#ff4444!important;
    color:black!important;
    transform:scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR COM DRAGAO
with st.sidebar:
    st.markdown("""
    <div class="dragao">
        <div style="font-size:50px">🐉🔥</div>
        <b>Dragão de Fogo - seu tutor</b><br>
        <span style="font-size:13px">Grrrr! Eu cuspo fogo nos golpes e te ensino de verdade. Sem enrolação.</span>
    </div>
    """, unsafe_allow_html=True)
    st.progress(min(int(st.session_state.xp),100))
    st.caption(f"🔥 Poder de fogo: {st.session_state.xp} XP")
    st.markdown("### 🐉 NAVEGAÇÃO DRAGÃO")
    menu = st.radio("menu",["INICIO","CAP 1 - O que é Bitcoin","CAP 2 - Criar conta segura","CAP 3 - PIX e Carteiras","CAP 4 - Primeira compra","CAP 5 - GRID Básico","CAP 6 - GRID Avançado + Taxas","CAP 7 - Plano R$20","CAP 8 - Golpes e Riscos","CAP 10 - Criar seu app","SIMULADOR DRAGÃO"],label_visibility="collapsed")
    mapa={"INICIO":"INICIO","CAP 1 - O que é Bitcoin":"CAP1","CAP 2 - Criar conta segura":"CAP2","CAP 3 - PIX e Carteiras":"CAP3","CAP 4 - Primeira compra":"CAP4","CAP 5 - GRID Básico":"CAP5","CAP 6 - GRID Avançado + Taxas":"CAP6","CAP 7 - Plano R$20":"CAP7","CAP 8 - Golpes e Riscos":"CAP8","CAP 10 - Criar seu app":"CAP10","SIMULADOR DRAGÃO":"SIM"}
    if st.session_state.pagina!=mapa[menu]:
        st.session_state.pagina=mapa[menu];st.rerun()
    st.markdown('<div class="card"><b>🐉 Dragão fala:</b><br><span style="font-size:13px">GRID ganha quando fica quicando lateral. Fica preso quando dispara ou desaba. Por isso teste com pouco.</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="font-size:11px;opacity:0.7">Conteúdo educacional Lei 9.394/96. Não é recomendação investimento. Alto risco. Sem corretora específica.</div>', unsafe_allow_html=True)

# HERO VERMELHO
st.markdown("""
<div class="hero">
<h1>🐉🔥 TRADE ACADEMY DRAGÃO</h1>
<p><b>Versão Fogo - Conteúdo completo que já aparece embaixo, sem precisar rolar</b></p>
</div>
""", unsafe_allow_html=True)

st.write("")

# BOTOES VERMELHOS
c1,c2,c3,c4,c5=st.columns(5)
with c1:
    if st.button("CAP 1\nO que é BTC",use_container_width=True): st.session_state.pagina="CAP1";st.rerun()
with c2:
    if st.button("CAP 2\nConta segura",use_container_width=True): st.session_state.pagina="CAP2";st.rerun()
with c3:
    if st.button("CAP 3\nPIX",use_container_width=True): st.session_state.pagina="CAP3";st.rerun()
with c4:
    if st.button("CAP 4\n1a compra",use_container_width=True): st.session_state.pagina="CAP4";st.rerun()
with c5:
    if st.button("🐉 SIMULADOR\nFOGO",use_container_width=True): st.session_state.pagina="SIM";st.rerun()
c6,c7,c8,c9,c10=st.columns(5)
with c6:
    if st.button("CAP 5\nGRID básico",use_container_width=True): st.session_state.pagina="CAP5";st.rerun()
with c7:
    if st.button("CAP 6\nAvançado",use_container_width=True): st.session_state.pagina="CAP6";st.rerun()
with c8:
    if st.button("CAP 7\nPlano R$20",use_container_width=True): st.session_state.pagina="CAP7";st.rerun()
with c9:
    if st.button("CAP 8\nGolpes",use_container_width=True): st.session_state.pagina="CAP8";st.rerun()
with c10:
    if st.button("CAP 10\nCriar app",use_container_width=True): st.session_state.pagina="CAP10";st.rerun()

st.divider()
pag=st.session_state.pagina

if pag=="INICIO":
    st.markdown('<div class="card-pop"><div class="titulo">🐉🔥 Bem vindo ao Trade Academy Dragão</div>Curso prático com tema fogo vermelho.<br><br>✅ Já abre conteúdo embaixo do título, não precisa rolar até fim<br>✅ Dragão tutor na lateral (clica >> no canto superior esquerdo no celular)<br>✅ Sem nome de corretora, sem risco<br>✅ Simulador que explica GRADE, RANGE, TAXA, LÍQUIDO<br><br>Clica nos botões vermelhos acima pra começar. Cada CAP dá XP de fogo.</div>', unsafe_allow_html=True)

elif pag=="CAP1":
    st.markdown('<div class="titulo">🐉 CAP 1 - O que é Bitcoin de verdade</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">2008 crise bancos, governo imprimiu trilhões. Nasce Bitcoin: dinheiro que ninguém pode imprimir à vontade.<br><br>Dinheiro é confiança. Real vale porque Brasil aceita. BTC vale porque milhões no mundo aceitam e só existe 21 milhões.<br><br>Blockchain: caderno público copiado em 20 mil PCs. Se um tenta mentir, outros 19.999 negam.<br><br>Volátil: cai 15% sobe 20% no dia. Quebra emocional.<br><br>Foca BTC e ETH início porque antigos, menos golpe. Moedinha nova prometendo 1000% = 99% golpe.<br><br>🐉 Ouro digital escasso. Dragão guarda, não deixa imprimir mais.</div>', unsafe_allow_html=True)

elif pag=="CAP2":
    st.markdown('<div class="titulo">🐉 CAP 2 - Criar conta segura (SEM MARCA)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">1. Escolhe corretora grande regulamentada, confere https domínio oficial, nunca link Telegram.<br>2. E-mail + senha 12 caracteres com maiúscula número símbolo.<br>3. Código e-mail.<br>4. KYC nome igual RG foto sem flash.<br>5. Selfie com RG + papel nome corretora + data.<br>6. Ativa 2FA Google Authenticator guarda código em PAPEL.<br><br>🐉 Dragão: Corretora séria NUNCA pede senha ou 2FA. Se pedir é golpe, cospe fogo e bloqueia.</div>', unsafe_allow_html=True)

elif pag=="CAP3":
    st.markdown('<div class="titulo">🐉 CAP 3 - PIX e Carteiras</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Spot = bolso principal seguro. Carteira depósito = onde cai PIX depois transfere Spot.<br><br>PIX genérico: Corretora > Depositar > BRL > PIX > copia chave > seu banco PIX R$10 teste > 1-3 min cai > Transferir pra Spot.<br><br>CPF banco = CPF corretora mesmo titular.<br><br>🐉 R$10 teste pra ver se cai certo, sem queimar dinheiro.</div>', unsafe_allow_html=True)

elif pag=="CAP4":
    st.markdown('<div class="titulo">🐉 CAP 4 - Primeira compra</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Trade > Spot > BTC/BRL > Mercado > Total 10 > Comprar. Ver fração em Spot. Deixa quieto olha 3h em 3h anota caderno. Primeira compra é pra perder medo. R$10 é aula paga. Não compra moeda que subiu 80% hoje (FOMO).<br><br>🐉 Primeira labareda é pra aprender, não pra queimar tudo.</div>', unsafe_allow_html=True)

elif pag=="CAP5":
    st.markdown('<div class="titulo">🐉 CAP 5 - GRID Básico - Feira automática</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-pop">Feira: maçã R$5 compra R$4,90 vende R$5,10 lucro R$0,20 faz 50x=R$10. GRID faz com BTC automático.<br><br>Você fala: compra 299k vende 300k. Cria ordens entre e trabalha sozinho.<br><br>Ganha lateral quicando. Perde se sobe forte sai por cima (vende tudo perde alta) ou cai forte sai por baixo (compra tudo fica preso no preju até voltar meses).<br><br>🐉 Dragão ganha pouco sempre, não fica rico rápido. Quem promete 10% ao dia mente.</div>', unsafe_allow_html=True)

elif pag=="CAP6":
    st.markdown('<div class="titulo">🐉 CAP 6 - Avançado + Taxas</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">Config R$20: inferior -4% superior +4% 8-10 grades R$2 por grade aritmético.<br><br>TAXA média 0,1% cada operação. Compra R$10 paga R$0,01 vende R$0,01 total R$0,02. 20 ciclos=R$0,40 taxa. Lucro R$0,04x20=R$0,80 bruto -0,40=0,40 líquido. Grade muito pequena taxa come tudo.<br><br>Genérico: Bots > Spot Grid > Criar > inferior 288k superior 312k 10 grades R$20<br><br>🐉 Dragão: Lucro sem taxa é mentira. Fogo consome taxa sempre.</div>', unsafe_allow_html=True)

elif pag=="CAP7":
    st.markdown('<div class="titulo">🐉 CAP 7 - Plano 7 dias R$20</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-pop">R$20/10=R$2 grade R$0,04x8=R$0,32 dia ~R$9,60 mês lateral perfeito. Não é R$200.<br><br>Dia1 conta 2FA Dia2 entende PIX sem depositar roda simulador Dia3 deposita R$20 compra R$10 BTC Dia4 GRID R$10 -3%+3% 5 grades Dia5 olha taxas Dia6 decide mais R$10 ou para Dia7 anota.<br><br>REGRA: nunca dinheiro aluguel comida emprestado. Só que se perder não te quebra.<br><br>🐉 R$20 é primeira chama, não incêndio.</div>', unsafe_allow_html=True)

elif pag=="CAP8":
    st.markdown('<div class="titulo">🐉 CAP 8 - Golpes e Riscos Reais</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">1 Dobrar BTC WhatsApp GOLPE 2 Print lucro falso esconde perda 3 GRID não mágico cai 30% fica preso meses 4 FUTURES 125x liquida 2s NÃO CLICA fica SPOT 5 Anota caderno físico 6 Ansioso desliga app 7 Imposto acima R$35k mês 15% 8 Não empresta conta CPF seu.<br><br>🐉🔥 Se é bom demais pra ser verdade, dragão cospe fogo e queima. É golpe.</div>', unsafe_allow_html=True)

elif pag=="CAP10":
    st.markdown('<div class="titulo">🐉 CAP 10 - BÔNUS Criar seu app e vender R$20</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-pop">Streamlit+GitHub+Cloud grátis. Copia código troca textos seu nicho. Cobrar: Mercado Pago Kiwify R$20 PIX verifica e-mail via API ou manual. Divulga TikTok mostrando simulador R$7,81 explicando GRADE TAXA.<br><br>Obrigatório aviso: Conteúdo educacional Lei 9.394/96. Não é recomendação investimento, não é promessa rentabilidade. Cripto alto risco pode perder tudo. Não indicamos corretora específica.<br><br>🐉 Vende conhecimento não promessa. Promessa dá processo e dragão te queima.</div>', unsafe_allow_html=True)

elif pag=="SIM":
    st.markdown('<div class="titulo">🐉🔥 SIMULADOR DRAGÃO QUE ENSINA</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-pop">Simulador refeito: já mostra tudo embaixo, explica cada termo com fogo.</div>', unsafe_allow_html=True)
    inv=st.slider("Valor fictício (mentira) 🔥",5.0,50.0,7.81)
    grades=st.slider("Grades (garras do dragão) 🐉",4,20,8)
    st.markdown(f'<div class="card"><b>📖 Glossário Dragão:</b><br><b>GRADE:</b> divisão dinheiro R${inv:.2f}/{grades}=R${inv/grades:.2f} cada - cada garra compra e vende<br><b>RANGE:</b> intervalo que dragão vigia 288k-312k<br><b>TAXA:</b> ~0,1% fogo que corretora queima cada operação<br><b>LÍQUIDO:</b> bruto - taxas - o que sobra pro dragão<br><b>LATERAL:</b> indo e voltando melhor pro GRID<br><b>PRESO:</b> caiu muito comprou tudo ficou prejuízo</div>', unsafe_allow_html=True)
    if st.button("🔥🐉 RODAR FOGO DO DRAGÃO - CLICA",type="primary",use_container_width=True):
        barra=st.progress(0); lt=0; tt=0
        for i in range(grades):
            pc=random.uniform(288000,299500); pv=pc*random.uniform(1.002,1.008)
            lb=(inv/grades)*(pv/pc-1); taxa=(inv/grades)*0.001*2; ll=lb-taxa
            lt+=ll; tt+=taxa; barra.progress(int((i+1)/grades*100))
            st.write(f"🔥 GARRA {i+1}: Dragão comprou R$ {pc:,.0f} (FUNDO) -> Cuspiu fogo e vendeu R$ {pv:,.0f} (TOPO) | Bruto R$ {lb:.4f} - Taxa queimada R$ {taxa:.4f} = Líquido R$ {ll:.4f} | Se caísse pra 250k dragão ficaria PRESO na caverna.")
            time.sleep(0.15)
        st.balloons()
        st.success(f"🐉🔥 FOGO FINAL: Bruto R$ {lt+tt:.2f} - Taxas queimadas R$ {tt:.2f} = Líquido R$ {lt:.2f}")
        st.markdown('<div class="card-pop">🐉 Dragão explica: Cada garra comprou barato fundo vendeu caro topo. Taxa queimou parte. Se RANGE rompido pra 350k vendia tudo e perdia alta. Se fosse pra 250k ficava preso na caverna meses. Não é garantia lucro real, é aula de fogo.</div>', unsafe_allow_html=True)

st.markdown('<div class="legal">🐉🔥 Trade Academy DRAGÃO - Vermelho fogo. Conteúdo educacional Lei 9.394/96. Não é recomendação investimento. Alto risco pode perder tudo. Sem marca. Sem promessa.</div>', unsafe_allow_html=True)
