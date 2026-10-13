import streamlit as st
import random
import time

st.set_page_config(page_title="Trade Academy - Dragão Gold Edition", page_icon="🐉", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
.stApp{background:#0f0f0f;color:#f5f1e8;}
.hero{
    background: radial-gradient(circle at top, #2a2210 0%, #1a1505 35%, #0f0f0f 100%);
    padding:48px 24px;border-radius:22px;text-align:center;
    border:2px solid #FFC300;box-shadow:0 0 40px #FFC30033;
    margin-bottom:24px;position:relative;
}
.hero::before{
    content:'';position:absolute;top:0;left:0;right:0;height:4px;
    background:linear-gradient(90deg,#FFC300,#FFB000,#FFD700,#FFC300);
    border-radius:22px 22px 0 0;
}
.hero h1{color:#FFC300;font-size:42px}
.hero p{color:#ffe9b8;opacity:0.9;font-size:17px}
.card{background:#1c1c1c;padding:22px;border-radius:16px;border:1px solid #2e2a1f;margin-top:8px;line-height:1.9;font-size:15px;color:#f0e6d2;}
.card-pop{background:linear-gradient(135deg,#201c0f 0%,#151208 100%);border:2px solid #FFC300;padding:24px;border-radius:16px;margin-top:8px;box-shadow:0 6px 20px rgba(255,195,0,0.12);}
.titulo{font-size:22px;font-weight:900;color:#FFC300;margin-bottom:10px;}
.dragao{background:linear-gradient(180deg,#222 0%,#111 100%);border:2px solid #FFC300;padding:16px;border-radius:16px;text-align:center;margin-bottom:14px;box-shadow:0 0 20px #FFC30022;}
.legal{font-size:11px;opacity:0.5;text-align:center;margin-top:40px;line-height:1.6;color:#cbb88f;}
div[data-testid="stExpander"]{background:linear-gradient(135deg,#1e1c10,#15120a)!important;border:1.5px solid #3a3520!important;border-radius:14px!important;margin-bottom:12px!important;}
div[data-testid="stExpander"]:hover{border-color
