# Ada baiknya kita menambahkan beberapa informasi di dalamnya agar
# pembaca mendapatkan insight dari grafik tersebut.

# Dilihat dari trend-nya, mulai bulan Oktober 2019, GMV kita naik drastis setelah sebelumnya
# stagnan di angka 200-300 milyar per bulan. Kita bisa mulai dengan menambahkan info ini di grafik.

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

fig = plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(
    color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center',
          pad=40, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019',
         transform=fig.transFigure, color='red')
plt.show()

# Perhatikan bahwa ada beberapa parameter yang diset saat menggunakan plt.text.
# Dua angka pertama itu adalah koordinat, x dan y. Saat set transform=fig.transFigure,
# maka koordinatnya berkisar 0 sampai 1 (untuk x dari kanan ke kiri, dan untuk y, dari bawah ke atas).

# Jika parameter transform tidak diisi, maka koordinatnya dalam satuan inch
# (Dalam contoh ini, dari 0-15 dari kiri ke kanan, dan 0-5 dari bawah ke atas).
# Seperti halnya title atau label, dimungkinkan juga untuk set warna dan ukuran hurufnya.
