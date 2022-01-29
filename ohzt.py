import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

t = np.linspace(0, 50, 1000)
#x, x'
x = [0, 1]
x_2 = [1, 0]
delta = 0.62
k = 30.5
m = 59


def sho(t, x):
    # x[1] -> x' 
    result = [x[1], (-2 * delta * x[1] - k / m * x[0])]
    return result


def sho_2(t, x_2):
    result = [x_2[1], (-2 * delta * x_2[1] - k / m * x_2[0])]
    return result


solution = solve_ivp(sho, [0, 1000], y0=x, t_eval=t)
solution_2 = solve_ivp(sho_2, [0, 1000], y0=x_2, t_eval=t)
plt.plot(t, solution.y[0], 'b')
plt.plot(t, solution_2.y[0], 'orange')
plt.legend(["x(0) = 0; x'(0) = 1", "x(0) = 1; x'(0) = 0"])
plt.xlabel("Czas")
plt.ylabel("Wychylenie")
plt.title('Oscylator harmoniczny z tłumieniem', fontsize=20)
plt.grid(True)
plt.show()
