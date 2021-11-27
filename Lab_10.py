import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *
x = [0,1.4,2.3,3.3,4.5]
y = [1.83,2.14,1.46,1.15,3.28]
spl = UnivariateSpline(x,y)
xs = linspace(0,4.5, 1000)
plt.plot(x,y,'ro',xs, spl(xs),'g')
plt.title('Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(x)
plt.grid()
plt.show()
