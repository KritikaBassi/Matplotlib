import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,15,20,15]

plt.subplot(2,1,1)
plt.plot(x,y,'b--',label='First Line')

plt.title('Sample Gragh')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

x1=[2,3,4,5]
y1=[30,40,60,50]
plt.subplots_adjust(hspace=0.5)
#To adjust the space between tow graphs
plt.subplot(2,1,2)
plt.plot(x1,y1,':',label='Second Line')

plt.title('Sample Gragh')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()
#subplot is used to plot two graghs in the same window
#subplot(rows,columns,garphno.)

