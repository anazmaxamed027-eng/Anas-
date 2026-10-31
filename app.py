import streamlit as st
import pandas as pd
import time
import random

# 1. Page Configuration & Premium Theme Styling
st.set_page_config(
    page_title="Nexus Forex AI Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom code si wejiga loogu dhigo Premium Dark Mode oo midabyo Neon ah leh
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #334155; }
    div.stButton > button:first-child { background-color: #10b981; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    .stTextArea textarea { background-color: #020617; color: #38bdf8; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

# 2. Login Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- 🔐 BOGGA LOGIN-KA ---
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center; color: #10b981;'>🔐 Nexus AI Control Panel</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>Fadlan geli aqoonsigaaga si aad u gasho Dashboard-ka</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        # Halkan waxaa ku jira username-kaaga iyo password-kaaga aad hore u samaysatay
        username = st.text_input("Anas!!:")
        password = st.text_input("pio54321:", type="password")
        submit = st.form_submit_button("Gudaha u gal")
        
        if submit:
            if username == "admin" and password == "admin123": # Ku beddel kuwii aad samaysatay
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Username ama Password-ka waa khaldan yihiin saaxiib!")

# --- 🤖 BOGGA DASHBOARD-KA RASMIGA AH (MARKUU LOGIN-KU SAXMO) ---
else:
    # Header-ka Dashboard-ka oo aad u qurux badan
    col_title, col_status = st.columns([4, 1])
    with col_title:
        st.markdown("<h1 style='color: #ffffff;'>🤖 NEXUS <span style='color: #10b981;'>AI AGENT</span> PRO</h1>", unsafe_allow_html=True)
        st.caption("Forex Live Operations & Cloud Management Console")
    with col_status:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Log out"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")

    # SIDEBAR: VPS iyo Xawaaraha Internet-ka
    st.sidebar.markdown("<h2 style='color: #10b981;'>⚙️ System Settings</h2>", unsafe_allow_html=True)
    
    # 🌐 1. Qaybta Xawaaraha Internet-ka (Simulated Cloud Ping)
    st.sidebar.markdown("### 🌐 Network Status")
    ping_speed = random.randint(12, 35) # Tusaale xawaare ah
    st.sidebar.metric(label="VPS Latency (Ping)", value=f"{ping_speed} ms", delta="Excellent connection")
    st.sidebar.progress(92, text="Internet Speed Status (Stable)")

    # 🖥️ 2. Qaybta VPS Connection (Meel aad hadhow VPS-kaaga kaga xirto)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🖥️ VPS & MetaTrader Connection")
    vps_ip = st.sidebar.text_input("VPS IP Address:", placeholder="e.g. 192.168.1.100")
    vps_port = st.sidebar.text_input("Port Terminal:", placeholder="e.g. 443")
    vps_connected = st.sidebar.checkbox("Connect Bot to VPS")
    
    if vps_connected:
        if vps_ip and vps_port:
            st.sidebar.success(f"🟢 Active Connection linked to VPS: {vps_ip}")
        else:
            st.sidebar.warning("Fadlan qor IP-ga iyo Port-ka si loo xiro VPS-ka.")

    # MAIN CONTENT: Account Information & Performance
    st.markdown("### 📊 Live Account Metrics")
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Total Balance", value="$14,820.50", delta="+$1,110.00 (Bishan)")
    with m_col2:
        st.metric(label="Floating PnL (Open)", value="+$275.00", delta_color="normal")
    with m_col3:
        st.metric(label="AI Bot Win Rate", value="76.4%", delta="+2.1%")

    # LIVE TRADES TABLE
    st.markdown("### 📈 Live Open Positions")
    trades = {
        "Asset Pair": ["EURUSD", "GBPUSD", "XAUUSD (Gold)"],
        "Direction": ["BUY", "SELL", "BUY"],
        "Lot Size": [0.20, 0.15, 0.10],
        "Entry Price": [1.0850, 1.2640, 2735.20],
        "Current Profit": ["+$120.00", "-$35.00", "+$190.00"]
    }
    st.dataframe(pd.DataFrame(trades), use_container_width=True)

    # CHAT & AI LOGS SECTION (Meel aad wax walba kala socoto oo aad ku sheekaysato)
    st.markdown("### 🧠 AI Live Operations & Chat Logs")
    log_col, chat_col = st.columns([2, 1])
    
    with log_col:
        st.markdown("**Bot Execution History:**")
        st.text_area("Live Engine Logs:", value="[SYSTEM] - Web App connected to GitHub Repo successfully.\n[AI ENGINE] - Market scanning active. Volatility is optimal.\n[STRATEGY] - Golden Cross detected on Gold 15m chart.\n[VPS] - Heartbeat signal received from remote terminal.", height=150)
        
    with chat_col:
        st.markdown("**Quick Notes / Terminal Commands:**")
        st.text_input("Giri amar ama qoraal (e.g. Stop Bot):", key="cmd_input")
        st.caption("Sanduuqan waxaad u isticmaali kartaa inaad ammaro toos ah ku siiso Bot-ka marka VPS-ka la xiro.")
