import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції для інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
N = 10000  # Кількість точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)

area_estimate = (b - a) * np.mean(y_random)
print(f"Оцінка інтегралу методом Монте-Карло: {area_estimate}")

# Аналітичне обчислення інтегралу за допомогою функції quad
result, error = spi.quad(f, a, b)
print(f"Аналітичне значення інтегралу: {result}, з помилкою: {error}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Висновки
if abs(area_estimate - result) < error:
    print("Результати методу Монте-Карло і функції quad майже збігаються.")
else:
    print("Існує суттєва різниця між методом Монте-Карло та функцією quad.")
