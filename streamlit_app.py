import streamlit as st
import random

st.set_page_config(page_title="Dragon Academy Luxury Gold", page_icon="🐉", layout="wide")

st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
.stApp{background:#0a0a0a;color:#f5e9c0;font-family:'Inter',sans-serif;}
header{visibility:hidden;}
.block-container{padding-top:1rem!important;}

/* HEADER GOLD */
.header-gold{
    background:linear-gradient(90deg,#0a0a0a 0%,#1a1500 100%);
    border:1px solid #3a2f0a;
    border-radius:12px;
    padding:12px 20px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}
.btn-gold{
    background:linear-gradient(135deg,#FFD700,#FFC300);
    border:none;
    padding:8px 16px;
    border-radius:8px;
    color:#111;
    font-weight:800;
    font-size:13px;
}

/* CARDS */
.card-dark{
    background:#111111;
    border:1px solid #2a2510;
    border-radius:12px;
    padding:18px;
    margin-bottom:12px;
}
.card-gold{
    background:linear-gradient(135deg,#1c1a0a 0%,#111 100%);
    border:1.5px solid #FFC300;
    border-radius:12px;
    padding:18px;
    box-shadow:0 0 20px #FFC30022;
}
.card-stat{
    background:#101010;
    border:1px solid #FFC30044;
    border-radius:12px;
    padding:16px;
    text-align:center;
}
.gold-text{color:#FFC300;font-weight:900;}
.gold-big{color:#FFD700;font-size:28px;font-weight:900;}
.progress-bar{height:8px;background:#222;border-radius:10px;overflow:hidden;margin:8px 0;}
.progress-fill{height:100%;background:linear-gradient(90deg,#FFC300,#FFD700);width:40%;}
.badge-done{background:#FFC300;color:#111;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:800;}
.badge-lock{background:#222;color:#666;padding:2px 8px;border-radius:6px;font-size:11px;}
.candle{font-family:monospace;font-size:12px;}
hr{border-color:#222!important;}
</style>
''', unsafe_allow_html=True)

# HEADER
st.markdown('''
<div class='header-gold'>
    <div style='display:flex;align-items:center;gap:12px'>
        <div style='font-size:32px'>🐉</div>
        <div>
            <div style='font-size:22px;font-weight:900;color:#FFD700;letter-spacing:1px'>Dragon Academy</div>
            <div style='font-size:10px;letter-spacing:3px;color:#FFC300'>✦ LUXURY GOLD EDITION ✦</div>
        </div>
    </div>
    <div style='display:flex;gap:10px'>
        <div class='btn-gold'>🔔 Notifications</div>
        <div class='btn-gold'>👤 Profile</div>
        <div class='btn-gold'>👑 Upgrade • PRO</div>
    </div>
</div>
''', unsafe_allow_html=True)

col1, col2 = st.columns([1,2.5])

with col1:
    st.markdown('''
    <div class='card-dark' style='border-color:#FFC30066'>
        <div style='display:flex;align-items:center;gap:8px;margin-bottom:12px'>
            <span style='font-size:18px'>🏆</span>
            <b style='color:#FFC300'>CAP MODULES LIST</b>
        </div>
        <div class='card-dark'>
            <div style='font-size:13px'>CAP Modules — Progress 40%</div>
            <div class='progress-bar'><div class='progress-fill'></div></div>
            <br>
            <div style='font-size:13px'>✅ <b>CAP 01: Blockchain & Crypto Foundations</b><br><span style='color:#888;font-size:11px'>Completed • 12/12 lessons</span></div>
            <hr>
            <div style='font-size:13px'>✅ <b>CAP 02: Candlestick & Technical Analysis</b><br><span style='color:#FFC300;font-size:11px'>• In Progress • 7/15 lessons</span></div>
            <hr>
            <div style='font-size:13px'>🔒 <b>CAP 03: Risk & Position Sizing</b><br><span style='color:#555;font-size:11px'>Locked • 0/10 lessons</span></div>
            <hr>
            <div style='font-size:13px'>🔒 <b>CAP 04: Order Types & Executions</b><br><span style='color:#555;font-size:11px'>Locked • 0/8 lessons</span></div>
            <hr>
            <div style='font-size:13px'>🔒 <b>CAP 05: DeFi & On-chain Data</b><br><span style='color:#555;font-size:11px'>Locked • 0/10 lessons</span></div>
        </div>
        <div class='card-dark' style='background:#151300'>
            <div style='color:#FFC300;font-weight:800'>🔥 LEARNING STREAK</div>
            <div style='font-size:16px;font-weight:800'>7 Day Streak • 🔥</div>
            <div style='font-size:11px;color:#888'>Keep going! Next reward at 10 days</div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div style='margin-bottom:12px'>
        <div style='font-size:26px;font-weight:900;color:#f5e9a0'>Crypto Trading Educational App</div>
        <div style='font-size:13px;color:#cbb87a'>Learn • Practice • Master Crypto Trading | Streamlit App • Dragon Academy</div>
    </div>
    ''', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('''
        <div class='card-stat'>
            <div style='font-size:12px;color:#cbb87a'>Portfolio Balance (Paper)</div>
            <div class='gold-big'>$12,485.60</div>
            <div style='font-size:11px;color:#4ade80'>+$842.30 (+7.2%) this week</div>
        </div>
        ''', unsafe_allow_html=True)
    with c2:
        st.markdown('''
        <div class='card-stat'>
            <div style='font-size:12px;color:#cbb87a'>Win Rate</div>
            <div class='gold-big'>72%</div>
            <div style='font-size:11px;color:#888'>18 Wins • 7 Losses</div>
        </div>
        ''', unsafe_allow_html=True)
    with c3:
        st.markdown('''
        <div class='card-stat'>
            <div style='font-size:12px;color:#cbb87a'>XP Earned</div>
            <div class='gold-big'>1,240 XP</div>
            <div style='font-size:11px;color:#cbb87a'>+120 XP today • Level 6</div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1.7,1])

    with left:
        st.markdown('''
        <div class='card-dark'>
            <div style='display:flex;gap:8px;align-items:center'>
                <span style='font-size:18px'>📖</span>
                <div>
                    <div style='font-size:12px;color:#888'>Today's Lesson</div>
                    <div style='font-weight:800;color:#FFD700'>CAP 02: Candlestick & Technical Analysis</div>
                </div>
            </div>
            <hr>
            <div style='font-size:13px;color:#FFD700;font-weight:700'>Current Lesson: Support & Resistance Levels</div>
            <div style='font-size:12px;color:#bbb;margin:6px 0'>Identify key support and resistance zones using historical price action. Practice plotting levels on the chart below.</div>
            <div style='background:#0e0e0e;border:1px solid #222;padding:10px;border-radius:8px;margin:10px 0'>
                <div style='font-size:11px;color:#888'>Live Market Lab — BTC/USD • 1H</div>
                <div style='height:90px;display:flex;align-items:end;gap:3px;margin-top:8px'>
                    <div style='width:4px;height:40%;background:#ef4444'></div><div style='width:4px;height:60%;background:#22c55e'></div><div style='width:4px;height:30%;background:#ef4444'></div><div style='width:4px;height:80%;background:#22c55e'></div><div style='width:4px;height:50%;background:#ef4444'></div><div style='width:4px;height:70%;background:#22c55e'></div><div style='width:4px;height:35%;background:#ef4444'></div><div style='width:4px;height:90%;background:#22c55e'></div><div style='width:4px;height:60%;background:#ef4444'></div><div style='width:4px;height:85%;background:#22c55e'></div>
                    <div style='margin-left:auto;font-size:10px;color:#FFD700'>— Support $43,200<br>— Resistance $44,500</div>
                </div>
            </div>
            <div style='display:flex;gap:10px;margin-top:10px'>
                <div class='btn-gold' style='flex:1;text-align:center'>▶ Start Practice Trade</div>
                <div style='flex:1;text-align:center;border:1px solid #FFC30044;padding:8px;border-radius:8px;color:#FFC300;font-size:12px'>❓ Take Lesson Quiz</div>
            </div>
            <div style='margin-top:14px;font-size:12px'>
                <b>Lesson Objectives</b><br>
                • Understand how support/resistance form<br>
                • Learn to validate levels with volume<br>
                • Apply in paper trading scenario
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with right:
        st.markdown('''
        <div class='card-dark'>
            <div style='font-weight:800;color:#FFD700'>🛡️ Risk Management Lab</div>
            <div style='background:#211e0a;padding:8px;border-radius:6px;margin:10px 0;font-size:12px;font-weight:700'>Position Size Calculator</div>
            <div style='font-size:12px;line-height:1.8'>
                Account Balance:<br><b>$12,485.60</b><hr>
                Risk per Trade (2%):<br><b>$249.71</b><br>
                <div style='background:#0f0f0f;padding:6px;border-radius:6px;margin:6px 0'>Suggested Stop Loss:<br><b>$43,200</b></div>
                <div style='background:#0f0f0f;padding:6px;border-radius:6px'>Recommended Position:<br><b>0.0056 BTC</b></div>
            </div>
            <div class='btn-gold' style='text-align:center;margin-top:12px'>Run Simulation</div>
            <div style='margin-top:12px;background:#101010;border:1px solid #333;padding:10px;border-radius:8px;font-size:11px'>
                <b>💡 Pro Tip</b><br>Never risk more than 2% of your portfolio on a single trade. Use stop-losses to protect capital.
            </div>
        </div>
        ''', unsafe_allow_html=True)

    if st.button("🐉 RODAR SIMULADOR DRAGÃO GOLD", use_container_width=True):
        st.balloons()
        total = 0
        for i in range(8):
            lucro = random.uniform(0.02, 0.12)
            total += lucro
            st.write(f"Grade {i+1} - Lucro R$ {lucro:.4f}")
        st.success(f"Total Premium GOLD: R$ {total:.2f}")

st.markdown('''
<div style='text-align:center;margin-top:30px;padding:12px;border-top:1px solid #FFC30044;font-size:11px;color:#cbb87a'>
Dragon Academy • Luxury Gold Edition • Streamlit • Disclaimer: Paper trading only. Educational purposes — not financial advice.
</div>
''', unsafe_allow_html=True)
