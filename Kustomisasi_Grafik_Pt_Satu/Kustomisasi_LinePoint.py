# Untuk mengubah style dari garis maupun titik di chart,
# cukup dengan menambahkan parameter di function .plot().
# Beberapa parameter yang bisa dikustomisasi:
# 1. color: mengubah warnanya (sama seperti di title)
# 2. linewidth: mengubah ketebalan line/garisnya (dalam satuan px)
# 3. linestyle: mengubah jenis dari garis. Misalnya '-' atau 'solid' untuk garis tak terputus
# (seperti pada default), '--' atau 'dashed' untuk garis putus-putus, ':' atau 'dotted' untuk
# garis berupa titik-titik, bisa juga '-.' atau ‘dashdot’ untuk garis dan titik bergantian.
# 4. marker: mengubah tipe points/titik data di chart. Ada banyak sekali kemungkinan nilai untuk marker ini,
# yang biasanya digunakan yaitu ‘.’ untuk bulatan kecil/titik, ‘o’ untuk bulatan agak besar, ‘s’ untuk persegi,
# ‘D’ untuk diamond/wajik, dan bentuk-bentuk lain seperti ‘+’, ‘x’, ‘|’, ‘*’.

# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

import pandas as pd
import datetime
import matplotlib.pyplot as plt
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(
    color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center',
          pad=40, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()
