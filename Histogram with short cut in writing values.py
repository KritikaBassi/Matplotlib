#Histogram with short cut in writing values
import matplotlib.pyplot as plt

x=[12,22,25,27,38,42,43,51]
values=[10,4,7,6,5,12,7,9]

ran=[10,15,20,25,30,35,40,45,50,55]
plt.hist(x,bins=ran,weights=values,facecolor='blue',edgecolor='red')
#x contains the values
#weights is used for frequency of different values
#ran contains the intervals
plt.show()
