import streamlit as st
import pandas as pd
import numpy as np
from stable_baselines3 import PPO

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="EV Smart Charging",
    layout="wide"
)

# =========================================================
# LOAD RL MODEL
# =========================================================
@st.cache_resource
def load_model():
    return PPO.load("ev_agent")

rl_model = load_model()

# =========================================================
# SESSION
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================================================
# MODERN CSS
# =========================================================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0b1120;
    color: white;
}

.main {
    background: linear-gradient(180deg,#0b1120,#111827);
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

.header {
    background: linear-gradient(135deg,#06b6d4,#2563eb);
    padding: 30px;
    border-radius: 0px 0px 30px 30px;
    margin-bottom: 25px;
    color: white;
    box-shadow: 0px 10px 30px rgba(37,99,235,0.35);
}

.card {
    background: rgba(17,24,39,0.95);
    border-radius: 22px;
    padding: 22px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0px 5px 25px rgba(0,0,0,0.35);
}

.metric-card {
    background: linear-gradient(135deg,#111827,#1e293b);
    border-radius: 18px;
    padding: 14px;
    min-height: 160px;
    margin-bottom: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.05);

    display: flex;
    flex-direction: column;
    justify-content: center;
}

.status-green {
    color: #22c55e;
    font-weight: 700;
}

.status-yellow {
    color: #facc15;
    font-weight: 700;
}

.status-red {
    color: #ef4444;
    font-weight: 700;
}

.stButton>button {
    width: 100%;
    border-radius: 16px;
    height: 3.5em;
    border: none;
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    font-size: 15px;
    font-weight: 600;
    margin-top: 10px;
    box-shadow: 0px 6px 20px rgba(59,130,246,0.35);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class='header'>
    <h1>⚡ EV Smart Charging Platform</h1>
    <p>AI-powered EV charging & smart grid optimization</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR ROLE SWITCH
# =========================================================
st.sidebar.title("⚙ Dashboard")

role = st.sidebar.radio(
    "Select Role",
    ["User", "Admin"]
)

st.sidebar.markdown("---")

# =========================================================
# USER DASHBOARD
# =========================================================
if role == "User":

    # =============================
    # HOME PAGE
    # =============================
    if st.session_state.page == "home":

        st.markdown("## 🚗 User Dashboard")

        # VEHICLE CARD
        st.markdown("""
        <div class='card'>
            <h3>🚗 Electric Vehicle</h3>
            <p>Battery Level: <span class='status-green'>62%</span></p>
            <p>Estimated Range: 230 km</p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(0.62)

        # METRICS
        c1, c2, c3 = st.columns(3, gap="large")

        with c1:
            st.markdown("""
            <div class='metric-card'>
                <h4>⚡ Grid Status</h4>
                <p class='status-yellow'>Moderate</p>
                <small>Load balancing active</small>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class='metric-card'>
                <h4>☀️ Solar</h4>
                <p class='status-green'>18% OFF</p>
                <small>Peak hours active</small>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class='metric-card'>
                <h4>💰 Cost</h4>
                <p class='status-green'>₹138</p>
                <small>ML optimized</small>
            </div>
            """, unsafe_allow_html=True)

        # AI RECOMMENDATION
        st.markdown("""
        <div class='card'>
            <h3>🤖 AI Recommendation</h3>
            <p>
            AI suggests charging after 10 PM
            to avoid slow charging.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # QUICK ACTIONS
        st.markdown("### ⚡ Quick Actions")

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("⚡ Emergency Booking", use_container_width=True):
                st.session_state.page = "emergency"
                st.rerun()

        with col2:
            if st.button("📅 Book Slot", use_container_width=True):
                st.session_state.page = "booking"
                st.rerun()

        with col3:
            if st.button("🧠 AI Insights", use_container_width=True):
                st.session_state.page = "insights"
                st.rerun()

    # =============================
    # BOOKING PAGE
    # =============================
    elif st.session_state.page == "booking":

        st.markdown("## 📅 Book Charging Slot")

        date = st.date_input("Select Date")

        slot = st.selectbox(
            "Select Time Slot",
            [
                "08:00 AM",
                "10:00 AM",
                "12:00 PM",
                "02:00 PM",
                "06:00 PM"
            ]
        )

        mode = st.radio(
            "Charging Mode",
            [
                "Standard Grid",
                "Solar Optimized",
                "AI Recommended"
            ]
        )

        st.success("Estimated Cost: ₹138")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("✅ Confirm Booking", use_container_width=True):
                st.success("Charging Slot Confirmed")

        with col2:
            if st.button("⬅ Back", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()

    # =============================
    # EMERGENCY PAGE
    # =============================
    elif st.session_state.page == "emergency":

        st.markdown("## 🚨 Emergency Charging")

        st.error("Emergency fast charging enabled")

        st.markdown("""
        <div class='card'>
            <h3>⚡ Priority Charging</h3>
            <p>
            AI allocated highest priority charging slot.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⬅ Back to Dashboard"):
            st.session_state.page = "home"
            st.rerun()

    # =============================
    # AI INSIGHTS PAGE
    # =============================
    elif st.session_state.page == "insights":

        st.markdown("## 🧠 AI Insights")

        chart_data = pd.DataFrame({
            "Grid Load": np.random.randint(20,100,24)
        })

        st.line_chart(chart_data)

        st.markdown("""
        <div class='card'>
            <h3>⚡ ML Predictions</h3>
            <p>
            Peak load expected at 8 PM.
            AI shifted 342 users to off-peak charging.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("⬅ Back to Dashboard"):
            st.session_state.page = "home"
            st.rerun()

# =========================================================
# ADMIN DASHBOARD
# =========================================================
if role == "Admin":

    st.markdown("## ⚡ Admin Dashboard")

    # GRID STATUS
    st.markdown("""
    <div class='card'>
        <h3>⚡ Grid Stability Index</h3>
        <h1 class='status-green'>87.5</h1>
        <p>Stable Grid Performance</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(0.87)

    # METRICS
    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.markdown("""
        <div class='metric-card'>
            <h4>🚗 Active EVs</h4>
            <h2>42</h2>
            <small>Currently Charging</small>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-card'>
            <h4>⚡ Peak Load</h4>
            <h2 class='status-yellow'>78%</h2>
            <small>Expected at 8 PM</small>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-card'>
            <h4>☀️ Solar Efficiency</h4>
            <h2 class='status-green'>91%</h2>
            <small>Renewable utilization</small>
        </div>
        """, unsafe_allow_html=True)

    # GRID ANALYTICS
    st.markdown("""
    <div class='card'>
        <h3>📊 Grid Analytics</h3>
    </div>
    """, unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        "Grid Load": np.random.randint(30,100,24)
    })

    st.line_chart(chart_data)

# =============================
# SAMPLE ML PRIORITY DATA
# =============================

ev_data = pd.DataFrame({
    "EV_ID": [f"EV-{i}" for i in range(101,111)],
    "SoC": np.random.randint(10,90,10),
    "Distance": np.random.randint(5,150,10),
    "Profession": np.random.randint(1,5,10)
})

# RANDOM ML-LIKE PRIORITY SCORE
ev_data["Priority"] = (
    (100 - ev_data["SoC"]) * 0.5 +
    ev_data["Distance"] * 0.3 +
    (5 - ev_data["Profession"]) * 10 +
    np.random.randint(1,20,10)
)

# SORT BY PRIORITY
ev_data = ev_data.sort_values(
    by="Priority",
    ascending=False
)
      

    # PRIORITY TABLE
st.markdown("""
    <div class='card'>
        <h3>🤖 ML Priority Ranking</h3>
        <p>Live AI-based EV charging allocation</p>
    </div>
    """, unsafe_allow_html=True)

st.dataframe(
        ev_data,
        use_container_width=True
    )

    # TOP PRIORITY EV
top_ev = ev_data.iloc[0]

st.markdown(f"""
    <div class='card'>
        <h3>⚡ Highest Priority EV</h3>
        <h1>{top_ev['EV_ID']}</h1>
        <p>Priority Score: {top_ev['Priority']}</p>
    </div>
    """, unsafe_allow_html=True)

    # TRANSFORMER MONITORING
st.markdown("""
    <div class='card'>
        <h3>📡 Transformer Monitoring</h3>
    </div>
    """, unsafe_allow_html=True)

transformer_data = pd.DataFrame({
        "Voltage": np.random.randint(210,240,24),
        "Current": np.random.randint(20,80,24)
    })

st.line_chart(transformer_data)

    # OCCUPANCY
st.markdown("""
    <div class='card'>
        <h3>🚗 Charging Station Occupancy</h3>
    </div>
    """, unsafe_allow_html=True)

occupancy = pd.DataFrame({
        "Station": ["S1","S2","S3","S4"],
        "Occupied": [90,65,40,85]
    })

st.bar_chart(
        occupancy.set_index("Station")
    )

    # ALERTS
st.markdown("""
    <div class='card'>
        <h3>🚨 Smart Alerts</h3>
        Transformer nearing high load threshold
        AI successfully balanced evening demand
        

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    "<center style='color:gray;'>⚡ EV Smart Charging • AI Powered</center>",
    unsafe_allow_html=True
)