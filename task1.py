from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += (2 * lemonade + fruit_juice <= 100, "water_limit")
model += (lemonade <= 50, "sugar_limit")
model += (lemonade <= 30, "lemon_juice_limit")
model += (2 * fruit_juice <= 40, "fruit_puree_limit")

model += lemonade + fruit_juice, "Total_Production"

model.solve()

print(f"Кількість виробленого Лимонаду: {value(lemonade)}")
print(f"Кількість виробленого Фруктового соку: {value(fruit_juice)}")
print(f"Максимальна кількість продуктів: {value(model.objective)}")
