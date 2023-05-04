import pandas as pd
import os


name = 'users'

table = pd.read_csv(os.path.abspath(f'{name}.csv'), sep=',')
# for obj in objects:
print(list(table['log']) == [])
    
# table.to_csv(os.path.abspath(f'{name}.csv'), index=False)

