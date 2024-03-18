# -*- coding: utf-8 -*-
"""Python_internal_assesment-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_o07dX4kyU8f42jP9lKSPtRBssl4kLpW

1
"""

import pandas as pd
import numpy as np

data=np.array([[[255,0,0],[0,255,0],[0,0,255]],
               [[255,255,0],[255,0,255],[0,255,255]],
               [[127,127,127],[200,200,200],[50,50,50]]])
data1=data[0]*0.2989+data[1]*0.5870+data[2]*0.1140
print(data1)

"""2"""

import pandas as pd
import numpy as np

data=np.array([[10.,20.,12.],[10.,23.,14]])
def normalizes(data):
  std=data.std()
  mean=data.mean()
  return std-(std-1),mean-mean

print(normalizes(data))

"""3"""

import pandas as pd
import numpy as np

data=[[1,3,3,5,6],[1,2,3,4,5]]
df=np.array(data)
df2=df.reshape(4,2)
print(df2)

"""4"""

import pandas as pd
import numpy as np

data=[[12,23,45,56],[12,34,56,78]]
df=np.array(data,index=['Row1','Row2'])
print(df)

"""5"""

import pandas as pd
import numpy as np

data=[[12,34,5,6],[12,34,45,56]]

a=np.array(data)
b=a.sum()/len(a)
print(b)

"""6"""

import pandas as pd
import numpy as np
def broadcasting(a,b):
  c=np.abs(a['temp']-b)
  return c

data={
    'city':['tel','chennai','mayapur'],
    'temp':[10.2,38.4,87.0],
}
data_temp_sen=[12.,3.,4.0]

a=np.array(data)
b=np.array(data_temp_sen)

print(broadcasting(a,b))

"""7"""

import pandas as pd
import numpy as np
data={
    'Name':['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
    'Age':[25,30,35,40,45,50,55],
    'City':['New York','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
    'Department':['Hr','It','Finanace','Marketing','Sales','It','Hr']
}

df=pd.DataFrame(data)
df2=df[(df['Department']!='Hr') & (df['Age']<45)]
df3=df2['Name','City']
print(df3)

"""8"""

import pandas as pd
import numpy as np
data={
    'Product':['Apples','Banana','Cherries','Dates'],
    'Category':['Fruit','Fruit','Fruit','Fruit'],
    'Price':[1.20,0.50,3.00,2.50],
    'Promotion':[True,False,True,True]

}

df=pd.DataFrame(data)
df2=df[(df['Category']=='Fruit') & (df['Promotion']==False)]
print(df2)

"""9"""

import pandas as pd
import numpy as np
Employee_data={
    'Employee':['Alice','Bob','Charlie','David'],
    'Department':['HR','IT','Finance','IT'],
    'Manager':['john','Rachel','Emily','Rachel']
}
Project_data={
    'Employee':['Alice','Charlie','Eve'],
    'Project':['P1','P2','P3']
}

df1=pd.DataFrame(Employee_data)
df2=pd.DataFrame(Project_data)
df3=pd.merge(df1,df2, on='Employee',how='left')
print(df3)

"""10"""

import pandas as pd
import numpy as np

data={'Department':['Electronics','Electronics','Clothing','Clothing','Home','Goods'],
      'Salesperson':['Alice','Bob','Charlie','David','Eve',None],
      'Sales':[70000,50000,40000,60000,None,None]}
df=pd.DataFrame(data)
df2=df.groupby('Department').aggregate({'Sales':['sum']})
df3=df2.sort_values('Sales')
print(df2)