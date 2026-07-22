import pandas as pd
from datetime import datetime

# 1. Cargar dataset transaccional
df = pd.read_csv('data/ecommerce_rfm_data.csv')
df['order_date'] = pd.to_datetime(df['order_date'])
df['total_spend'] = df['quantity'] * df['unit_price']

# 2. Definir fecha de referencia para Recency
snapshot_date = df['order_date'].max() + pd.Timedelta(days=1)

# 3. Calcular métricas RFM por cliente
rfm = df.groupby('customer_id').agg({
    'order_date': lambda x: (snapshot_date - x.max()).days, # Recency
    'order_id': 'nunique',                                  # Frequency
    'total_spend': 'sum'                                    # Monetary
}).reset_index()

rfm.rename(columns={
    'order_date': 'Recency_Days',
    'order_id': 'Frequency',
    'total_spend': 'Monetary'
}, inplace=True)

# 4. Asignar Scores RFM (1-3)
rfm['R_Score'] = pd.qcut(rfm['Recency_Days'], q=3, labels=[3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=3, labels=[1, 2, 3])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], q=3, labels=[1, 2, 3])

rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

print("--- Resumen RFM ---")
print(rfm.head())
