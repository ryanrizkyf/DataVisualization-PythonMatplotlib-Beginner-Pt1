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

# Dengan pendekatan lain, dimungkinkan juga melakukan
# visualisasi dengan matplotlib tanpa membuat variabel baru.
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()

# Grafik yang dihasilkan pun serupa kan?
# Dengan begini, sudah bisa lihat GMV dari bulan ke bulan. Selesai deh line chart nya
