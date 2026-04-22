# ⬡ You&.. Analytics OS

> **A dark-themed, gold-accented SaaS analytics dashboard built with Python & Streamlit.**

Upload any CSV or XLSX dataset and get an instant interactive analytics experience — no configuration needed.

---

## ✨ Features

- 📁 **Drag & Drop Upload** — supports CSV and Excel files
- 🔍 **Smart Filters** — sidebar filters for Region, Industry, Plan Type, Company Size + MRR slider
- 📊 **8 Analysis Tabs:**
  - **Preprocessing** — Null values, duplicates, outlier detection (IQR method)
  - **Overview** — KPI cards, MRR distribution, signup trends
  - **Revenue** — Industry breakdown, company size analysis, discount vs MRR heatmap
  - **Churn & Renewal** — Renewal status, churn risk distribution, high-risk account table
  - **Product Usage** — Feature adoption, seat utilization, MAU by region
  - **Trial & Conversion** — Conversion rates, trial length analysis, industry breakdown
  - **Customer Health** — NPS distribution, support tickets vs churn, health score stats
  - **Raw Data** — Column selector, descriptive statistics, filtered CSV export

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.10+` | Core language |
| `Streamlit` | Web app framework |
| `Pandas` | Data manipulation |
| `Plotly Express` | Interactive charts |
| `OpenPyXL` | Excel file support |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/youya-analytics-os.git
cd youya-analytics-os
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## 📂 Project Structure

```
youya-analytics-os/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---

## 🎨 Design System

| Token | Value | Usage |
|-------|-------|-------|
| `--bg-base` | `#07080a` | Page background |
| `--bg-elevated` | `#13161a` | Card backgrounds |
| `--accent-gold` | `#e8b84b` | Primary accent, KPI values |
| `--accent-crimson` | `#d94040` | Danger / churn indicators |
| `--accent-emerald` | `#2fcf8a` | Success / healthy indicators |
| `--text-primary` | `#e8e4d8` | Main text |
| `--text-secondary` | `#7a7870` | Labels and captions |

**Fonts:** Syne (headings) · Space Grotesk (body) · JetBrains Mono (labels/code)

---

## 📋 Expected Dataset Columns

The app is flexible — it works with any CSV/XLSX. For the best experience, include columns like:

```
Account_ID, Signup_Date, Region, Industry, Plan_Type, Company_Size,
MRR, ARR, Net_MRR, Discount_Pct, Churn_Risk, Health_Score,
Renewal_Status, Trial_Converted, Trial_Length_Days,
Usage_Hours_30D, Feature_Adoption_Score, Seat_Utilization_Pct,
Monthly_Active_Users, Support_Tickets_90D, NPS, CSM_Tier
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Built with ❤️ using Python, Streamlit & Plotly*
