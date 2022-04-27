import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.pyplot import stem

#Sample size
N=30

read = pd.read_excel("tables/question.xlsx","Sheet1")
data = np.array(read)
data=data.ravel()
data=pd.Series(data)
freq=data.value_counts(sort=False)
write = pd.DataFrame({"No. of heads":[i for i in range(4)],"Frequency":freq})
write.to_excel("tables/output.xlsx",index=False)

#Plotting PMF from the given data
X = np.array([3,2,1,0])
Y = np.array([freq[0]/N,freq[1]/N,freq[2]/N,freq[3]/N])
fig1 = stem(X, Y, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.grid('minor')
plt.savefig("figs/PMF1.png")

#Plotting PMF to compare theoretical and practical
X = np.array([0,1,2,3])
Y = np.array([1/8,3/8,3/8,1/8])
fig2 = stem(X, Y, linefmt='k-', markerfmt='ro', basefmt='k-')
plt.grid('minor')
plt.text(2.2,0.32,"o - Theoretical",color = 'red')
plt.text(2.2,0.3,"o - Practical",color = 'black')
plt.savefig("figs/PMF2.png")