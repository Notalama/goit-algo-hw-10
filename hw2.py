import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення визначеного інтеграла
def monte_carlo_integration(f, a, b, num_points=10000):
    # Генерація випадкових точок у межах інтервалу [a, b]
    x_random = np.random.uniform(a, b, num_points)
    y_random = np.random.uniform(0, max(f(x_random)), num_points)
    
    # Підрахунок точок, що потрапляють під криву
    points_under_curve = y_random < f(x_random)
    area = (b - a) * max(f(x_random)) * np.mean(points_under_curve)
    
    return area

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)
print("Метод Монте-Карло: ", monte_carlo_result)

# Аналітичне обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Аналітичне значення (quad):", result)
print("Абсолютна похибка (quad):", error)

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Висновки
print(f"\nРезультат методом Монте-Карло: {monte_carlo_result}")
print(f"Результат функцією quad: {result}")
print(f"Різниця між методами: {abs(monte_carlo_result - result)}")
