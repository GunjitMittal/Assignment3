from tabulate import tabulate
import numpy as np
import pandas as pd
read = pd.read_excel(r'question.xlsx')
data = np.array(read)
l=len(data)
k=len(data[0])
a0=0;a1=0;a2=0;a3=0
for i in range(l):
    for j in range(k):
        if (data[i][j]==0):
            a0+=1
        if (data[i][j]==1):
            a1+=1
        if (data[i][j]==2):
            a2+=1
        if (data[i][j]==3):
            a3+=1
dat = [[0,a0],
[1,  a1],
[2, a2],
[3, a3]]
print(tabulate(dat, headers=["No. of heads", "Frequency"]))