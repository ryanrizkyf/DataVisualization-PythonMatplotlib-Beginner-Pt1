# Resolusinya dapat kita atur juga agar hasil gambarnya lebih berkualitas.
# Terdapat beberapa parameter yang harus kita ingat.

# Ada berbagai parameter yang bisa diatur saat menyimpan gambar, antara lain:
# 1. dpi: Resolusi gambar (dots per inch).
# 2. quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg),
# bisa diisi nilai 1 (paling buruk) hingga 95 (paling bagus).
# 3. facecolor: Memberikan warna bagian depan figure, di luar area plot
# 4. edgecolor: Memberikan warna pinggiran gambar
# 5. transparent: Jika nilainya True, maka gambarnya jadi transparan (jika filenya png)

# Tapi biasanya, parameter-parameter ini tidak digunakan karena grafik di file gambar
# bisa jadi berbeda dengan yang muncul saat menjalankan code di python.

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
# Yang akan menghasilkan kualitas gambar yang tersimpan sebesar 95% dari awal.
plt.savefig('monthly_gmv.png', quality=95)
plt.show()
