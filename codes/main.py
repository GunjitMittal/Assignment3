import numpy as np
import pandas as pd
read = pd.read_excel("question.xlsx","Sheet1")
data = np.array(read)
values = list(data[0])+list(data[1])+list(data[2])
a0 = values.count(0)
a1 = values.count(1)
a2 = values.count(2)
a3 = values.count(3)
no_of_heads = [0,1,2,3]
frequencies = [a0,a1,a2,a3]
write = pd.DataFrame({"No. of heads":no_of_heads,"Frequency":frequencies})
write.to_excel("output.xlsx",index=False)