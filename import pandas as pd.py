import pandas as pd
from IPython.display import display

venda = {'data': ['15/02/2023', '16/02/2023'],
             'valor': [500,300],
             'produto': ['feijão', 'arroz'],
             'qtde': [50,70],          
             }

vendas_df = pd.DataFrame(venda)

display(vendas_df)