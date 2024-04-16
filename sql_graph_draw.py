import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[3,5,8,9]
# plt.bar(x,y,fc='b')
# plt.barh(x,y,fc='b')
plt.pie(y,labels=x)
# plt.plot(x,y,ls='-.',color='r',marker = 'o',mfc = 'green') #color as shortly "c" - mfc is marker color

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Graph')

plt.show() # to show the graph
