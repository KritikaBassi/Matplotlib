import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-1,0,0.1)
y=np.sin(x)

plt.plot(x,y)
plt.title('Sample Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
