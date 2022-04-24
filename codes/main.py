import numpy as np
import pandas as pd
read = pd.read_excel("question.xlsx","Sheet1")
data = np.array(read)
data=data.ravel()
data=pd.Series(data)
freq=data.value_counts(sort=False)
write = pd.DataFrame({"No. of heads":[i for i in range(4)],"Frequency":freq})
write.to_excel("output.xlsx",index=False)