import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.exp(np.sin(x))


x = np.array([i * 0.1 for i in range(1, 11)])  # задаємо x генератором списків
y = np.array([func(x)])
print('x=', x)
print('y=', y)
mean_x = np.mean(x)  # середнє значення х
mean_y = np.mean(y)  # cереднє значення y
mean_x2 = np.mean(x ** 2)
mean_xy = np.mean(x * y)
print('mean_x=', mean_x, '\n', 'mean_y=', mean_y, '\n', 'mean_xy=', mean_xy, '\n',
      'mean_x2=', mean_x2)
a1 = (mean_xy - mean_x * mean_y) / (mean_x2 - (np.mean(x) ** 2))
a0 = mean_y - (a1 * mean_x)

print('Coefficients', 'a0=', round(a0, 2), 'a1=', round(a1, 2))
plt.plot(x, a1 * x + a0, 'r', label='Fitted line')
plt.scatter(x, y, label='Scatter Plot')
plt.title(f'f(x)={a1}x + {a0}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
