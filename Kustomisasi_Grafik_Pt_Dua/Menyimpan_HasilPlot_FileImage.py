# Kita bisa menyimpan sebagai file gambar dengan function savefig sebelum plt.show()

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
plt.savefig('monthly_gmv.png')
plt.show()

# Kita bisa menyimpannya ke berbagai tipe file, seringnya sih jpg, png, atau kadang pdf juga bisa.
# Untuk mengetahui format lengkapnya, kita bisa menggunakan code berikut:
# plt.gcf().canvas.get_supported_filetypes()
# tipe-tipe file yang support untuk menyimpan hasil nya :
# 1. 'ps' : 'Postcript'
# 2. 'eps' : 'Encapsulated Postcript'
# 3. 'pdf' : 'Portable Document Format'
# 4. 'pgf' : 'PGF code for LaTex'
# 5. 'png' : 'Portable Netwokr Graphics'
# 6. 'raw' : 'Raw RGBA bitmap'
# 7. 'rgba' : 'Raw RGBA bitmap'
# 8. 'svg' : 'Scalable Vector Graphics'
# 9. 'svgz' : 'Scalable Vector Graphics'
# 10. 'jpg' : 'Joint Photographic Experts Group'
# 11. 'jpeg' : 'Joint Photographic Experts Group'
# 12. 'tif' : 'Tagged Image File Format'
# 13. 'tiff' : 'Tagged Image File Format'
