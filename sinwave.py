import matplotlib.pyplot as plt
import numpy as np
i = 0
j = 0
x = []
y = []
while i <1000:
    x.append(i/100)
    i +=1

while j<1000:
    y.append(np.sin(x[j]*8))
    j+=1

plt.plot(x,y)
plt.show()
