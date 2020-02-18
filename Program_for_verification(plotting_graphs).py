import numpy as np 
import matplotlib.pyplot as plt 
from pylab import *

t = np.linspace(0,20,1000)
t1 = np.linspace(0,3,100)

x1 = np.sin(t1) #input to the system.

y_o = np.cos(t) - np.exp(-t) #steady state output of the system
y_o1 = np.cos(t1) - np.exp(-t1) #for plotting wrt t1 .thats it.

y1 = np.cos(t)
y2 = -np.exp(-t)
subplot(2,1,1)
plt.plot(t1,x1,'g',label = 'Input x(t) = sin(t)')
plt.plot(t1,y_o1,'b',label = 'Resultant output y(t)')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('The input & output of the system in t-domain')

subplot(2,1,2)
plt.plot(t,y_o,'b',label = 'Resultant output y(t)')
plt.plot(t,y1,'k',linestyle='dashed',label= 'steady state output :cos(t)')
plt.plot(t,y2,'r',linestyle='dashed',label = '-e$^{-t}$')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('The output of the system in t-domain')
plt.show()

