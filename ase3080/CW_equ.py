import numpy as np
from matplotlib import pyplot as plt

r_c = 7000 #km
mu = 398600 #km^3/s^2
n = np.sqrt(mu/(r_c)**3)
r0 = [np.sqrt(2)/2, 3-np.sqrt(2), 0]
v0 = [-np.sqrt(2)/2*n, -np.sqrt(2)*n, 0]

T = 2*np.pi/n
t_span = np.linspace(0,T,101)

x_t = lambda t : (v0[0]/n)*np.sin(n*t) - (3*r0[0]+2*v0[1]/n)*np.cos(n*t) + 4*r0[0] + 2*v0[1]/n
#np.cos(n*t) 
y_t = lambda t : 2*(v0[0]/n)*np.cos(n*t) + (6*r0[0]+4*v0[1]/n)*np.sin(n*t) - (6*n*r0[0] + 3*v0[1])*t - 2*v0[0]/n + r0[1]
#-2*np.sin(n*t) + 3

v_r = lambda t : v0[0]*np.cos(n*t) + (3*r0[0]*n+2*v0[1])*np.sin(n*t)
v_t = lambda t : -2*v0[0]*np.sin(n*t) + (6*r0[0]*n+4*v0[1])*np.cos(n*t) - (6*n*r0[0] + 3*v0[1])

print(f'first relative position{x_t(0),y_t(0)}') #초기 위치가 동일함을 보임
print(f'first relative velocity{v_r(0),v_t(0)}') #초기 속도가 동일함을 보임
plt.plot(y_t(t_span),x_t(t_span), label = 'relative orbit')
plt.scatter(y_t(0), x_t(0), label = 'first position', color = 'red')
plt.xlabel('T(y)[km]')
plt.ylabel('R(x)[km]')
plt.legend()
plt.grid(True)
plt.show()