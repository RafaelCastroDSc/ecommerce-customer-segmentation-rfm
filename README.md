# 📊 E-Commerce Customer Segmentation & RFM Analysis

## 📌 Executive Summary

This project delivers an end-to-end customer segmentation analysis for an e-commerce platform using the **RFM (Recency, Frequency, Monetary)** model. By analyzing transactional patterns, customers are categorized into distinct behavioral tiers to optimize retention strategies, marketing spend, and Customer Lifetime Value (CLV).

---

## 🏗️ Project Architecture

```text
ecommerce-customer-segmentation-rfm/
│
├── data/
│   └── ecommerce_rfm_data.csv    # Transactional e-commerce dataset
├── scripts/
│   └── rfm_analysis.py           # Data transformations & RFM score calculation
└── README.md                     # Project documentation

```

---

## 🛠️ Tech Stack & Methods

* **SQL / Python (Pandas)**: Data processing, date aggregation, and quantile-based segmentation (`qcut`).
* **RFM Framework**:
* **Recency (R)**: Days since last order.
* **Frequency (F)**: Total distinct completed orders.
* **Monetary (M)**: Total transaction revenue.



---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/RafaelCastroDsC/ecommerce-customer-segmentation-rfm.git

```


2. Run the analysis script:
```bash
python scripts/rfm_analysis.py

```
