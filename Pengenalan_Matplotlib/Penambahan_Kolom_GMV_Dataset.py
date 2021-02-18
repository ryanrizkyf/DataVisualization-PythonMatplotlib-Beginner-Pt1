# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

# Selanjutnya, bagaimana dengan GMV? Definisikan GMV adalah perkalian setiap entri di kolom item_price
# dan kolom quantity. Bisa saja menggunakan fungsi apply & lambda seperti tadi,
# tetapi ada cara yang lebih mudah yaitu dengan mengalikan kedua kolom yang disebutkan secara langsung.

import pandas as pd
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

# Sekarang isi dataframe menjadi seperti ini, sudah ada kolom order_month dan gmv.
