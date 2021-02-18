# Kita bisa melakukan berbagai modifikasi dengan menambahkan parameter ke dalam function-nya.

# Misalnya, untuk judul/title, parameter yang bisa ditambahkan:
# 1. loc: digunakan untuk menentukan posisi title, misalnya ‘left’ untuk membuat rata kiri,
# ‘right’ untuk rata kanan, dan ‘center’ untuk meletakkannya di tengah. Jika tidak didefinisikan,
# maka defaultnya title ada di tengah.
# 2. pad: digunakan untuk menambahkan jarak antara judul ke grafik (dalam satuan px),
# misalnya kita tidak ingin judulnya terlalu menempel dengan grafiknya, jadi kita beri jarak.
# 3. fontsize: digunakan untuk mengganti ukuran font/huruf (dalam satuan px).
# 4. color: digunakan untuk mengganti warna huruf judul. Kita bisa menggunakan
# warna dasar dengan kata seperti ‘blue’, ‘red’, ‘orange’, dsb.
# Bisa juga dengan hex string, misalnya '#42DDF5' untuk warna biru muda.
# 5.Untuk xlabel dan ylabel, kita bisa mengganti fontsize dan color, tetapi tidak bisa mengganti loc.


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
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019', loc='center',
          pad=40, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()

# Bisa dilihat bahwa judulnya sekarang menjadi lebih besar, agak berjarak ke atas, dan berwarna biru.
# Label di sumbu x maupun y juga menjadi lebih besar dari sebelumnya.
