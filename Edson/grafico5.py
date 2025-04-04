import matplotlib.pyplot as plt #Como fazer graficos 


a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=(1,2,3,4,5)
d=(1,2,3,4,5)

plt.subplot(1,2,1)
plt.plot(a,b)

plt.subplot(1,2,2)
plt.plot(c,d)

"""plt.suplot(1,2,1)# linha coluna e elemento"""
plt.show()