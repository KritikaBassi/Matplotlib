#Bar Graph Practice
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[30,40,50,60,70]

plt.bar(x,y,facecolor='blue',edgecolor='red',width=0.5,align='edge')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Practice')
plt.show()
