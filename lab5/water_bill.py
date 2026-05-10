def calculate_usage(previous_reading, current_reading):
    """
    Обчислює обсяг використаної води.

    >>> calculate_usage(100, 120)
    20
    >>> calculate_usage(50, 50)
    0
    """
    if previous_reading < 0 or current_reading < 0:
        raise ValueError("Показники лічильника не можуть бути від'ємними")
    if current_reading < previous_reading:
        raise ValueError("Поточний показник не може бути меншим за попередній")
    return current_reading - previous_reading


def calculate_bill(usage, tariff):
    """
    Обчислює суму до оплати.

    >>> calculate_bill(10, 30)
    300
    >>> calculate_bill(0, 30)
    0
    """
    if usage < 0:
        raise ValueError("Використання води не може бути від'ємним")
    if tariff < 0:
        raise ValueError("Тариф не може бути від'ємним")
    return usage * tariff


def create_summary(previous_reading, current_reading, tariff):
    """
    Формує підсумок розрахунку.

    >>> create_summary(100, 120, 30)
    {'usage': 20, 'tariff': 30, 'total': 600}
    """
    usage = calculate_usage(previous_reading, current_reading)
    total = calculate_bill(usage, tariff)

    return {
        "usage": usage,
        "tariff": tariff,
        "total": total,
    }


def main():
    previous_reading = float(input("Введіть попередній показник лічильника: "))
    current_reading = float(input("Введіть поточний показник лічильника: "))
    tariff = float(input("Введіть тариф за 1 м3 води: "))

    summary = create_summary(previous_reading, current_reading, tariff)

    print("Використано води:", summary["usage"], "м3")
    print("Тариф:", summary["tariff"], "грн")
    print("Сума до оплати:", summary["total"], "грн")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
