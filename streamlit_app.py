import streamlit as st, random, time

st.set_page_config(page_title="Trade Academy - Escola Completa", page_icon="💜", layout="wide")

st.markdown("""
<style>
.stApp{background:#0b0a12;color:#e8e8e8;}
.hero{background:radial-gradient(circle at top,#7c3aed 0%,#1a1625 55%,#0b0a12 100%);padding:50px 25px;border-radius:28px;text-align:center;border:2px solid #7c3aed;box-shadow:0 0 50px rgba(124,58,237,0.5);}
.card{background:linear-gradient(135deg,#1e1b2e 0%,#15131f 100%);padding:28px;border-radius:20px;border:1px solid #3a3450;margin-bottom:18px;line-height:2.0;font-size:15px;}
.card-pop{background:linear-gradient(135deg,#2a1f4a 0%,#1e1b2e 100%);border:2px solid #a78bfa;padding:28px;border-radius:22px;margin-bottom:18px;box-shadow:0 0 30px rgba(167,139,250,0.3);}
.titulo{font-size:26px;font-weight:900;color:#d8b4fe;margin-bottom:12px;}
.sub{font-size:18px;font-weight:800;color:#a78bfa;margin-top:20px;margin-bottom:8px;}
.badge{display:inline-block;background:#7c3aed;color:white;padding:5px 14px;border-radius:20px;font-size:11px;font-weight:800;margin-bottom:10px;}
.badge-green{background:#22c55e;}
.badge-gold{background:#eab308;color:black;}
.legal{font-size:11px;opacity:0.4;margin-top:50px;text-align:center;}
</style>
""", unsafe_allow_html=True)

# MENU EM CAPÍTULOS ORGANIZADOS
menu = st.sidebar.radio("📚 ESCOLA - CAPÍTULOS EM ORDEM", [
"💜 CAP 0 - INÍCIO - COMEÇA AQUI",
"🎮 CAP 0.5 - SIMULADOR R$7,81",
"📘 CAP 1 - O QUE É DINHEIRO E BITCOIN",
"📗 CAP 2 - CRIANDO CONTA NA CORRETORA",
"📙 CAP 3 - COLOCANDO R$20 VIA PIX",
"📕 CAP 4 - COMPRANDO BITCOIN PELA 1ª VEZ",
"🤖 CAP 5 - GRID BÁSICO - FEIRA DA MAÇÃ",
"⚙️ CAP 6 - GRID AVANÇADO E TAXAS REAIS",
"💸 CAP 7 - TENHO SÓ R$20 - PLANO 7 DIAS",
"🛡️ CAP 8 - GOLPES, RISCOS E PSICOLOGIA",
"📖 CAP 9 - GLOSSÁRIO E CHECKLIST FINAL",
"🚀 CAP 10 - BÔNUS - CRIE SEU PRÓPRIO APP"
])

if menu=="💜 CAP 0 - INÍCIO - COMEÇA AQUI":
    st.markdown("""
    <div class="hero">
    <h1 style="font-size:46px;">💜 TRADE ACADEMY - ESCOLA COMPLETA</h1>
    <p style="font-size:18px;">Do zero absoluto até criar seu próprio app. 10 capítulos, sem pular, sem misturar.<br>Cada capítulo é uma pasta separada, com tudo no seu lugar.</p>
    <span style="background:#22c55e;color:white;padding:8px 18px;border-radius:20px;font-weight:900;">🟢 TESTE ABERTO - TUDO LIBERADO POR ENQUANTO</span>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card-pop">
        <span class="badge">FASE 1 - BASE</span>
        <div class="titulo">📚 Cap 1 ao 4 - Fundação</div>
        Cap 1: O que é Bitcoin<br>
        Cap 2: Criar conta na Binance<br>
        Cap 3: Colocar R$20 via Pix<br>
        Cap 4: Comprar BTC pela 1ª vez<br>
        <b>Objetivo: perder o medo de clicar</b>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card-pop">
        <span class="badge badge-green">FASE 2 - ROBÔ</span>
        <div class="titulo">🤖 Cap 5 ao 7 - GRID</div>
        Cap 5: GRID básico feira<br>
        Cap 6: GRID avançado e taxas<br>
        Cap 7: Plano 7 dias com R$20<br>
        <b>Objetivo: entender quando ganha e perde</b>
        </div>
        """, unsafe_allow_html=True)
    c3,c4 = st.columns(2)
    with c3:
        st.markdown("""
        <div class="card-pop">
        <span class="badge" style="background:#ef4444;">FASE 3 - PROTEÇÃO</span>
        <div class="titulo">🛡️ Cap 8 ao 9 - Não quebrar</div>
        Cap 8: Golpes e psicologia<br>
        Cap 9: Glossário e checklist<br>
        <b>Objetivo: não cair em golpe e não quebrar</b>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="card-pop">
        <span class="badge badge-gold">FASE 4 - BÔNUS</span>
        <div class="titulo">🚀 Cap 10 - Crie seu app</div>
        Como criar um app igual esse no Streamlit<br>
        Como colocar no ar de graça<br>
        Como vender por R$20 igual você<br>
        <b>Objetivo: transformar aprendizado em renda</b>
        </div>
        """, unsafe_allow_html=True)
    st.progress(5, text="Progresso: Cap 0 de 10 - Bora pro Cap 1 💜")

elif menu=="📘 CAP 1 - O QUE É DINHEIRO E BITCOIN":
    st.markdown('<div class="card-pop"><span class="badge">CAP 1 - FUNDAMENTO</span><div class="titulo">📘 Cap 1 - O que é dinheiro e Bitcoin sem enrolação</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">💵 O que é dinheiro de verdade:</div>
    Dinheiro é confiança. Real vale porque todo mundo no Brasil aceita. Dólar vale porque mundo todo aceita. Bitcoin vale porque milhões de pessoas no mundo aceitam pagar por ele. Só que real o governo pode imprimir quanto quiser. Bitcoin não, só vai ter 21 milhões no mundo, nunca mais. Por isso quando muita gente quer comprar, preço sobe. Quando muita gente quer vender, preço cai.<br><br>
    <div class="sub">⛓️ O que é Blockchain (caderno público):</div>
    É um caderno gigante onde anota: João mandou 0,1 BTC pra Maria às 14h32. Esse caderno fica copiado em milhares de computadores no mundo. Ninguém consegue apagar uma página sozinho porque os outros milhares têm cópia. É por isso que dizem que é seguro, mas não é 100% à prova de golpe em corretora, por isso cuidado onde deixa.<br><br>
    <div class="sub">🪙 Bitcoin vs Altcoins:</div>
    Bitcoin foi o primeiro (2009), mais famoso e mais estável entre as criptos. Altcoins são as outras: Ethereum (ETH), Solana, etc. Pra começar, foca só em BTC e ETH, que são mais estáveis. Moedinha pequena tipo SHIB, DOGE sobe e desce 20% por dia e deixa iniciante maluco.<br><br>
    <div class="sub">📈 Por que sobe e desce tanto:</div>
    Porque é oferta e demanda 24h por dia, sem pausa. Sai notícia boa (ex: empresa grande comprou Bitcoin) sobe 10%. Sai notícia ruim (ex: governo proibiu) cai 15%. É volátil, mais que bolsa. Por isso com R$20 objetivo não é ficar rico, é aprender a lidar com volatilidade sem pânico.<br><br>
    <b>✅ Tarefa do Cap 1:</b> Assiste 1 vídeo no YouTube de 10 min sobre o que é Bitcoin, só pra ouvir outra explicação. Não precisa comprar nada hoje.
    </div>
    """, unsafe_allow_html=True)

elif menu=="📗 CAP 2 - CRIANDO CONTA NA CORRETORA":
    st.markdown('<div class="card-pop"><span class="badge">CAP 2 - PRÁTICA</span><div class="titulo">📗 Cap 2 - Criando conta na Binance passo a passo</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">🏦 O que é corretora:</div>
    É onde você troca reais por Bitcoin, igual casa de câmbio troca real por dólar. Binance é a maior do mundo, existe desde 2017. Você manda Pix em reais pra lá e lá dentro troca por Bitcoin. Ela ganha taxa de cada troca.<br><br>
    <div class="sub">📱 Passo a passo pra criar conta (10 min):</div>
    1. Abre Google, digita binance.com, confere se é binance.com oficial, sem letra a mais.<br>
    2. Clica em REGISTRAR amarelo no topo.<br>
    3. E-mail que usa mesmo + senha forte com maiúscula, minúscula, número e símbolo. Anota num caderno.<br>
    4. Vai no Gmail, abre e-mail da Binance, clica em Confirmar.<br>
    5. Nome completo igual RG, CPF sem traço, data nascimento, endereço igual conta de luz.<br>
    6. KYC: foto do RG frente nítida sem flash em cima de mesa escura, foto verso, selfie segurando RG + folha escrita à mão Binance + data de hoje (ex: Binance 12/10/2026). Luz boa perto da janela.<br>
    7. Envia e espera 5-15 min, chega e-mail Aprovado. Se reprovar, tira foto melhor.<br>
    8. Ativa 2FA: baixa Google Authenticator, escaneia QR Code da Binance, anota código de 16 letras que aparece, guarda.<br>
    9. Cuidado: nunca clica em link de e-mail que parece Binance mas é binance-suporte.com (falso). Sempre digita binance.com no navegador.<br><br>
    <div class="sub">🔒 Segurança depois de criar:</div>
    Ativa verificação por e-mail, celular e Google Authenticator. Usa senha diferente de outros sites. Não empresta conta pra amigo, se ele fizer coisa errada responde seu CPF.<br><br>
    <b>✅ Tarefa do Cap 2:</b> Cria conta hoje, faz KYC, ativa 2FA. Não coloca dinheiro ainda. Tira print de cada tela e guarda numa pasta Binance no celular.
    </div>
    """, unsafe_allow_html=True)

elif menu=="📙 CAP 3 - COLOCANDO R$20 VIA PIX":
    st.markdown('<div class="card-pop"><span class="badge">CAP 3 - DINHEIRO</span><div class="titulo">📙 Cap 3 - Colocando R$20 via Pix sem medo</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">💸 Como colocar dinheiro via Pix (3 min):</div>
    1. Dentro da Binance app: embaixo clica Carteira > Depositar > Fiat > BRL > Pix.<br>
    2. Aparece chave Pix aleatória tipo 123e4567 ou QR Code. Clica Copiar chave.<br>
    3. Abre seu banco: Nubank, Inter, Caixa, Bradesco. Vai em Pix > Pix copia e cola > Cola chave > Valor R$20 > Confirma com senha.<br>
    4. Volta na Binance, espera 1-3 min, puxa pra atualizar. Vai em Carteira > Spot > deve aparecer BRL R$20,00.<br>
    5. Se não cair em 10 min, pega comprovante do Pix com ID da transação e abre chat Suporte: Perfil > Suporte > Chat, manda comprovante.<br>
    6. Dica de ouro: faz Pix de R$10 primeiro pra testar, depois mais R$10. Se errar chave perde pouco.<br><br>
    <div class="sub">👀 Onde fica seu dinheiro e o que é Spot:</div>
    Em Carteira > Spot. Spot = à vista, dinheiro disponível agora, sem empréstimo, sem alavancagem, mais seguro pra iniciante. Lá mostra BRL R$20 e BTC 0. Quando comprar Bitcoin, mostra BTC 0,00003 e BRL diminui. NÃO clica por enquanto em Earn, Futures, Margin, Launchpad. Só Spot.<br><br>
    <div class="sub">🏧 Como sacar depois:</div>
    Carteira > Spot > vende BTC pra BRL > Sacar > Fiat > BRL > Pix > coloca chave Pix do seu banco > confirma. Pix de saque cai em 1-5 min normalmente.<br><br>
    <b>✅ Tarefa do Cap 3:</b> Deposita R$20 hoje e só olha em Carteira Spot. Não compra nada. Acostuma ver R$20 lá. Vê como se sente: ansioso ou tranquilo? Anota.
    </div>
    """, unsafe_allow_html=True)

elif menu=="📕 CAP 4 - COMPRANDO BITCOIN PELA 1ª VEZ":
    st.markdown('<div class="card-pop"><span class="badge">CAP 4 - PRIMEIRA COMPRA</span><div class="titulo">📕 Cap 4 - Comprando Bitcoin pela primeira vez</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">🛒 Passo a passo pra comprar primeira vez (2 min):</div>
    1. Vai em Trade > Spot > no topo escolhe par BTC/BRL (Bitcoin em reais).<br>
    2. No meio tem Comprar e Vender. Clica Comprar > Mercado (Market) que compra na hora pelo preço atual.<br>
    3. Em Total digita R$10 > Clica Comprar BTC.<br>
    4. Pronto. Agora em Carteira Spot você tem BTC 0,000033 e BRL R$10.<br>
    5. Deixa quieto. Olha de 3 em 3 horas como seu BTC sobe e desce em reais. Anota num caderno: 9h R$10,12 / 12h R$9,98 / 18h R$10,05 / 21h R$10,20. Acostuma com oscilação sem pânico.<br><br>
    <div class="sub">📊 Mercado vs Limite:</div>
    Mercado compra na hora pelo preço atual, mais fácil pra iniciante. Limite você coloca preço que quer comprar (ex: quero comprar BTC quando cair pra 290k). Começa com Mercado, depois aprende Limite.<br><br>
    <div class="sub">❓ Dúvidas que todo mundo tem:</div>
    - Mínimo? R$10 por operação.<br>
    - Imposto? Só se vender mais de R$35 mil no mês.<br>
    - Pode perder tudo no Spot? Só se Bitcoin for a zero, nunca foi em 15 anos, mas já caiu 80% e demorou 2 anos pra voltar.<br>
    - É seguro deixar na Binance? Maior do mundo, mas no futuro aprende carteira fria Ledger. Por enquanto R$20 pode deixar lá.<br><br>
    <b>✅ Tarefa do Cap 4:</b> Compra R$10 de BTC e deixa R$10 em BRL. Olha 1 dia inteiro oscilando. Anota.
    </div>
    """, unsafe_allow_html=True)

elif menu=="🤖 CAP 5 - GRID BÁSICO - FEIRA DA MAÇÃ":
    st.markdown('<div class="card-pop"><span class="badge">CAP 5 - ROBÔ</span><div class="titulo">🤖 Cap 5 - GRID básico - feira da maçã</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>🍎 Feira:</b> Maçã tá R$5. Você fala: compro a R$4,90 10 maçãs, vendo a R$5,10. Se ficar indo e voltando entre R$4,90 e R$5,10 o dia todo, compra e vende várias vezes e ganha R$0,20 cada vez. 10 idas e vindas = R$2. GRID faz isso com Bitcoin automático.<br><br>
    <b>Exemplo Bitcoin R$300k:</b> Você diz: trabalha entre R$285k e R$315k, 10 grades. Cria ordens compra 286.5k, 289.5k, 292.5k... venda 301.5k, 304.5k, 307.5k... Cai pra 289.5k compra, sobe pra 292.5k vende com lucro R$3k de diferença, mas com R$20 seu lucro é centavos porque grade tem R$2.<br><br>
    <div class="sub">📈 Quando GANHA?</div>
    Quando mercado fica lateral, quicando. Ex: 3 dias entre 295k e 305k, sobe e desce. GRID faz 30-40 trades de R$0,10, junta R$3 no dia. Chato, devagar, não é 10% ao dia.<br><br>
    <div class="sub">📉 Quando PERDE?</div>
    1. Alta forte pra 350k: vendeu tudo em 315k e perdeu alta de 315k até 350k.<br>
    2. Baixa forte pra 200k: comprou tudo e fica preso no prejuízo 30% até voltar, pode demorar meses.<br>
    3. Taxa come lucro se colocar muitas grades.<br><br>
    <b>✅ Tarefa do Cap 5:</b> Roda simulador aqui do app 3 vezes com R$7,81 e vê quicando. Só depois coloca dinheiro real.
    </div>
    """, unsafe_allow_html=True)

elif menu=="⚙️ CAP 6 - GRID AVANÇADO E TAXAS REAIS":
    st.markdown('<div class="card-pop"><span class="badge">CAP 6 - AVANÇADO</span><div class="titulo">⚙️ Cap 6 - GRID avançado e taxas reais</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">⚙️ Configuração exata pra R$20 - copia igual:</div>
    Par: BTC/BRL<br>
    Inferior: preço atual -4% (se BTC 300k, inferior 288k)<br>
    Superior: preço atual +4% (superior 312k)<br>
    Grades: 8 a 10 grades (não 50 senão taxa come)<br>
    Modo: Aritmético (divide igual)<br>
    Investimento: R$20 total / 10 grades = R$2 por grade<br>
    Stop loss: NÃO coloca por enquanto<br><br>
    <div class="sub">💰 Taxa real - faz conta comigo:</div>
    Binance cobra 0,1% por operação pra quem tem pouco. Compra R$10 paga R$0,01. Vende R$10 paga R$0,01. Ciclo compra+venda = R$0,02. 20 ciclos/dia = R$0,40 taxa. Se lucro bruto R$1/dia, lucro líquido R$0,60. Se tem BNB e ativa pagar taxa com BNB, taxa cai pra 0,075%, economiza 25%. Muita gente acha que lucrou R$10 no mês mas pagou R$12 taxa, perdeu R$2.<br><br>
    <div class="sub">📍 Onde clica na Binance pra criar GRID:</div>
    1. App Binance > Trade > Bots > Trading Bots<br>
    2. Spot Grid > Criar<br>
    3. Par BTC/BRL<br>
    4. Inferior 288000, Superior 312000, Grades 10<br>
    5. Investimento R$20 > Criar. Tira print antes de criar e me manda no gatinho que confiro.<br>
    6. Depois aparece em Bots > Em execução. Mostra operações, lucro, taxa.<br><br>
    <b>✅ Tarefa do Cap 6:</b> Cria seu primeiro GRID de R$20 com config acima. Deixa 24h ligado.
    </div>
    """, unsafe_allow_html=True)

elif menu=="💸 CAP 7 - TENHO SÓ R$20 - PLANO 7 DIAS":
    st.markdown('<div class="card-pop"><span class="badge badge-green">CAP 7 - PLANO</span><div class="titulo">💸 Cap 7 - Tenho só R$20 - plano 7 dias real</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <b>Conta real sem mentira:</b> R$20 /10 grades = R$2 por grade. Lucro R$0,04 por trade x 8 trades/dia = R$0,32/dia. 30 dias = R$9,60. Tem dia zero, tem dia R$0,50. Não é todo dia igual.<br><br>
    <div class="sub">🗓️ Plano dia a dia:</div>
    Dia 1: Cria conta, KYC, 2FA, sem dinheiro, tira print, guarda pasta Binance.<br>
    Dia 2: Deposita R$20 Pix, só olha em Spot, não compra, vê como se sente, anota.<br>
    Dia 3: Compra R$10 BTC Spot e deixa R$10 BRL, olha de 3 em 3h subir e descer, anota 9h R$10,12 /12h R$9,98 /18h R$10,05.<br>
    Dia 4: Cria GRID R$10, -3% a +3%, 5 grades, deixa 24h, não olha toda hora.<br>
    Dia 5: Vê quantas operações fez, taxa paga, lucro/prejuízo, tira print Bots > Em execução.<br>
    Dia 6: Se gostou coloca mais R$10 no mesmo GRID ou cria outro ETH/BRL. Se não gostou clica Parar GRID e vende tudo pra BRL.<br>
    Dia 7: Anota tudo: entrou R$20, hoje tem X, taxa Y, lucro Z, como me senti (ansioso? calmo?).<br><br>
    <div class="sub">🚨 Regra de ouro:</div>
    Nunca dinheiro do aluguel, luz, comida, remédio, emprestado, cartão crédito, limite banco. Só o que se perder dorme tranquilo. R$20 é escola, não é pra pagar boleto.<br><br>
    <div class="sub">❌ Erro que quebra 90% iniciantes:</div>
    Ver R$0,32 e achar pouco, colocar R$500 que não tem e perder R$50 dia 1 e falar que cripto é golpe. Ou ver R$0,32 e achar muito e colocar R$5000 emprestado e quebrar. Vai devagar. R$20 é escola. Escola paga pra aprender.<br><br>
    <b>✅ Tarefa Cap 7:</b> Segue plano 7 dias sem pular. Cria planilha Data | Coloquei | Tenho hoje | Taxa | Lucro | Como me senti.
    </div>
    """, unsafe_allow_html=True)

elif menu=="🛡️ CAP 8 - GOLPES, RISCOS E PSICOLOGIA":
    st.markdown('<div class="card-pop"><span class="badge" style="background:#ef4444;">CAP 8 - PROTEÇÃO</span><div class="titulo">🛡️ Cap 8 - Golpes, riscos e psicologia - salva seu dinheiro</div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    1. <b>Golpe WhatsApp/Instagram/Telegram:</b> "Sou da Binance, me manda R$100 te devolvo R$1000 em 1h". Golpe 100%. Binance NUNCA chama no WhatsApp. Retorno fixo alto = golpe. Bloqueia.<br><br>
    2. <b>Print lucro falso:</b> "Fiz R$5 mil hoje". Com quanto? Com R$100 mil fez 5%. Com R$20 precisaria 25.000%, impossível. Print sem contexto é demo ou alavancagem que quebra depois.<br><br>
    3. <b>GRID não é mágico:</b> Se cair 30% num dia (maio 2022 caiu 40k pra 28k), GRID compra na queda e fica preso prejuízo 30% até voltar, pode demorar meses. Só usa dinheiro que aguenta ficar preso.<br><br>
    4. <b>NÃO clica Futures 125x:</b> Com R$20 opera R$2.500. Cai 1% perde tudo em 2 seg. Cassino, não investimento. Fica só Spot.<br><br>
    5. <b>Anota tudo:</b> Data | Coloquei | Tenho hoje | Taxa | Lucro | Como me senti. Sem anotar cérebro engana, acha que ganhou mas perdeu de taxa.<br><br>
    6. <b>Saúde mental:</b> Se fica olhando gráfico 5 em 5 min, coração acelerado, sem dormir, desliga. GRID é chato e devagar, igual plantar feijão. Se tá emocionante demais, tá errado, muito dinheiro ou alavancagem.<br><br>
    7. <b>Imposto:</b> Vendeu mais de R$35 mil no mês paga 15% sobre lucro. Com R$20 não precisa agora, mas guarda comprovante pasta Gmail Imposto Cripto.<br><br>
    8. <b>Não empresta conta:</b> Amigo usar sua conta e fazer coisa errada, responde seu CPF.<br><br>
    9. <b>Senha e segurança:</b> Senha forte, 2FA Google Authenticator, não clica link e-mail binance-suporte.com falso, sempre digita binance.com.<br><br>
    <b>✅ Tarefa Cap 8:</b> Lê 2 vezes. Salva nos favoritos. Quando alguém te chamar no WhatsApp com promessa, volta aqui e lê de novo.
    </div>
    """, unsafe_allow_html=True)

elif menu=="📖 CAP 9 - GLOSSÁRIO E CHECKLIST FINAL":
    st.markdown("""
    <div class="card">
    <div class="titulo">📖 Cap 9 - Glossário e Checklist final antes de operar</div>
    <div class="sub">📖 Glossário - palavras que vai ver:</div>
    BTC: Bitcoin. ETH: Ethereum. USDT/BRL: dólar ou real digital. Spot: compra à vista sem empréstimo, seguro. Futures: futuro com alavancagem, perde tudo rápido, NÃO usa. GRID: robô compra barato vende caro automático. Grade: cada degrau do GRID. Taxa/Fee: corretora cobra 0,1% por trade. KYC: verificação RG selfie. 2FA: segundo fator código 30 seg. Carteira/Wallet: onde fica dinheiro. HODL: segurar muito tempo. FOMO: medo ficar de fora compra no topo por ansiedade. FUD: medo incerteza dúvida vende no fundo por pânico.<br><br>
    <div class="sub">✅ Checklist antes de colocar R$20 real:</div>
    [ ] Criei conta Binance e fui aprovado KYC<br>
    [ ] Ativei 2FA Google Authenticator<br>
    [ ] Depositei R$10 Pix e vi cair em Spot<br>
    [ ] Rodei simulador 3 vezes e entendi quicando<br>
    [ ] Comprei R$10 BTC Spot e vi subir e descer 1 dia<br>
    [ ] Li aula golpes e sei que ninguém da Binance chama WhatsApp<br>
    [ ] Criei caderno ou planilha pra anotar tudo<br>
    [ ] Sei que com R$20 objetivo é aprender não ficar rico<br>
    [ ] Prometo não clicar Futures 125x<br>
    [ ] Prometo não colocar dinheiro do aluguel<br><br>
    Se marcou tudo, pode criar primeiro GRID R$20. Se não marcou, volta no capítulo que falta.
    </div>
    """, unsafe_allow_html=True)

elif menu=="🚀 CAP 10 - BÔNUS - CRIE SEU PRÓPRIO APP":
    st.markdown('<div class="card-pop"><span class="badge badge-gold">CAP 10 - BÔNUS PREMIUM</span><div class="titulo">🚀 Cap 10 - Como criar seu próprio app igual esse e vender por R$20</div>Esse capítulo só libera depois que aprendeu tudo. É aqui que você transforma aprendizado em renda.</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <div class="sub">💡 Ideia:</div>
    Você aprendeu cripto do zero ao GRID. Muita gente quer aprender igual. Você pode criar um app igual esse e vender acesso por R$20, R$30, R$50. Foi assim que esse app foi feito.<br><br>
    <div class="sub">🛠️ Passo 1 - Ferramentas gratuitas:</div>
    1. Streamlit: site que transforma código Python em app bonito. É de graça.<br>
    2. GitHub: site que guarda seu código. É de graça.<br>
    3. Streamlit Cloud: coloca seu app no ar de graça, com link tipo seuapp.streamlit.app.<br><br>
    <div class="sub">💻 Passo 2 - Código base:</div>
    Você não precisa saber programar muito. Copia código desse app, troca textos, cores, capítulos. O código é Python com st.markdown e st.sidebar.radio. Cada capítulo é um if menu == "CAP X".<br><br>
    <div class="sub">🎨 Passo 3 - Deixar chamativo:</div>
    Usa CSS que já tá nesse app: hero com gradiente roxo, card-pop com borda, badge colorido. Troca emoji, título, cor. Quanto mais chamativo, mais pessoa fica e lê.<br><br>
    <div class="sub">💰 Passo 4 - Como cobrar R$20 (igual você vai fazer depois):</div>
    1. Cria link de pagamento no Mercado Pago: R$20, Pix.<br>
    2. No código, coloca verificação: pessoa paga, depois digita e-mail usado no Pix, seu app confere se pagamento foi aprovado via API do Mercado Pago.<br>
    3. Se aprovado, libera conteúdo. Se não, mostra botão pagar.<br>
    4. Token do Mercado Pago fica em Secrets do Streamlit, ninguém vê.<br><br>
    <div class="sub">📣 Passo 5 - Como divulgar:</div>
    Faz vídeo curto no TikTok/Reels mostrando simulador R$7,81, fala "aprendi com R$20". Mostra checklist, mostra plano 7 dias. Não promete ficar rico, promete ensinar sem quebrar. Isso vende mais que promessa falsa.<br><br>
    <div class="sub">📚 O que ensinar no seu app:</div>
    Copia estrutura de capítulos desse app, mas com sua história. Cap 1 o que é Bitcoin com suas palavras, Cap 2 como criou conta, etc. Quanto mais pessoal e didático, mais vende.<br><br>
    <div class="sub">🔒 Legal:</div>
    Sempre coloca aviso: Conteúdo educacional livre Lei 9.394/96. Não é recomendação de investimento, não é consultoria CVM. Cripto tem alto risco. Sem promessa de lucro. Isso te protege.<br><br>
    <b>✅ Tarefa Cap 10:</b> Depois de 30 dias usando GRID com R$20, grava sua tela mostrando app, mostra seu aprendizado, cria seu próprio app com sua cara. Aí sim ativa pagamento de R$20 nesse app aqui.<br><br>
    <span class="badge badge-gold">Esse capítulo é o motivo do app valer R$20. Você não compra só curso de GRID, compra modelo de negócio pra criar seu próprio app.</span>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown('<div class="card-pop"><span class="badge">SIMULADOR</span><div class="titulo">🎮 Cap 0.5 - Simulador R$7,81 - treina sem dinheiro real</div></div>', unsafe_allow_html=True)
    c1,c2 = st.columns([1][2])
    with c1:
        inv=st.slider("💰 Valor fictício", 5.0, 50.0, 7.81)
        st.metric("Fictício", f"R$ {inv:.2f}", "+R$ 0,32 hoje")
        st.progress(60, text="Mercado lateral - GRID feliz")
    with c2:
        if st.button("🚀 RODAR SIMULAÇÃO AGORA", type="primary", use_container_width=True):
            barra=st.progress(0)
            for i in range(8):
                barra.progress((i+1)*12)
                st.write(f"✅ Trade {i+1}: Comprou R$ {random.uniform(299200,299800):.2f} → Vendeu R$ {random.uniform(300200,300800):.2f} | Lucro R$ 0,0{random.randint(2,9)} 💜 Taxa R$0,01")
                time.sleep(0.4)
            st.balloons()
            st.success("💜 Isso é GRID: pouquinho muitas vezes. Com R$7,81 centavos, com R$20 um pouco mais. Não é mágica.")

st.markdown('<div class="legal">💜 Trade Academy - Escola Completa - 10 capítulos separados. Conteúdo educacional livre Lei 9.394/96. Não é recomendação de investimento. Cripto tem alto risco. GRID pode dar prejuízo. Sem promessa de lucro.<br>Versão teste aberta, pagamento desativado por enquanto. Quando estiver 100% você ativa o R$20 no Cap 10.</div>', unsafe_allow_html=True)
