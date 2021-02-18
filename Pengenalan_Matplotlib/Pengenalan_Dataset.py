# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

import pandas as pd
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

# Di sini terlihat bahwa kita punya 5000 barisdata, dan terdiri dari 9 kolom.
