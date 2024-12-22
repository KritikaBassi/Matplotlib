#Histogram
import matplotlib.pyplot as plt

weight=[7,8,9,10,11,13,13,15,23,26,27,27,31,34,35,35,35,41,42,42,48,49,49,51,52,52]
ran=[5,15,25,35,45,55]#For intervals
plt.hist(weight,bins=ran,facecolor='yellow',edgecolor='red')
#bin is not compulsory and its default value is 10
plt.show()
