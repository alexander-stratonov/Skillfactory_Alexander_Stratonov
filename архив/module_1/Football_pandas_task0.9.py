import pandas as pd
from IPython.display import display
df = pd.read_csv('C:/Users/user/Downloads/data_sf.csv')
#df = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/data_sf.csv')
#small_df = df[df.columns[1:8]].head(25)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(small_df)
df_groupby = df.groupby('Club')['Wage'].agg(['mean', 'median']).reset_index()
df_groupby.columns = ['CLUB', 'MEAN', 'MEDIAN']
#1
display(df_groupby[df_groupby['MEAN']==df_groupby['MEDIAN']].shape[0])
#2
display(df_groupby[df_groupby['MEAN']==df_groupby['MEDIAN']])

