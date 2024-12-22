import matplotlib.pyplot as plt

labels=['I','II','III','IV']

x1=[0,1,2,3]
y1=[40,45,35,44]
plt.bar(x1,y1,color='red',width=0.3,label="Bar 1")

x=[0.5,1.5,2.5,3.5]
y=[35,56,20,50]
plt.bar(x,y,color='blue',width=0.3,label="Bar 2")

pos=range(len(x))
plt.xticks(pos,labels)

plt.legend()
plt.title("Bar Graph with ticks")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
