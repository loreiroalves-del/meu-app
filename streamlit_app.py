import streamlit as st, random, time
from datetime import datetime

st.set_page_config(page_title="Trade Academy - Acolhedora", page_icon="🐱", layout="wide")

if "lib1" not in st.session_state: st.session_state.lib1=False
if "lib20" not in st.session_state: st.session_state.lib20=False

st.markdown("""
<style>
.stApp{background:#0f0f12; color:#e8e8e8;}
.hero{background: linear-gradient(180deg, #1a1625 0%, #0f0f12 100%); padding:40px; border-radius:24px; text-align:center; border:1px solid #2a2438;}
.card{background:#18161f; padding:20px; border-radius:16px; border:1px solid #2a2438; margin-bottom:12px;}
.card-soft{background:#1c1a26; border:1px solid #3a3450; padding:20px; border-radius:16px;}
.legal{font-size:11px; opacity:0.5; margin-top:20px;}
#catbot-btn{position:fixed; bottom:22px; right:22px; z-index:99999; background:#2a2440; border:1px solid #7c3aed; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:28px; cursor:pointer; box-shadow:0 4px 20px #000;}
#catbot-box{position:fixed; bottom:90px; right:20px; z-index:99999; width:320px; background:#1c1a26; border:1px solid #3a3450; border-radius:18px; padding:16px; display:none;}
.cat-opt{background:#252236; border:1px solid #3a3450; padding:10px; border-radius:12px; margin:6px 0; cursor:pointer; width:100%; color:#e8e8e8; text-align:left;}
.cat-opt:hover{background:#2e2a44;}
</style>
""", unsafe_allow_html=True)

# GATINHO ACOLHEDOR
st.markdown("""
<div id="catbot-btn" onclick="toggleCat()">🐱</div>
<div id="catbot-box">
<div style="display:flex; justify-content:space-between;"><b>🐱 Gatinho aqui pra te ajudar</b><span onclick="toggleCat()" style="cursor:pointer;">✖️</span></div>
<div style="background:#252236; padding:10px; border-radius:12px; margin:10px 0; font-size:13px; line-height:1.4;">
Fica tranquilo, todo mundo começa sem entender nada. Me diz onde travou que eu explico com calma 💜
</div>
<button class="cat-opt" onclick="alert('GRID com calma: imagina que você disse pro robô - trabalha só entre 0,07 e 0,10. Quando cai ele compra, quando sobe ele vende. Sem pressa, vai na Pasta 2 que explico devagar.')">🤖 Não entendi GRID ainda</button>
<button class="cat-opt" onclick="alert('Converter com calma: você manda Reais via PIX e recebe USDT (dólar digital). Depois com USDT compra a moedinha. É como trocar dinheiro pra viajar. Pasta 1 explica passo a passo.')">💱 Como converte Real?</button>
<button class="cat-opt" onclick="alert('Sobre começar com pouco: você tinha 7,81 USDT e deu erro de 65 USDT porque a moeda era cara. Com moeda de centavos + 3 grids libera. Não é sua culpa, é configuração. Te mostro na Pasta 3.')">💸 Tenho pouco, e agora?</button>
<button class="cat-opt" onclick="alert('Respira, tá tudo bem ficar com dúvida. GRID pode dar prejuízo também, não é mágica. O importante é entender o risco antes. Veja a Pasta 4 com calma.')">😰 Tô com medo de perder</button>
<div style="font-size:11px; opacity:0.5; margin-top:10px; text-align:center;">Aqui é lugar seguro pra aprender, sem pressa 💜</div>
</div>
<script>function toggleCat(){var b=document.getElementById('catbot-box'); b.style.display=b.style.display=='none'||b.style.display==''?'block':'none';}</script>
""", unsafe_allow_html=True)

try: st.image("grid.png", use_container_width=True)
except: pass

with st.sidebar:
    st.title("💜 Trade Academy")
    st.caption("Aprenda no seu tempo, sem pressa")
    if not st.session_state.lib1:
        menu=st.radio("Onde você quer começar?", ["🏠 Boas-vindas", "🎮 Ver simulador calmo"])
    else:
        menu=st.radio("Suas pastas", ["📚 Começar do zero", "🤖 Entender o GRID", "💸 Com pouco dinheiro", "💜 Dúvidas e cuidados", "🏆 Seu certificado", "🚀 Bônus - Criar seu app"])
    st.divider()
    if not st.session_state.lib1:
        st.write("Acesso educacional por R$1")
        st.link_button("💜 Entrar por R$1", "https://mpago.la/1mfEXkt", use_container_width=True)
        if st.button("Já paguei R$1, quero entrar"): st.session_state.lib1=True; st.rerun()
    else:
        st.success("Você já está dentro 💜")
        st.link_button("🚀 Ver bônus R$20", "https://mpago.la/1jN2tXo", use_container_width=True)
        if st.button("Já paguei R$20"): st.session_state.lib20=True; st.rerun()

LEGAL='<div class="legal">Conteúdo educacional, curso livre Lei 9.394/96 Art.42. Não é consultoria CVM, sem MEC/CNPI. Cripto tem risco de perda. GRID é estratégia educacional que pode ter prejuízo. Sem promessa de lucro. Suporte via gatinho no app.</div>'

if menu=="🏠 Boas-vindas":
    st.markdown("""
    <div class="hero">
    <h1>💜 Bem-vindo, fica à vontade</h1>
    <p style="font-size:18px; line-height:1.6; opacity:0.9;">
    Aqui você não precisa saber nada de cripto.<br>
    A gente vai no seu tempo, sem pressa, sem competição.<br>
    Se travar, chama o gatinho no canto 🐱 ele explica com calma.
    </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class="card-soft">
    <h3>💜 Como vai funcionar, sem susto:</h3>
    <p>1. Primeiro você vê o simulador, só pra entender a ideia, sem dinheiro real<br>
    2. Depois entra na Pasta 1 - lá explico o que é USDT como se fosse pra uma criança<br>
    3. Na Pasta 2 mostro o robô da imagem, botão por botão, com calma<br>
    4. Na Pasta 3 te mostro seu caso real: por que deu erro de 65 USDT e como liberou com 7,81<br>
    5. Se ficar com medo, tem a Pasta 4 só de cuidados e riscos</p>
    <p><b>Tudo por R$1, no seu tempo. Sem WhatsApp te cobrando, sem grupo te apressando.</b></p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("💜 Quero aprender com calma por R$1", "https://mpago.la/1mfEXkt", use_container_width=True)
    st.markdown(LEGAL, unsafe_allow_html=True)

elif "simulador" in menu.lower():
    st.title("🎮 Simulador calmo - só pra entender")
    st.markdown('<div class="card-soft">Aqui é só de mentirinha, pra você ver como o robô pensa. Sem dinheiro real, sem risco, só pra ficar confortável com a ideia 💜</div>', unsafe_allow_html=True)
    invest=st.slider("Valor fictício (só pra simular)", 5.0, 20.0, 7.81)
    grids=st.slider("Quantidade de grids", 3, 12, 3)
    pct=14.07 if grids==3 else 2.36 if grids>=12 else 8.0
    if st.button("▶️ Ver como funciona devagar"):
        ph=st.empty()
        for i in range(6):
            pr=round(random.uniform(0.07,0.10),4)
            msg="comprou fictício" if i%2==0 else "vendeu fictício"
            ph.markdown(f'<div class="card">🐱 Robô {msg} a {pr} - estimativa educacional {invest*pct/100:.2f} USDT (não é real)</div>', unsafe_allow_html=True)
            time.sleep(0.8)
        st.info("Viu? Ele compra na baixa e vende na alta. Na vida real pode ter perda também, por isso estudamos riscos com calma.")
    st.markdown(LEGAL, unsafe_allow_html=True)

elif menu=="📚 Começar do zero":
    st.title("📚 Começar do zero, sem vergonha")
    st.markdown('<div class="card-soft">Não tem pergunta boba aqui. Todo mundo começou sem saber.</div>', unsafe_allow_html=True)
    with st.expander("O que é cripto, explicado com carinho", expanded=True):
        st.write("Pensa num caderno que todo mundo tem cópia. Quando alguém manda dinheiro, todo mundo anota. Ninguém apaga. Esse caderno é o blockchain. Sobe e desce porque tem gente comprando e vendendo.")
    with st.expander("O que é USDT?"):
        st.write("USDT é só um dólar digital. 1 USDT vale perto de 1 dólar. A gente usa ele pra não se perder. Você manda Reais via PIX e recebe USDT. Com USDT compra a moedinha.")
    with st.expander("Como não cair em golpe?"):
        st.write("Se alguém te chamar no privado prometendo dobrar dinheiro, bloqueia. No P2P, só negocie com quem tem muitas vendas e nota boa. E nunca mande cripto pra alguém que promete retorno.")
    st.markdown(LEGAL, unsafe_allow_html=True)

elif menu=="🤖 Entender o GRID":
    st.title("🤖 Entender o GRID com calma")
    st.markdown('<div class="card-soft">GRID é só um nome bonito pra robô que compra barato e vende caro sozinho dentro de uma faixa que você escolhe.</div>', unsafe_allow_html=True)
    with st.expander("Exemplo da sua imagem 0,07 a 0,10", expanded=True):
        st.write("Você fala: robô, trabalha só entre 0,07 e 0,10 com 3 degraus. Caiu pra 0,07 ele compra. Subiu pra 0,08 ele vende com estimativa de 10% a 14% (não garantido). E repete. Quando tem 12 degraus, estimativa por venda fica menor, tipo 2,36%, e pede mais dinheiro pra começar, por isso deu erro 17,43 USDT.")
    st.markdown(LEGAL, unsafe_allow_html=True)

elif menu=="💸 Com pouco dinheiro":
    st.title("💸 Com pouco dinheiro, do seu jeito")
    st.markdown('<div class="card-soft">Seu caso real: você tinha 7,81 USDT e deu erro de 65 USDT porque a moeda era cara e tinha muitos degraus. Quando usou moeda de centavos + 3 grids, liberou. Não foi sorte, foi configuração. Você já achou o caminho.</div>', unsafe_allow_html=True)
    st.write("Não precisa ter muito. Começa com exemplo pequeno, só pra entender. Se perder, que seja pouco e aprendendo.")
    st.markdown(LEGAL, unsafe_allow_html=True)

elif menu=="💜 Dúvidas e cuidados":
    st.title("💜 Dúvidas e cuidados - parte mais importante")
    with st.expander("E se sair da faixa 0,07 a 0,10?", expanded=True): st.write("Robô para. Tá tudo bem, acontece. Você fecha e cria novo onde preço está, com calma.")
    with st.expander("Se internet cair?"): st.write("Robô fica na nuvem, não no seu celular. Mas pode falhar, tecnologia falha. Por isso não coloque tudo.")
    with st.expander("Posso perder?"): st.write("Pode. Se moeda só cai e não volta, fica com prejuízo. Por isso estudamos moeda que fica andando de lado e usamos stop ligado. Isso não evita perda, só ajuda a controlar.")
    with st.expander("Como sacar pra Reais?"): st.write("Faz o caminho inverso: moedinha -> USDT -> vende por PIX no P2P. Com calma, confere taxas.")
    st.markdown(LEGAL, unsafe_allow_html=True)

elif menu=="🏆 Seu certificado":
    st.title("🏆 Seu certificado de dedicação")
    st.markdown('<div class="card-soft">Esse certificado é só pra lembrar que você se dedicou a aprender, no seu tempo. Sem pressa, sem competição.</div>', unsafe_allow_html=True)
    nome=st.text_input("Como quer que apareça seu nome?")
    if nome:
        st.markdown(f"""
        <div class="card" style="text-align:center; border:1px solid #7c3aed;">
        <h3>💜 Certificado de Conclusão - Curso Livre</h3>
        <p>Curso livre - Introdução ao GRID (Educacional) - 4h</p>
        <h2>{nome}</h2>
        <p>Concluiu com dedicação em {datetime.now().strftime('%d/%m/%Y')}</p>
        <p style="font-size:11px; opacity:0.6;">Curso livre Lei 9.394/96, sem MEC/CVM/CNPI. Educacional, sem recomendação investimento, risco de perda. Feito com carinho pela Trade Academy.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown(LEGAL, unsafe_allow_html=True)

elif "Bônus" in menu:
    if not st.session_state.lib20:
        st.title("🚀 Bônus - Criar seu app acolhedor")
        st.markdown('<div class="card-soft">Se você gostou desse jeito calmo de ensinar, no bônus te ensino a criar um app igual esse, acolhedor, pra você ensinar do seu jeito também. Sem promessa de venda.</div>', unsafe_allow_html=True)
        st.link_button("💜 Ver bônus R$20", "https://mpago.la/1jN2tXo", use_container_width=True)
    else:
        st.title("🚀 Como criar seu app acolhedor")
        st.write("1. GitHub > New repo\n2. Cria streamlit_app.py com esse código calmo\n3. Deploy no Streamlit\n4. Troca links\n5. Ensina com carinho, como você faz")
    st.markdown(LEGAL, unsafe_allow_html=True)
