# dataset = 'https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv'),
# buatlah sebuah line chart dengan Matplotlib, yang menunjukkan jumlah pembeli harian
# (daily number of customers) selama bulan Desember.

# Beberapa spesifikasi yang harus diperhatikan:
# 1. Ukuran figure adalah 10x5
# 2. Sumbu-x adalah tanggal pembelian, dari tanggal 1 - 31 Desember 2019
# 3. Sumbu-y adalah jumlah unique customers di tiap tanggal
# 4. Title dan axis label harus ada, tulisan dan style-nya silakan disesuaikan sendiri

# Import library yang dibutuhkan
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# Baca dataset retail_raw_reduced.csv
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
# Buat kolom order_month
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
# Buat kolom gmv
dataset['gmv'] = dataset['item_price'] * dataset['quantity']
# Plot grafik sesuai dengan instruksi
plt.figure(figsize=(10, 5))
dataset[dataset['order_month'] == '2019-12'].groupby(
    ['order_date'])['customer_id'].nunique().plot(color='red', marker='.', linewidth=2)
plt.title('Daily Number of Customers - December 2019',
          loc='left', pad=30, fontsize=20, color='orange')
plt.xlabel('Order Date', fontsize=15, color='blue')
plt.ylabel('Number of Customers', fontsize=15, color='blue')
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.show()
