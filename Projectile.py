import math
import matplotlib.pyplot as plt

#constants

m = float(input("Mass: "))
c_d = float(input("Coefficient of Air Resistance: "))
rho = float(input("Density of Fluid: "))
A = float(input("Cross Sectional Area: "))
k = (1 / 2) * c_d * rho * A
g = 9.81

#initial values and func

x_0 = float(input("x_0: "))
y_0 = float(input("y_0: "))
u_0 = float(input("u_0: "))
v_0 = float(input("v_0: "))

x = x_0
y = y_0
u = u_0
v = v_0

X = []
Y = []
U = []
V = []

#time stuff

delta_t = 0.001
t = 0

#the fun stuff

def F_x(x,y,u,v):
    if k == 0:
        return 0
    else:
        return -k * math.sqrt(u ** 2 + v ** 2) * u
    
def F_y(x,y,u,v):
    if k == 0:
        return -m * g
    else:
        return -m * g - k * math.sqrt(u ** 2 + v ** 2) * v
    

while y > 0:
    X.append(x)
    Y.append(y)
    U.append(u)
    V.append(v)

    x = x + delta_t * u
    y = y + delta_t * v
    u = u + delta_t * F_x(x,y,u,v) / m
    v = v + delta_t * F_y(x,y,u,v) / m

plt.plot(X,Y)
plt.show()

