# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

import datetime
import pandas as pd
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())

# Sebelum membuat grafiknya, kita pastikan dulu bahwa datanya sudah siap.
# Kita bisa memanfaatkan library pandas dan numpy untuk mengolah data.
# Untuk membuat grafik GMV bulanan, bayangan kita tentu adalah sebuah line chart
# dengan sumbu-x berupa bulan, dan sumbu-y adalah total GMV di bulan tersebut.


# Ada beberapa function yang berperan di sini:
# 1. apply & lambda biasa digunakan untuk membuat kolom baru, berdasarkan suatu kolom lain yang sudah ada
# (misal .apply(lambda x: x*2) berarti setiap input x di dalam kolom, akan diubah menjadi x*2).
# Dalam hal ini kolom yang sudah ada adalah dataset['order_date'], lalu tiap nilai di dalamnya
# kita proses agar menjadi month-nya saja
# 2. Function datetime.datetime.strptime digunakan untuk mengubah date/time dalam bentuk
# string menjadi tipe data datetime.
# 3. Function  strftime digunakan untuk mengubah format suatu data bertime datetime,
# dalam hal ini diubah menjadi '%Y-%m', yang berarti outputnya adalah waktu dengan bentuk YYYY-MM atau
# tahun dan bulan saja, tanggalnya sudah tidak ada.
