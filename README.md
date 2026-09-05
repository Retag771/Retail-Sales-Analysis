# Retail Sales Analytics

### End-to-End Data Analytics Project — SQL · Python · Excel · Power BI

A complete retail analytics case study — from relational database design to an interactive business dashboard.

[Overview](#project-overview) • [Dashboard](#dashboard-preview) • [Database](#database-schema) • [Analysis](#python-analysis-highlights) • [Structure](#repository-structure) • [How to Run](#how-to-use-this-project)

---

## Project Overview

This project simulates a multi-branch retail store and builds a complete analytics pipeline to answer real business questions across sales, profit, products, customers, promotions, and returns.

| Layer | Tool | What it does |
|---|---|---|
| Data Modeling & Querying | SQL Server (T-SQL) | Relational schema (9 tables), bulk data ingestion, business KPI queries |
| Deep-Dive Analysis | Python (Jupyter) | EDA, KPI calculation, RFM segmentation, Pareto analysis, promotion impact, sales forecasting |
| Ad-hoc Reporting | Excel | Pivot tables for quick slicing of sales & profit |
| Business Dashboard | Power BI | 4-page interactive dashboard for stakeholders |

---

## Dashboard Preview

### Home

<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Home(1).png" width="850" alt="Home page of the Power BI dashboard">

### Sales & Profit

<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Sales%20%26%20Profit(1).png" width="850" alt="Sales and profit analysis page">

Total Sales, Total Profit, AOV, sales trend, top profitable products, and sales/profit by country & payment method.

### Product & Promotion

<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Product%26%20Promotion(1).png" width="850" alt="Product and promotion analysis page">

Inventory turnover, gross margin, profit by category/country/discount band, and promotion performance.

### Customers & Returns

<img src="https://github.com/Retag771/Retail-Sales-Analysis/blob/main/Customer(1).png" width="850" alt="Customer and returns analysis page">

Customer count, return rate, refund analysis by reason/category, and top customers by returns.

---

## Database Schema

The relational model includes 9 tables with proper primary/foreign keys and constraints:

`customer` · `Employee` · `product` · `brand` · `supplier` · `orders` · `order_items` · `promotion` · `returns`

Key design choices:
- `CHECK` constraint ensuring `sell_price >= cost_price` on every product
- `payment_method` restricted to `cash`, `card`, `wallet`
- `ON DELETE CASCADE` on `order_items` → `orders`
- Full referential integrity across orders, promotions, products, brands, and suppliers

Example business queries (T-SQL):
- Top 5 best-selling products by quantity
- Monthly revenue trend
- Top 10 customers by spend
- Profit & profit margin by category
- Customers with no orders in the last 3 months (churn watch)
- Low-stock products (`stock_qty < 10`)
- Most-used payment method

Query file: [`Retail_sales_store_project.sql`](Retail_sales_store_project.sql)

---

## Python Analysis Highlights

Notebook: [`https://github.com/Retag771/Retail-Sales-Analysis/blob/main/retail-sales-deep-dive%20(3).ipynb`](retail-sales-deep-dive.ipynb)

| Step | Description |
|---|---|
| Data Quality Audit | Missing values, duplicates, and data type checks across all datasets |
| KPI Calculation | Total revenue, profit, orders, customers, AOV |
| EDA | Revenue & profit by category, top products, brand performance |
| RFM Segmentation | Classifies customers into Champions, Loyal, New, At Risk, etc., each with a tailored retention action |
| Promotion Impact Analysis | Sales/orders with vs. without promotions, and by promotion type |
| Inventory Analysis | Stock levels vs. demand to flag overstock/understock risk |
| Pareto (80/20) Analysis | Identifies which products drive the majority of revenue |
| Sales Forecasting | Linear Regression on monthly trend (MAE, RMSE, R² reported) |
| Correlation Study | Orders are the strongest driver of Sales (r = 0.874, R² = 0.763); Promotions positively influence Orders (r = 0.774) and Sales (r = 0.685) |

---

## Excel Pivot Report

File: [`Retail_project_excel_pivot.xlsx`](Retail_project_excel_pivot.xlsx)

Quick-access pivot tables for slicing sales & profit — built for stakeholders who need answers fast without opening a BI tool.

---

## Key Metrics at a Glance

| Total Sales | Total Profit | Total Orders | AOV | Return Rate |
|:---:|:---:|:---:|:---:|:---:|
| ~$74.6M | ~$48.2K | ~4M | ~$48.8K | ~0.42% |

---

## Repository Structure

```
Retail-Sales-Analysis/
│
├── Retail_sales_store_project.sql     # Schema, constraints, bulk inserts, business queries
├── retail-sales-deep-dive.ipynb       # Full EDA, RFM, Pareto, ML forecasting
├── Retail_project_excel_pivot.xlsx    # Pivot tables for sales & profit
│
├── Home(1).png                        # Power BI dashboard screenshots
├── Sales & Profit(1).png
├── Product& Promotion(1).png
├── Customer(1).png
│
└── README.md
```

---

## How to Use This Project

1. Database — Run `Retail_sales_store_project.sql` in SQL Server Management Studio (update the `BULK INSERT` file paths to your local CSVs first).
2. Analysis — Open `retail-sales-deep-dive.ipynb` in Jupyter/Kaggle/Colab (`pandas`, `numpy`, `seaborn`, `plotly`, `scikit-learn` required).
3. Pivot report — Open `Retail_project_excel_pivot.xlsx` in Excel.
4. Dashboard — Open the `.pbix` file (if included) in Power BI Desktop, or browse the screenshots above.

---

## Tech Stack

SQL Server · Python (pandas, numpy, seaborn, plotly, scikit-learn) · Jupyter Notebook · Microsoft Excel · Power BI

---

## Author

Built as an end-to-end retail analytics case study — from raw relational data to actionable business insight.

If you find this useful, consider starring the repo.

[LinkedIn](#) • [GitHub](#)
