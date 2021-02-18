# dataset = https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/retail_raw_reduced.csv

import datetime
import pandas as pd
dataset = pd.read_csv(
    'retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)
