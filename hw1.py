from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо модель для максимізації
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні (кількість продукції, яку потрібно виробити)
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Об'єктивна функція: максимізувати загальну кількість вироблених продуктів
model += lemonade + fruit_juice, "Total Products"

# Обмеження по ресурсам
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water Constraint"
model += (1 * lemonade <= 50), "Sugar Constraint"
model += (1 * lemonade <= 30), "Lemon Juice Constraint"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Кількість виробленого Лимонаду: {lemonade.value()}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.value()}")
print(f"Загальна кількість продуктів: {model.objective.value()}")
