import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,15,20,15]
plt.plot(x,y,'b--',label='First Line')

x1=[2,3,4,5]
y1=[30,40,60,50]
plt.plot(x1,y1,':',label='Second Line')

plt.title('Sample Gragh')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()
#b for blue colour
#k is for black colour
#We can write b or blue 
# -- is for dashed line
# -. is for -. line
# : is for dotted line
# - is for plane/solid line
