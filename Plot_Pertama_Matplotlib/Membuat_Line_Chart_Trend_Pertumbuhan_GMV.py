# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

import matplotlib.pyplot as plt
import datetime
import pandas as pd
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

# Cara standar untuk menggunakan matplotlib yaitu dengan memanggil function plt.plot
# lalu definisikan nilai di sumbu-x dan sumbu-y. Dalam hal ini, definisikan kolom order_month
# di sumbu-x (parameter pertama), dan kolom gmv di sumbu-y (parameter kedua).
# Setelah selesai mendefinisikan komponen chart-nya, lalu panggil plt.show()untuk menampilkan grafiknya.
plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])
plt.show()
