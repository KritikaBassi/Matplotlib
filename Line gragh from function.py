import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=2*x + 10

plt.plot(x,y)
plt.title('Sample Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
