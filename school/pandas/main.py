import pandas as pd
import numpy as np
# data={"name":['q','w','e'],'age':np.arange(1,4)}
# res= pd.DataFrame(data)
data2= pd.read_csv('data.csv')

print(data2,data2['Store'])