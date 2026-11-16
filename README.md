# 📊 Amazon India Revenue Leakage & Profitability Command Center

<p align="center">
  <strong>An End-to-End E-Commerce Data Analytics & Business Intelligence Project</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-SQLite-003B57?logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Data%20Analysis-Pandas-150458?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
</p>

---

## 📌 Project Overview

The **Amazon India Revenue Leakage & Profitability Command Center** is an end-to-end data analytics project designed to investigate revenue leakage, profitability challenges, inventory inefficiencies, and marketplace pricing inconsistencies in Indian e-commerce operations.

The project analyzes approximately 129,000 Amazon India order lines alongside supporting business datasets to transform raw commercial data into actionable business intelligence.

The ultimate goal is to help business stakeholders understand:

- Where revenue is being lost.
- Why profitability is under pressure.
- Which products and categories create the highest risks.
- How inventory and pricing decisions can be improved.
- Which actions should be prioritized to protect revenue.

## 🎯 Business Problem

**"Sales are increasing, but why isn't the bank balance growing?"**

An Indian ethnic-wear business sells products across multiple online marketplaces. Despite increasing order volumes, the business faces potential financial losses caused by:

- Order cancellations and returns.
- Inventory shortages and stock-outs.
- Unsold and dead inventory.
- Inconsistent marketplace pricing.
- Operational and warehouse expenses.

This project uses Python, SQL, statistical analysis, and machine learning to investigate these challenges and support better business decisions.

---

## 📂 Dataset Information

| Attribute | Details |
|---|---|
| Dataset | E-Commerce Sales Dataset – Amazon India |
| Source | Kaggle |
| Main Dataset | Amazon Sale Report |
| Verified Main Dataset Rows | 128,975 |
| Main Dataset Columns | 24 original columns |
| Historical Period | April–June 2022 |
| Supporting Files | 6 additional datasets |

**Dataset Source:**  
https://www.kaggle.com/datasets/thedevastator/unlock-profits-with-e-commerce-sales-data

### Supporting Business Data

1. Amazon Sales Transactions
2. Warehouse Inventory
3. Product Pricing and Cost Information
4. International Sales
5. Business Expenses
6. Warehouse Fee Comparison

*Raw commercial datasets are excluded from this repository.*

---

## 🛠️ Technology Stack

| Technology | Application |
|---|---|
| Python | Core programming and data processing |
| Pandas & NumPy | Data cleaning and transformation |
| SQLite | Relational database |
| Advanced SQL | Business intelligence and analytics |
| Matplotlib & Seaborn | Statistical visualization |
| Plotly | Interactive data visualization |
| SciPy | Hypothesis testing |
| Statsmodels | Time-series forecasting |
| Scikit-learn | Predictive modelling |
| Streamlit | Interactive analytics dashboard |
| Git & GitHub | Version control |

---

## 🏗️ Project Architecture

```text
                 RAW BUSINESS DATA
                         |
                         ▼
                  DATA INGESTION
                         |
                         ▼
                DATA QUALITY AUDIT
                         |
                         ▼
              DATA CLEANING & FEATURES
                         |
                         ▼
                  SQLITE DATABASE
                         |
                         ▼
                  ADVANCED SQL
                         |
                         ▼
              EXPLORATORY DATA ANALYSIS
                         |
                         ▼
              REVENUE LEAKAGE ANALYSIS
                         |
                         ▼
             MACHINE LEARNING & FORECAST
                         |
                         ▼
              STREAMLIT COMMAND CENTER
                         |
                         ▼
              BUSINESS INSIGHTS & ACTIONS
```

---

## 📈 Analytical Objectives

### 01. Revenue Leakage Analysis
- Quantify cancellation and return-related losses.
- Calculate gross sales and net realised revenue.
- Identify leakage by category, SKU, size and geography.
- Build a revenue leakage waterfall.

### 02. Advanced SQL Analytics
- Design a relational star schema.
- Implement CTEs and window functions.
- Develop analytical SQL views.
- Identify top-performing products and categories.
- Analyze weekly and monthly revenue trends.

### 03. Exploratory Data Analysis
- Revenue and order trends.
- Product and category performance.
- Geographic demand analysis.
- Fulfilment performance.
- Promotion effectiveness.
- Customer order patterns.

### 04. Inventory Intelligence
- ABC inventory classification.
- Stock-out risk identification.
- Dead-stock analysis.
- Days of inventory cover.

### 05. Marketplace Pricing Intelligence
- Compare marketplace product prices.
- Identify pricing parity gaps.
- Estimate margins using transfer price as a cost proxy.

### 06. Predictive Analytics
- Cancellation and return risk prediction.
- Model evaluation and feature importance.
- Fourteen-day product demand forecasting.

---

## 📊 Key Business KPIs

The final dashboard will monitor:

| KPI | Business Purpose |
|---|---|
| Gross Sales | Total recorded sales value |
| Net Realised Revenue | Revenue after defined leakage adjustments |
| Revenue Leakage ₹ | Estimated value lost |
| Leakage Rate % | Leakage relative to gross sales |
| Average Order Value | Average order-line value |
| Units Sold | Total quantity sold |
| Stock-out Risk | Products requiring inventory attention |
| Price Parity Gap | Marketplace pricing inconsistency |

---

## 🗂️ Repository Structure

```text
amazon-india-revenue-leakage/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── sql/
│
├── docs/
│
├── app/
│   └── pages/
│
├── models/
│
├── images/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Project Development Progress

| Phase | Development Area | Status |
|---|---|---|
| 01 | Problem Framing & Project Setup | Completed |
| 02 | Data Ingestion & Quality Audit | In Progress |
| 03 | Database Design & Advanced SQL | Upcoming |
| 04 | Data Cleaning & Feature Engineering | Upcoming |
| 05 | Exploratory Data Analysis | Upcoming |
| 06 | Leakage Diagnostics & Statistics | Upcoming |
| 07 | Inventory & Pricing Intelligence | Upcoming |
| 08 | Predictive Modelling & Forecasting | Upcoming |
| 09 | Streamlit Dashboard & Deployment | Upcoming |
| 10 | Business Insights & Final Reporting | Upcoming |

---

## 📉 Dashboard Preview

The final Streamlit application will contain:

- Executive Overview
- Revenue Leakage Explorer
- Geographic Performance
- Product & Inventory Intelligence
- Marketplace Pricing Parity
- Risk Prediction

*Dashboard screenshots and live deployment link will be added after development.*

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/arushicoder/amazon-india-revenue-leakage.git
```

### 2. Navigate into the project

```bash
cd amazon-india-revenue-leakage
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the dashboard

```bash
streamlit run app/streamlit_app.py
```

<<<<<<< HEAD
*The dashboard command
=======
*The dashboard command will be available once the application is implemented.*

---

## 📌 Project Limitations

- The available historical sales data covers a limited period.
- Missing and inconsistent records require careful treatment.
- Transfer price is a cost proxy, not verified actual cost.
- Forecast reliability is limited by the short historical period.
- Observed revenue leakage must not automatically be interpreted as recoverable cash.

---

## 👩‍💻 Author

**Arushi**

Data Analytics | Python | SQL | Machine Learning | Business Intelligence

- GitHub: https://github.com/arushicoder

---

<p align="center">
  <strong>Turning E-Commerce Data into Actionable Business Intelligence.</strong>
</p>

<p align="center">
  ⭐ If you find this project interesting, consider starring the repository!
</p>

---

*Developed as part of the NYCTA Data Analytics Program.*
>>>>>>> 38c5241 (docs: organize project configuration and documentation)
