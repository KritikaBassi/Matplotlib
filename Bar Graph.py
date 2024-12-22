#Bar Graph
import matplotlib.pyplot as plt

x=['IP','Physics','Accountancy','Arts']
y=[10,12,5,9]

plt.bar(x,y,color='magenta',width=0.5,align='edge')

plt.title('Subject liking graph')
plt.xlabel('Subject')
plt.ylabel('No. of students')

plt.show()

