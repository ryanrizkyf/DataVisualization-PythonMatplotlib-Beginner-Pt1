# Di sini dapat dilihat bahwa nilai terkecil di sumbu-y adalah 150.
# Ini kadang bisa membuat orang tertipu sih, seakan-akan GMV di bulan Oktober naik
# menjadi hampir 3 kali lipat dari September. Untuk itu sebaiknya diset agar sumbu-y nya
# dimulai dari 0, cukup tambahkan plt.ylim(ymin=0)

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
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.show()

# Untuk mengatur batas maksium, kita tambahkan juga parameter ymax,
# tetapi sepertinya di sini tidak perlu. Kita juga bisa mengatur batas minimum dan maksimum
# sumbu-x dengan function plt.xlim.
