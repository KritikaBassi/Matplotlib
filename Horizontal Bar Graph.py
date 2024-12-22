import matplotlib.pyplot as plt

x=['IP','Physics','Accountancy','Arts']
y=[10,12,5,9]

plt.barh(x,y,color='red',width=0.5,align='edge')

plt.title('Subject liking graph')
plt.xlabel('Subject')
plt.ylabel('No. of students')

plt.show()
