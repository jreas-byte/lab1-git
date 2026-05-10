MENU = {
    "Кава": 45,
    "Чай": 35,
    "Круасан": 60,
    "Сендвіч": 95,
    "Тістечко": 70,
}


def add_menu_item(menu, name, price):
    menu[name] = price
    return menu


def create_order(items):
    order = []
    for item in items:
        if item in MENU:
            order.append(item)
    return order


def calculate_bill(order):
    total = 0
    for item in order:
        total += MENU[item]
    return total


def print_order(order):
    print("Замовлення кафе:")
    for item in order:
        print(f"- {item}: {MENU[item]} грн")
    print(f"Загальна вартість: {calculate_bill(order)} грн")


def main():
    add_menu_item(MENU, "Сік", 50)
    order = create_order(["Кава", "Круасан", "Сік", "Тістечко"])
    print_order(order)


if __name__ == "__main__":
    main()
