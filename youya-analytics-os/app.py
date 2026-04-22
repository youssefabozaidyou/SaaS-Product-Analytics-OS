import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="You&.. Analytics OS",
    page_icon="⬡",
    layout="wide"
)

YOUYA_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Design Tokens ─────────────────────────────────── */
:root {
    --bg-base:        #07080a;
    --bg-surface:     #0d0f12;
    --bg-elevated:    #13161a;
    --bg-hover:       #1a1d22;

    --accent-gold:    #e8b84b;
    --accent-gold-2:  #c49a30;
    --accent-crimson: #d94040;
    --accent-emerald: #2fcf8a;
    --accent-sapphire:#4fa8f5;

    --text-primary:   #e8e4d8;
    --text-secondary: #7a7870;
    --text-muted:     #3d3b36;

    --border-soft:    rgba(232,184,75,0.08);
    --border-mid:     rgba(232,184,75,0.15);
    --border-strong:  rgba(232,184,75,0.35);

    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;

    --gold-glow:      0 0 24px rgba(232,184,75,0.12), 0 0 48px rgba(232,184,75,0.06);
    --card-shadow:    0 1px 0 rgba(255,255,255,0.03) inset, 0 -1px 0 rgba(0,0,0,0.4) inset;
}

/* ── Reset & Global ────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main {
    background-color: var(--bg-base) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
    border: none !important;
}

/* Subtle grid texture on the whole app background */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(232,184,75,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(232,184,75,0.015) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
    z-index: 0;
}

/* ── Sidebar ───────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: var(--bg-surface) !important;
    border-right: 1px solid var(--border-soft) !important;
}

[data-testid="stSidebar"] > div {
    padding-top: 2rem !important;
}

[data-testid="stSidebar"] * {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: 'Syne', sans-serif !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 4px !important;
    text-transform: uppercase;
    color: var(--accent-gold) !important;
    padding: 0 0 8px 0 !important;
}

[data-testid="stSidebar"] hr {
    border: none !important;
    border-top: 1px solid var(--border-soft) !important;
    margin: 1.5rem 0 !important;
}

/* Sidebar metric cards */
[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-md) !important;
    padding: 12px 14px !important;
    border-left: 2px solid var(--accent-gold) !important;
    border-bottom: none !important;
}

[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    font-size: 18px !important;
}

/* ── Slider ────────────────────────────────────────── */
[data-testid="stSidebar"] [data-testid="stSlider"] {
    padding: 8px 0 4px 0 !important;
}

[data-testid="stSidebar"] [data-testid="stSlider"] > div > div > div > div {
    background: var(--accent-gold) !important;
}

[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
    background: var(--accent-gold) !important;
    border: 2px solid var(--bg-base) !important;
    box-shadow: 0 0 8px rgba(232,184,75,0.4) !important;
    width: 16px !important;
    height: 16px !important;
}

[data-testid="stSidebar"] [data-testid="stSlider"] [data-baseweb="slider"] > div:first-child {
    background: var(--bg-elevated) !important;
    height: 3px !important;
    border-radius: 2px !important;
}

/* MRR Slider band card */
.mrr-slider-card {
    background: var(--bg-elevated);
    border: 1px solid var(--border-soft);
    border-left: 2px solid var(--accent-gold);
    border-radius: var(--radius-md);
    padding: 12px 14px;
    margin: 8px 0 4px 0;
}

.mrr-slider-card .label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 4px;
}

.mrr-slider-card .value {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: var(--accent-gold);
}

/* ── Typography ────────────────────────────────────── */
h1 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    font-size: 28px !important;
    letter-spacing: -0.5px !important;
    color: var(--text-primary) !important;
    text-transform: none !important;
    padding-bottom: 0 !important;
    border-bottom: none !important;
    margin-bottom: 0.5rem !important;
    line-height: 1.1 !important;
}

h2, h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    color: var(--text-secondary) !important;
    text-transform: uppercase !important;
    font-size: 10px !important;
    margin-top: 2rem !important;
    margin-bottom: 1rem !important;
}

p, li, label, span {
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 14px !important;
}

/* ── Horizontal Rule ───────────────────────────────── */
hr {
    border: none !important;
    border-top: 1px solid var(--border-soft) !important;
    margin: 1.5rem 0 !important;
}

/* ── KPI Metric Cards ──────────────────────────────── */
[data-testid="stMetric"] {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-lg) !important;
    padding: 20px 22px !important;
    border-bottom: 2px solid var(--accent-gold) !important;
    box-shadow: var(--card-shadow) !important;
    position: relative !important;
    overflow: hidden !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
}

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 60px; height: 60px;
    background: radial-gradient(circle, rgba(232,184,75,0.08) 0%, transparent 70%);
    pointer-events: none;
}

[data-testid="stMetric"]:hover {
    border-color: var(--border-mid) !important;
    border-bottom-color: var(--accent-gold) !important;
    box-shadow: var(--gold-glow), var(--card-shadow) !important;
}

[data-testid="stMetricLabel"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: var(--text-secondary) !important;
    font-weight: 400 !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 28px !important;
    font-weight: 800 !important;
    color: var(--accent-gold) !important;
    line-height: 1.1 !important;
    letter-spacing: -0.5px !important;
}

[data-testid="stMetricDelta"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1px !important;
}

/* ── Tabs ──────────────────────────────────────────── */
[data-baseweb="tab-list"] {
    background-color: transparent !important;
    border-bottom: 1px solid var(--border-soft) !important;
    gap: 0 !important;
    padding: 0 !important;
}

[data-baseweb="tab"] {
    background-color: transparent !important;
    color: var(--text-muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    padding: 10px 18px !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    margin-bottom: -1px !important;
    transition: all 0.2s ease !important;
}

[data-baseweb="tab"]:hover {
    color: var(--text-secondary) !important;
    background: rgba(232,184,75,0.04) !important;
}

[aria-selected="true"][data-baseweb="tab"] {
    color: var(--accent-gold) !important;
    border-bottom: 2px solid var(--accent-gold) !important;
    background: transparent !important;
}

[data-baseweb="tab-highlight"] {
    background-color: var(--accent-gold) !important;
    height: 2px !important;
}

[data-baseweb="tab-border"] {
    background-color: var(--border-soft) !important;
}

/* ── File Uploader ─────────────────────────────────── */
[data-testid="stFileUploader"] {
    background: var(--bg-surface) !important;
    border: 1px dashed var(--border-mid) !important;
    border-radius: var(--radius-lg) !important;
    padding: 24px !important;
    transition: all 0.25s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: var(--border-strong) !important;
    background: var(--bg-elevated) !important;
    box-shadow: var(--gold-glow) !important;
}

[data-testid="stFileUploader"] label {
    color: var(--accent-gold) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] * {
    color: var(--text-secondary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background-color: var(--accent-gold) !important;
    color: var(--bg-base) !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    letter-spacing: 2px !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    padding: 9px 22px !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease !important;
}

[data-testid="stFileUploaderDropzone"] button:hover {
    background-color: var(--text-primary) !important;
}

/* ── Selectbox / Multiselect ───────────────────────── */
[data-baseweb="select"] > div {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-sm) !important;
    color: var(--text-primary) !important;
    transition: border-color 0.2s !important;
}

[data-baseweb="select"] > div:hover {
    border-color: var(--border-mid) !important;
}

[data-baseweb="select"] svg { fill: var(--accent-gold) !important; }

[data-baseweb="popover"] {
    background: var(--bg-elevated) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5) !important;
}

[data-baseweb="option"] {
    background: var(--bg-elevated) !important;
    color: var(--text-primary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 13px !important;
}

[data-baseweb="option"]:hover,
[data-baseweb="option"][aria-selected="true"] {
    background: rgba(232,184,75,0.08) !important;
    color: var(--accent-gold) !important;
}

[data-baseweb="tag"] {
    background: rgba(232,184,75,0.1) !important;
    border: 1px solid var(--border-mid) !important;
    border-radius: 4px !important;
}

[data-baseweb="tag"] span {
    color: var(--accent-gold) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
}

/* ── Buttons ───────────────────────────────────────── */
[data-testid="stDownloadButton"] button,
.stButton > button {
    background: transparent !important;
    color: var(--accent-gold) !important;
    border: 1px solid var(--border-mid) !important;
    border-radius: var(--radius-sm) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 2px !important;
    padding: 9px 22px !important;
    text-transform: uppercase !important;
    transition: all 0.2s ease !important;
}

[data-testid="stDownloadButton"] button:hover,
.stButton > button:hover {
    background: var(--accent-gold) !important;
    color: var(--bg-base) !important;
    border-color: var(--accent-gold) !important;
    box-shadow: 0 0 20px rgba(232,184,75,0.25) !important;
}

/* ── DataFrames ────────────────────────────────────── */
[data-testid="stDataFrame"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-md) !important;
    overflow: hidden !important;
}

[data-testid="stDataFrame"] thead,
[data-testid="stDataFrame"] th {
    background: var(--bg-elevated) !important;
    color: var(--accent-gold) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    border-bottom: 1px solid var(--border-soft) !important;
}

[data-testid="stDataFrame"] td {
    color: var(--text-secondary) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 12px !important;
    border-bottom: 1px solid var(--border-soft) !important;
}

[data-testid="stDataFrame"] tr:hover td {
    background: rgba(232,184,75,0.03) !important;
    color: var(--text-primary) !important;
}

/* ── Alerts ────────────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: var(--radius-md) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 13px !important;
    border-left-width: 2px !important;
}

.stSuccess {
    background: rgba(47,207,138,0.06) !important;
    border-left-color: var(--accent-emerald) !important;
    color: var(--accent-emerald) !important;
}

.stWarning {
    background: rgba(232,184,75,0.06) !important;
    border-left-color: var(--accent-gold) !important;
    color: var(--accent-gold) !important;
}

.stError {
    background: rgba(217,64,64,0.06) !important;
    border-left-color: var(--accent-crimson) !important;
    color: var(--accent-crimson) !important;
}

.stInfo {
    background: rgba(79,168,245,0.06) !important;
    border-left-color: var(--accent-sapphire) !important;
    color: var(--text-secondary) !important;
}

/* ── Expander ──────────────────────────────────────── */
[data-testid="stExpander"] {
    background: var(--bg-surface) !important;
    border: 1px solid var(--border-soft) !important;
    border-radius: var(--radius-md) !important;
    transition: border-color 0.2s !important;
}

[data-testid="stExpander"]:hover {
    border-color: var(--border-mid) !important;
}

[data-testid="stExpander"] summary {
    color: var(--text-secondary) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

[data-testid="stExpander"] summary:hover {
    color: var(--accent-gold) !important;
}

/* ── Caption / Small Text ──────────────────────────── */
.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--text-muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1px !important;
}

/* ── Scrollbar ─────────────────────────────────────── */
::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border-mid); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent-gold); }

/* ── Plotly modebar ────────────────────────────────── */
.modebar { background: transparent !important; }
.modebar-btn path { fill: var(--text-muted) !important; }
.modebar-btn:hover path { fill: var(--accent-gold) !important; }

/* ── Header decoration line ────────────────────────── */
.header-rule {
    display: block;
    height: 1px;
    background: linear-gradient(90deg, var(--accent-gold) 0%, transparent 60%);
    margin: 6px 0 20px 0;
    opacity: 0.5;
}
</style>
"""
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#0d0f12",
    font=dict(family="Space Grotesk, sans-serif", color="#7a7870", size=12),
    title_font=dict(family="Syne, sans-serif", color="#e8b84b", size=13, weight="bold"),
    xaxis=dict(
        gridcolor="#13161a",
        linecolor="#1a1d22",
        tickcolor="#2a2a2a",
        tickfont=dict(color="#3d3b36", size=10, family="JetBrains Mono, monospace"),
        title_font=dict(color="#5a5850"),
    ),
    yaxis=dict(
        gridcolor="#13161a",
        linecolor="#1a1d22",
        tickcolor="#2a2a2a",
        tickfont=dict(color="#3d3b36", size=10, family="JetBrains Mono, monospace"),
        title_font=dict(color="#5a5850"),
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        bordercolor="#1a1d22",
        borderwidth=1,
        font=dict(color="#7a7870", size=11),
    ),
    margin=dict(t=52, b=40, l=44, r=20),
)

YOUYA_COLORS = [
    "#e8b84b",  # gold
    "#d94040",  # crimson
    "#2fcf8a",  # emerald
    "#4fa8f5",  # sapphire
    "#f97316",  # orange
    "#a78bfa",  # violet
    "#34d399",  # mint
    "#fb7185",  # rose
    "#c49a30",  # dark gold
]

COLOR_SCALE = [[0, "#13161a"], [0.5, "#c49a30"], [1, "#e8b84b"]]

def apply_layout(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig

st.markdown(YOUYA_CSS, unsafe_allow_html=True)

st.markdown("""
<div style="padding: 1.5rem 0 0 0;">
  <p style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:4px;color:#3d3b36;margin:0 0 6px 0;text-transform:uppercase;">
    You&.. · Intelligence Layer
  </p>
  <h1 style="margin:0 !important;">Analytics OS</h1>
  <span class="header-rule"></span>
</div>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "xlsx"])
if uploaded_file is None:
    st.markdown("""
    <div style="margin:3rem 0;padding:2rem;background:#0d0f12;border:1px solid rgba(232,184,75,0.08);border-radius:16px;text-align:center;">
      <p style="font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:3px;color:#3d3b36;text-transform:uppercase;margin:0;">
        Awaiting Dataset · Upload CSV or XLSX to begin
      </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()
try:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
except Exception as e:
    st.error(f"Error loading file: {e}")
    st.stop()

if "Signup_Date" in df.columns:
    df["Signup_Date"] = pd.to_datetime(df["Signup_Date"])
    df["Signup_Month"] = df["Signup_Date"].dt.month_name()
    df["Signup_Year"]  = df["Signup_Date"].dt.year

for col in df.select_dtypes("object").columns:
    df[col] = df[col].astype("category")


st.sidebar.markdown("### ⚙ Filters")

filters = {}
for col in ["Region", "Industry", "Plan_Type", "Company_Size"]:
    if col in df.columns:
        options = df[col].cat.categories.tolist()
        chosen  = st.sidebar.multiselect(col, options, default=options)
        filters[col] = chosen

filtered = df.copy()
for col, chosen in filters.items():
    filtered = filtered[filtered[col].isin(chosen)]

if "MRR" in df.columns:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💰 MRR Range")

    mrr_min = int(df["MRR"].min())
    mrr_max = int(df["MRR"].max())

    mrr_range = st.sidebar.slider(
        "Monthly Recurring Revenue ($)",
        min_value=mrr_min,
        max_value=mrr_max,
        value=(mrr_min, mrr_max),
        step=max(1, (mrr_max - mrr_min) // 200),
        format="$%d",
        help="Drag handles to isolate a specific MRR band — all tabs update instantly",
    )

    filtered = filtered[
        (filtered["MRR"] >= mrr_range[0]) & (filtered["MRR"] <= mrr_range[1])
    ]

    pct_shown   = len(filtered) / len(df) * 100 if len(df) > 0 else 0
    mrr_in_band = filtered["MRR"].sum()
    st.sidebar.markdown(
        f"""
        <div style="
            background:#13161a;
            border:1px solid rgba(232,184,75,0.08);
            border-left:2px solid #e8b84b;
            border-radius:10px;
            padding:12px 14px;
            margin:6px 0 2px 0;
        ">
            <div style="font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;
                        text-transform:uppercase;color:#3d3b36;margin-bottom:6px;">
                Active Band
            </div>
            <div style="font-family:'Syne',sans-serif;font-size:14px;font-weight:700;
                        color:#e8b84b;line-height:1.3;">
                ${mrr_range[0]:,} – ${mrr_range[1]:,}
            </div>
            <div style="font-family:'JetBrains Mono',monospace;font-size:9px;
                        color:#7a7870;margin-top:6px;letter-spacing:1px;">
                {len(filtered):,} accounts · {pct_shown:.0f}% of total<br>
                Band MRR: <span style="color:#c49a30;">${mrr_in_band:,.0f}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")
st.sidebar.metric("Accounts", len(filtered))
if "MRR" in filtered.columns:
    st.sidebar.metric("Total MRR", f"${filtered['MRR'].sum():,.0f}")

st.caption(f"Showing {len(filtered):,} of {len(df):,} accounts")

tabs = st.tabs([
    "⬡ Preprocessing",
    "⬡ Overview",
    "⬡ Revenue",
    "⬡ Churn & Renewal",
    "⬡ Product Usage",
    "⬡ Trial & Conversion",
    "⬡ Customer Health",
    "⬡ Raw Data",
])

# TAB 0 — Preprocessing
with tabs[0]:
    st.subheader("Data Quality")
    st.dataframe(filtered.head())

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows",    filtered.shape[0])
    col2.metric("Columns", filtered.shape[1])
    col3.metric("Memory",  f"{filtered.memory_usage(deep=True).sum() / 1024:.0f} KB")

    null_tab, dup_tab, out_tab = st.tabs(["Null Values", "Duplicates", "Outliers"])

    with null_tab:
        null_count = filtered.isnull().sum().sum()
        if null_count > 0:
            st.warning(f"Total Null Values: {null_count}")
            for col in filtered.columns:
                n = filtered[col].isnull().sum()
                if n > 0:
                    st.warning(f"  {col}: {n} nulls")
        else:
            st.success("No Null Values")

    with dup_tab:
        dup_count = filtered.duplicated().sum()
        if dup_count > 0:
            st.warning(f"Duplicate Rows: {dup_count}")
        else:
            st.success("No Duplicate Rows")
        col_check = st.selectbox("Check column", filtered.columns, key="dup_col")
        dup_in_col = filtered[col_check].duplicated().sum()
        if dup_in_col > 0:
            st.warning(f"{col_check}: {dup_in_col} duplicate values")
        else:
            st.success(f"No duplicates in '{col_check}'")

    with out_tab:
        numeric_cols = filtered.select_dtypes("number").columns.tolist()
        if numeric_cols:
            col_out = st.selectbox("Numeric column", numeric_cols, key="out_col")
            q1, q3 = filtered[col_out].quantile(0.25), filtered[col_out].quantile(0.75)
            iqr = q3 - q1
            outliers = filtered[(filtered[col_out] < q1-1.5*iqr) | (filtered[col_out] > q3+1.5*iqr)]
            if len(outliers):
                st.warning(f"Outliers: {len(outliers)}")
            else:
                st.success("No Outliers")
            fig = px.box(filtered, y=col_out, title=f"Box Plot — {col_out}",
                         color_discrete_sequence=[YOUYA_COLORS[0]])
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)


# TAB 1 — Overview
with tabs[1]:
    st.subheader("Key Metrics")

    kpi_cols = st.columns(4)
    if "MRR" in filtered.columns:
        kpi_cols[0].metric("Total MRR",  f"${filtered['MRR'].sum():,.0f}")
        kpi_cols[1].metric("Avg MRR",    f"${filtered['MRR'].mean():,.0f}")
    if "ARR" in filtered.columns:
        kpi_cols[2].metric("Total ARR",  f"${filtered['ARR'].sum():,.0f}")
    if "Churn_Risk" in filtered.columns:
        kpi_cols[3].metric("Avg Churn Risk", f"{filtered['Churn_Risk'].mean():.1f}%")

    st.markdown("---")
    col_a, col_b = st.columns(2)

    with col_a:
        if "Plan_Type" in filtered.columns and "MRR" in filtered.columns:
            plan_mrr = filtered.groupby("Plan_Type", observed=True)["MRR"].sum().reset_index()
            fig = px.pie(plan_mrr, names="Plan_Type", values="MRR",
                         title="MRR by Plan Type", hole=0.55,
                         color_discrete_sequence=YOUYA_COLORS)
            apply_layout(fig)
            fig.update_traces(textfont_color="white", textfont_size=11)
            st.plotly_chart(fig, use_container_width=True)

    with col_b:
        if "Region" in filtered.columns and "MRR" in filtered.columns:
            region_mrr = filtered.groupby("Region", observed=True)["MRR"].sum().sort_values()
            fig = px.bar(region_mrr, x=region_mrr.values, y=region_mrr.index,
                         orientation="h", title="MRR by Region",
                         color=region_mrr.values, color_continuous_scale=COLOR_SCALE,
                         text_auto=".2s")
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    if "Signup_Date" in filtered.columns:
        trend = filtered.groupby("Signup_Date").size().reset_index(name="New Accounts")
        fig = px.line(trend, x="Signup_Date", y="New Accounts",
                      title="Monthly Signup Trend",
                      color_discrete_sequence=[YOUYA_COLORS[0]])
        apply_layout(fig)
        fig.update_traces(line_width=1.5)
        st.plotly_chart(fig, use_container_width=True)

# TAB 2 — Revenue
with tabs[2]:
    st.subheader("Revenue Analysis")

    col1, col2 = st.columns(2)
    with col1:
        if "Industry" in filtered.columns and "MRR" in filtered.columns:
            ind_mrr = filtered.groupby("Industry", observed=True)["MRR"].sum().sort_values(ascending=False)
            fig = px.bar(ind_mrr, x=ind_mrr.index, y=ind_mrr.values,
                         title="MRR by Industry",
                         color=ind_mrr.values, color_continuous_scale=COLOR_SCALE,
                         text_auto=".2s")
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if "Company_Size" in filtered.columns and "MRR" in filtered.columns:
            fig = px.box(filtered, x="Company_Size", y="MRR",
                         color="Company_Size",
                         title="MRR by Company Size",
                         category_orders={"Company_Size": ["SMB", "Mid-Market", "Enterprise"]},
                         color_discrete_sequence=YOUYA_COLORS)
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    if "Discount_Pct" in filtered.columns and "Net_MRR" in filtered.columns:
        fig = px.scatter(filtered, x="Discount_Pct", y="Net_MRR",
                         color="Plan_Type" if "Plan_Type" in filtered.columns else None,
                         title="Discount % vs Net MRR", opacity=0.65,
                         color_discrete_sequence=YOUYA_COLORS)
        apply_layout(fig)
        st.plotly_chart(fig, use_container_width=True)

    if "Industry" in filtered.columns and "Plan_Type" in filtered.columns and "MRR" in filtered.columns:
        heat = filtered.pivot_table(values="MRR", index="Industry",
                                    columns="Plan_Type", aggfunc="sum", fill_value=0, observed=True)
        fig = px.imshow(heat, text_auto=".2s",
                        title="MRR Heatmap: Industry × Plan",
                        color_continuous_scale=COLOR_SCALE, aspect="auto")
        apply_layout(fig)
        st.plotly_chart(fig, use_container_width=True)

# TAB 3 — Churn & Renewal
with tabs[3]:
    st.subheader("Churn & Renewal")

    col1, col2 = st.columns(2)
    with col1:
        if "Renewal_Status" in filtered.columns:
            ren = filtered["Renewal_Status"].value_counts().reset_index()
            ren.columns = ["Status", "Count"]
            color_map = {"Renewed": "#2fcf8a", "Upcoming": "#e8b84b",
                         "At Risk": "#f97316", "Churned": "#d94040"}
            fig = px.pie(ren, names="Status", values="Count",
                         title="Renewal Status", color="Status",
                         color_discrete_map=color_map, hole=0.55)
            apply_layout(fig)
            fig.update_traces(textfont_color="white")
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if "Churn_Risk" in filtered.columns:
            fig = px.histogram(filtered, x="Churn_Risk", nbins=25,
                               title="Churn Risk Distribution",
                               color_discrete_sequence=[YOUYA_COLORS[1]])
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    if "Health_Score" in filtered.columns and "Churn_Risk" in filtered.columns:
        fig = px.scatter(filtered, x="Health_Score", y="Churn_Risk",
                         color="Renewal_Status" if "Renewal_Status" in filtered.columns else None,
                         size="MRR" if "MRR" in filtered.columns else None,
                         title="Health Score vs Churn Risk", opacity=0.65,
                         hover_data=["Account_ID"] if "Account_ID" in filtered.columns else None,
                         color_discrete_sequence=YOUYA_COLORS)
        apply_layout(fig)
        st.plotly_chart(fig, use_container_width=True)

    if "Churn_Risk" in filtered.columns:
        st.subheader("High-Risk Accounts (Churn Risk > 40%)")
        risk_cols = [c for c in ["Account_ID","Industry","Plan_Type","MRR","Churn_Risk","Health_Score","Renewal_Status"] if c in filtered.columns]
        at_risk = filtered.loc[filtered["Churn_Risk"] > 40, risk_cols].sort_values("Churn_Risk", ascending=False)
        st.dataframe(at_risk.reset_index(drop=True), use_container_width=True)
        st.caption(f"{len(at_risk)} at-risk accounts")

# TAB 4 — Product Usage
with tabs[4]:
    st.subheader("Product Usage")

    col1, col2 = st.columns(2)
    with col1:
        if "Usage_Hours_30D" in filtered.columns and "Feature_Adoption_Score" in filtered.columns:
            fig = px.scatter(filtered, x="Usage_Hours_30D", y="Feature_Adoption_Score",
                             color="Plan_Type" if "Plan_Type" in filtered.columns else None,
                             title="Usage Hours vs Feature Adoption", opacity=0.65,
                             color_discrete_sequence=YOUYA_COLORS)
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if "Plan_Type" in filtered.columns and "Seat_Utilization_Pct" in filtered.columns:
            fig = px.box(filtered, x="Plan_Type", y="Seat_Utilization_Pct",
                         color="Plan_Type", title="Seat Utilization by Plan",
                         color_discrete_sequence=YOUYA_COLORS)
            apply_layout(fig)
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    if "Region" in filtered.columns and "Monthly_Active_Users" in filtered.columns:
        mau = filtered.groupby("Region", observed=True)["Monthly_Active_Users"].mean().reset_index()
        fig = px.bar(mau, x="Region", y="Monthly_Active_Users",
                     title="Avg Monthly Active Users by Region",
                     color="Region", color_discrete_sequence=YOUYA_COLORS, text_auto=".0f")
        apply_layout(fig)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# TAB 5 — Trial & Conversion
with tabs[5]:
    st.subheader("Trial & Conversion")

    if "Trial_Converted" in filtered.columns:
        conv_rate = (filtered["Trial_Converted"] == "Yes").mean() * 100
        m1, m2, m3 = st.columns(3)
        m1.metric("Conversion Rate", f"{conv_rate:.1f}%")
        if "Trial_Length_Days" in filtered.columns:
            m2.metric("Avg Trial Length", f"{filtered['Trial_Length_Days'].mean():.0f} days")
        m3.metric("Converted Accounts", f"{(filtered['Trial_Converted'] == 'Yes').sum():,}")

        col1, col2 = st.columns(2)
        with col1:
            tc = filtered["Trial_Converted"].value_counts().reset_index()
            tc.columns = ["Converted", "Count"]
            fig = px.pie(tc, names="Converted", values="Count",
                         title="Trial Conversion", color="Converted",
                         color_discrete_map={"Yes": "#2fcf8a", "No": "#d94040"}, hole=0.55)
            apply_layout(fig)
            fig.update_traces(textfont_color="white")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            if "Trial_Length_Days" in filtered.columns:
                fig = px.box(filtered, x="Trial_Converted", y="Trial_Length_Days",
                             color="Trial_Converted", title="Trial Length vs Conversion",
                             color_discrete_map={"Yes": "#2fcf8a", "No": "#d94040"})
                apply_layout(fig)
                fig.update_layout(showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

        if "Industry" in filtered.columns:
            ind_conv = (filtered.groupby("Industry", observed=True)["Trial_Converted"]
                        .apply(lambda x: (x == "Yes").mean() * 100).reset_index())
            ind_conv.columns = ["Industry", "Conversion_Rate"]
            ind_conv = ind_conv.sort_values("Conversion_Rate", ascending=False)
            fig = px.bar(ind_conv, x="Industry", y="Conversion_Rate",
                         title="Conversion Rate by Industry",
                         color="Conversion_Rate", color_continuous_scale="RdYlGn",
                         text_auto=".1f")
            apply_layout(fig)
            fig.update_traces(texttemplate="%{text}%", textposition="outside")
            st.plotly_chart(fig, use_container_width=True)

# TAB 6 — Customer Health
with tabs[6]:
    st.subheader("Customer Health & NPS")

    col1, col2 = st.columns(2)
    with col1:
        if "NPS" in filtered.columns:
            fig = px.histogram(filtered, x="NPS", nbins=20,
                               title="NPS Score Distribution",
                               color_discrete_sequence=[YOUYA_COLORS[0]])
            apply_layout(fig)
            fig.add_vline(x=0,  line_dash="dot", line_color=YOUYA_COLORS[1], line_width=1,
                          annotation_text="Neutral", annotation_font_color="#7a7870", annotation_font_size=10)
            fig.add_vline(x=50, line_dash="dot", line_color=YOUYA_COLORS[2], line_width=1,
                          annotation_text="Good",    annotation_font_color="#7a7870", annotation_font_size=10)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if "Support_Tickets_90D" in filtered.columns and "Churn_Risk" in filtered.columns:
            fig = px.scatter(filtered, x="Support_Tickets_90D", y="Churn_Risk",
                             color="Plan_Type" if "Plan_Type" in filtered.columns else None,
                             title="Support Tickets vs Churn Risk", opacity=0.65,
                             color_discrete_sequence=YOUYA_COLORS)
            apply_layout(fig)
            st.plotly_chart(fig, use_container_width=True)

    if "CSM_Tier" in filtered.columns and "MRR" in filtered.columns:
        csm = filtered.groupby("CSM_Tier", observed=True)["MRR"].sum().reset_index()
        fig = px.pie(csm, names="CSM_Tier", values="MRR",
                     title="MRR by CSM Tier", hole=0.55,
                     color_discrete_sequence=YOUYA_COLORS)
        apply_layout(fig)
        fig.update_traces(textfont_color="white")
        st.plotly_chart(fig, use_container_width=True)

    if "Health_Score" in filtered.columns:
        st.subheader("Health Score Statistics")
        h = filtered["Health_Score"]
        s1, s2, s3, s4 = st.columns(4)
        s1.metric("Max",    f"{h.max():.1f}")
        s2.metric("Min",    f"{h.min():.1f}")
        s3.metric("Mean",   f"{h.mean():.1f}")
        s4.metric("Median", f"{h.median():.1f}")

# TAB 7 — Raw Data
with tabs[7]:
    st.subheader("Dataset Explorer")

    all_cols     = filtered.columns.tolist()
    default_cols = all_cols[:10] if len(all_cols) > 10 else all_cols
    selected_cols = st.multiselect("Select columns", all_cols, default=default_cols)

    if selected_cols:
        st.dataframe(filtered[selected_cols].reset_index(drop=True), use_container_width=True, height=400)

    with st.expander("Descriptive Statistics"):
        st.dataframe(filtered.describe(), use_container_width=True)

    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download Filtered CSV", data=csv,
                       file_name="youya_filtered.csv", mime="text/csv")

st.markdown("---")
st.caption("You&.. Analytics OS · Streamlit · Pandas · Plotly")