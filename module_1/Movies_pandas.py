import pandas as pd
from IPython.display import display
#ratings = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/ratings.csv')
#movies = pd.read_csv('C:/Users/Крис/Documents/GitHub/Skillfactory_Alexander_Stratonov/movies.csv')
ratings = pd.read_csv('C:/Users/user/Downloads/ratings.csv')
movies = pd.read_csv('C:/Users/user/Downloads/movies.csv')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    display(df)
joined = ratings.merge(movies, on='movieId', how='left')
with pd.option_context('display.max_columns', None):
    display(joined) 
print(len(ratings) == len(joined))