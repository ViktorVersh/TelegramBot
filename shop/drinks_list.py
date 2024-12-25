"""
Список доступных напитков хранится в виде словаря название: стоимость,
можно легко менять ассортимент редактируя словарь
"""
drinks = {
    'coke': 100,
    'sprite': 90,
    'fanta': 80,
    'cofe_americano': 120,
    'cofe_latte': 110,
    'cofe_cappuccino': 130,
    'tea_black': 100,
    'tea_green': 90,
    'tea_lemon': 110,
}

# Форматируем список напитков для отображения
formatted_drinks = "\n".join([f"{name}: {price} ₽" for name, price in drinks.items()])

if __name__ == '__main__':
    print(formatted_drinks)