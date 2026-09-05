# Retail-Sales-Analysis
<div align="center">

# 🛍️ Retail Sales Analytics
### End-to-End Data Analytics Project — SQL · Python · Excel · Power BI

![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

*A complete retail analytics case study — from relational database design to an interactive business dashboard.*

[Overview](#-project-overview) • [Dashboard](#-dashboard-preview) • [Database](#-database-schema) • [Analysis](#-python-analysis-highlights) • [Structure](#️-repository-structure) • [How to Run](#-how-to-use-this-project)

</div>

---

## 📌 Project Overview

This project simulates a multi-branch retail store and builds a complete analytics pipeline to answer real business questions across **sales, profit, products, customers, promotions, and returns**.

| Layer | Tool | What it does |
|---|---|---|
| 🗄️ **Data Modeling & Querying** | SQL Server (T-SQL) | Relational schema (9 tables), bulk data ingestion, business KPI queries |
| 🐍 **Deep-Dive Analysis** | Python (Jupyter) | EDA, KPI calculation, RFM segmentation, Pareto analysis, promotion impact, sales forecasting |
| 📋 **Ad-hoc Reporting** | Excel | Pivot tables for quick slicing of sales & profit |
| 📊 **Business Dashboard** | Power BI | 4-page interactive dashboard for stakeholders |

---

## 📊 Dashboard Preview

<div align="center">

### 🏠 Home
<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Home(1).png" width="850" alt="Home page of the Power BI dashboard">

### 💰 Sales & Profit
<img src="dashboard/2_sales_profit.png" width="850" alt="Sales and profit analysis page">

*Total Sales, Total Profit, AOV, sales trend, top profitable products, and sales/profit by country & payment method.*

### 📦 Product & Promotion
<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Product%26%20Promotion(1).png" width="850" alt="Product and promotion analysis page">

*Inventory turnover, gross margin, profit by category/country/discount band, and promotion performance.*

### 👥 Customers & Returns
<img src="dashboard/4_customer_returns.png" width="850" alt="Customer and returns analysis page">

*Customer count, return rate, refund analysis by reason/category, and top customers by returns.*

</div>

> 💡 *Screenshots above load automatically from the `dashboard/` folder — make sure the 4 PNG files keep their exact names when you add them.*

---

## 🧱 Database Schema

The relational model includes **9 tables** with proper primary/foreign keys and constraints:

`customer` · `Employee` · `product` · `brand` · `supplier` · `orders` · `order_items` · `promotion` · `returns`

**Key design choices:**
- ✅ `CHECK` constraint ensuring `sell_price >= cost_price` on every product
- ✅ `payment_method` restricted to `cash`, `card`, `wallet`
- ✅ `ON DELETE CASCADE` on `order_items` → `orders`
- ✅ Full referential integrity across orders, promotions, products, brands, and suppliers

**Example business queries (T-SQL):**
- 🏆 Top 5 best-selling products by quantity
- 📈 Monthly revenue trend
- 👑 Top 10 customers by spend
- 💵 Profit & profit margin by category
- ⚠️ Customers with no orders in the last 3 months (churn watch)
- 📉 Low-stock products (`stock_qty < 10`)
- 💳 Most-used payment method

📄 [`sql/retail_sales_store_project.sql`](sql/retail_sales_store_project.sql)

---

## 🐍 Python Analysis Highlights

📄 [`notebook/retail_sales_deep_dive.ipynb`](notebook/retail_sales_deep_dive.ipynb)

| # | Step | Description |
|---|---|---|
| 1 | **Data Quality Audit** | Missing values, duplicates, and data type checks across all datasets |
| 2 | **KPI Calculation** | Total revenue, profit, orders, customers, AOV |
| 3 | **EDA** | Revenue & profit by category, top products, brand performance |
| 4 | **RFM Segmentation** | Classifies customers into Champions, Loyal, New, At Risk, etc., each with a tailored retention action |
| 5 | **Promotion Impact Analysis** | Sales/orders with vs. without promotions, and by promotion type |
| 6 | **Inventory Analysis** | Stock levels vs. demand to flag overstock/understock risk |
| 7 | **Pareto (80/20) Analysis** | Identifies which products drive the majority of revenue |
| 8 | **Sales Forecasting** | Linear Regression on monthly trend (MAE, RMSE, R² reported) |
| 9 | **Correlation Study** | Orders are the strongest driver of Sales (**r = 0.874, R² = 0.763**); Promotions positively influence Orders (r = 0.774) and Sales (r = 0.685) |

---

## 📋 Excel Pivot Report

📄 [`excel/retail_project_excel_pivot.xlsx`](excel/retail_project_excel_pivot.xlsx)

Quick-access pivot tables for slicing sales & profit — built for stakeholders who need answers fast without opening a BI tool.

---

## 📈 Key Metrics at a Glance

<div align="center">

| 💵 Total Sales | 💰 Total Profit | 🧾 Total Orders | 🛒 AOV | 📉 Return Rate |
|:---:|:---:|:---:|:---:|:---:|
| **~$74.6M** | **~$48.2K** | **~4M** | **~$48.8K** | **~0.42%** |

</div>

---

## 🗂️ Repository Structure

```
retail-sales-analytics/
│
├── sql/
│   └── retail_sales_store_project.sql     # Schema, constraints, bulk inserts, business queries
│
├── notebook/
│   └── retail_sales_deep_dive.ipynb       # Full EDA, RFM, Pareto, ML forecasting
│
├── excel/
│   └── retail_project_excel_pivot.xlsx    # Pivot tables for sales & profit
│
├── dashboard/
│   ├── 1_home.png
│   ├── 2_sales_profit.png
│   ├── 3_product_promotion.png
│   └── 4_customer_returns.png
│
└── README.md
```

---

## 🚀 How to Use This Project

1. **Database** — Run `sql/retail_sales_store_project.sql` in SQL Server Management Studio (update the `BULK INSERT` file paths to your local CSVs first).
2. **Analysis** — Open `notebook/retail_sales_deep_dive.ipynb` in Jupyter/Kaggle/Colab (`pandas`, `numpy`, `seaborn`, `plotly`, `scikit-learn` required).
3. **Pivot report** — Open `excel/retail_project_excel_pivot.xlsx` in Excel.
4. **Dashboard** — Open the `.pbix` file (if included) in Power BI Desktop, or browse the screenshots above.

---

## 🛠️ Tech Stack

`SQL Server` · `Python` (pandas, numpy, seaborn, plotly, scikit-learn) · `Jupyter Notebook` · `Microsoft Excel` · `Power BI`

---

<div align="center">

### 👤 Author

Built as an end-to-end retail analytics case study — from raw relational data to actionable business insight.

⭐ **If you find this useful, consider starring the repo!** ⭐

[LinkedIn](#) • [GitHub](#)

</div>
