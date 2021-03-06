import pandas as pd
from IPython.display import display
items_dict = {

    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 

    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],

    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]

}
purchase_log = {

    'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],

    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 

    'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]

}
items_df = pd.DataFrame(items_dict)
purchase_df = pd.DataFrame(purchase_log)

#1 and 2 and 3
joined = purchase_df.merge(items_df, on='item_id', how='outer')
f=joined.fillna(0)
display('1,2,3', f)

#4
display('4', f['price'] * f['stock_count'])

#5
display('5', sum(f['price'] * f['stock_count']))
