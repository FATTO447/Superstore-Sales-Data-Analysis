# 🔮 Superstore Sales Analytics & Prescriptive Forecasting Engine

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10-blue.svg)](https://www.python.org)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)](https://streamlit.io)
[![Apache PySpark](https://img.shields.io/badge/Apache_PySpark-ETL_Pipeline-E25A1C.svg)](https://spark.apache.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML_Model-F7931E.svg)](https://scikit-learn.org/)

An end-to-end retail intelligence platform and decision-support system built on the **Superstore** dataset. This project goes beyond traditional predictive modeling by combining a **Machine Learning baseline (Random Forest)** with a **Hybrid Expert Calibration Layer** to offer *prescriptive analytics* and real-time managerial scenario simulations.

---

## 🚀 Key Architectural Highlights

1. **Robust Data Engineering Pipeline:** Implements scalable data preprocessing and feature transformations leveraging **Apache PySpark**.
2. **Advanced Feature Engineering:** Automatically handles cyclical time-series variables using sine/cosine positional encodings (`Month_Sin`, `Month_Cos`, `Quarter_Sin`, `Quarter_Cos`) along with rolling historical sales lags and volatility tracking.
3. **Hybrid Intelligent System:** Integrates a predictive Machine Learning backbone with a rule-based expert layer to calibrate business anomalies (e.g., dynamic profit margins based on simulated discount rates, basket sizes, and holiday traffic).
4. **Interactive Simulation Dashboard:** A responsive **Streamlit** user interface designed for executive decision-making, showcasing immediate financial impacts and strategic risk warnings.

---

## 🛠️ Tech Stack & Core Dependencies

- **Data Engineering & ETL:** Apache PySpark, Pandas, NumPy
- **Machine Learning Infrastructure:** Scikit-Learn (`RandomForestRegressor`), Joblib (Model Serialization)
- **Interactive UI & Visualizations:** Streamlit, Plotly Express
- **Environment Management:** Git, Anaconda / Pip envs

---

## 📂 Repository Structure

```text
Superstore-Sales-Data-Analysis/
│
├── .vscode/                   # Editor configuration settings
├── analysis&modeling/         # Research & Development notebooks
│   ├── data.ipynb             # PySpark ETL, data cleaning & feature engineering
│   └── models.ipynb           # Machine Learning model training & evaluation
│
├── data/                      # Local storage for data assets
│
├── streamlit/                 # Interactive user interface deployment
│   ├── loader/                # Data adapters & internal utility loaders
│   └── pages/
│       └── 6_🔮_AI_Sales_Predictor.py  # Production forecasting engine
│
├── .gitignore                 # System & environment exclusion files
└── requirements.txt           # Python environment tracking specification
```

🕹️ Interactive Strategic Simulator Features
The core production dashboard equips managers with interactive sliders and controls to simulate future retail quarters:

Target Forecasting Month & Calendar Factors: Evaluates calendar trends and weekend distributions.

Seasonality Toggles: Direct controls for High-Demand periods (Black Friday, Cyber Monday, Holidays).

Discount & Basket Sizing Calibrators: Tests the behavior of sales volume against changing basket profiles and promotional metrics.

Strategic Risk Warning System: Automatically triggers prescriptive alerts (e.g., detecting severe profit leakage if steep discounts exceeding 20% are run during peak high seasons).

⚙️ Local Installation & Setup
Follow these steps to spin up the retail intelligence dashboard locally:

1. Clone the Repository
Bash
git clone [https://github.com/FATTO447/Superstore-Sales-Data-Analysis.git](https://github.com/FATTO447/Superstore-Sales-Data-Analysis.git)
cd Superstore-Sales-Data-Analysis
2. Configure Environment & Install Dependencies
Ensure you have Python 3.9+ installed. It is highly recommended to use a virtual environment:

Bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
3. Execution
To launch the Streamlit server and access the forecasting simulator webapp, execute:

Bash
streamlit run streamlit/pages/6_🔮_AI_Sales_Predictor.py
💡 Model Interpretation (Feature Weights)
The predictive engine is back-tested and analyzed for total transparency. Core impact drivers include:

Discount Strategy (Lag Factor): 42.5% impact weight.

Historical Sales Lags: 23.1% impact weight.

Cyclical Seasonality (Sin/Cos Encodings): 16.5% impact weight.

Basket Size Dynamics: 12.4% impact weight.
