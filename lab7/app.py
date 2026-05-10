def calculate_payroll(employees):
    """
    Розраховує зарплату працівників.

    >>> calculate_payroll([{"name": "Іван", "hours": 40, "rate": 100}])
    [{'name': 'Іван', 'salary': 4000}]
    >>> calculate_payroll([])
    []
    """
    payroll = []

    for employee in employees:
        name = employee["name"]
        hours = employee["hours"]
        rate = employee["rate"]

        if hours < 0 or rate < 0:
            raise ValueError("Години та ставка не можуть бути від'ємними")

        salary = hours * rate
        payroll.append({"name": name, "salary": salary})

    return payroll


def main():
    employees = [
        {"name": "Іван", "hours": 40, "rate": 120},
        {"name": "Марія", "hours": 35, "rate": 150},
        {"name": "Олег", "hours": 20, "rate": 100},
    ]

    payroll = calculate_payroll(employees)

    print("Нарахована зарплата працівників:")
    for employee in payroll:
        print(f"{employee['name']}: {employee['salary']} грн")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
