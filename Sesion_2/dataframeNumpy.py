import pandas as pd
import numpy as np

data=np.array([[1,2,3],[4,5,6],[7,8,9]])
dataArray=pd.DataFrame(data, columns=['A','B','C'])
print(dataArray)

data_n=[{'ID':1,
       'Name':'Erika',
       'Age': 25 }]
dataDicc=pd.DataFrame(data_n)
print(dataDicc)

