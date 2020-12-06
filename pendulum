import math
import matplotlib.pyplot as plt

theta = (2 * math.pi / 360) * float(input("Theta_0: "))
theta_dot = float(input("Theta'_0: "))

g = 9.81
l = float(input("Length: "))
mu = float(input("mu: "))

t = 0
t_f = float(input("Final t: "))
delta_t = 0.01

def theta_ddot(theta,theta_dot):
    return -(g / l) * math.sin(theta) - mu * theta_dot 

T = []
THETA = []
THETA_DOT = []

while t < t_f:
    T.append(t)
    THETA.append(theta)
    THETA_DOT.append(theta_dot)

    theta = theta + delta_t * theta_dot
    theta_dot = theta_dot + delta_t * theta_ddot(theta,theta_dot)

    t = t + delta_t
    
plt.plot(T,THETA)
plt.show()
