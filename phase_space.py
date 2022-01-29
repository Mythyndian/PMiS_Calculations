import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

t = np.linspace(0, 20, 10000)
x = [2, 0]
delta = 0.62
k = 30.5
m = 59


def sho(t, x):
    result = (x[1], (-2*delta*x[1]-(k/m)*x[0]))
    return result


solution = solve_ivp(sho, [0, 10000], y0=x, t_eval=t)
plt.plot(solution.y[0], solution.y[1], color='b')
# plt.axis([0, 6, -1.4, 0])
plt.title('Przestrzeń fazowa', fontsize=20)
plt.xlabel("x")
plt.ylabel("v")
plt.grid(True)
plt.show()
