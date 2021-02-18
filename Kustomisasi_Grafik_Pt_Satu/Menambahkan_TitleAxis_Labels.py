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

# Beberapa hal yang lazim dimodifikasi pada sebuah grafik adalah judul (title) dan
# label di sumbu-x & sumbu-y (axis labels).

# Untuk menambahkannya, tinggal menambah plt.title, plt.xlabel, dan plt.ylabel di code sebelum plt.show(),
# misalnya seperti ini:
plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019')
plt.xlabel('Order Month')
plt.ylabel('Total GMV')
plt.show()

# Sekarang terlihat bahwa chart ini sudah memiliki judul, dan label teks di kedua sumbunya.
