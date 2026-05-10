import os

import sentry_sdk


def init_sentry():
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        traces_sample_rate=1.0,
    )


def check_memory(value):
    """
    Перевіряє значення пам'яті.

    Якщо значення більше 70, повертає повідомлення про високий рівень пам'яті.
    Якщо дані неправильні, викликає помилку.
    """
    try:
        memory_value = float(value)
    except ValueError as exc:
        raise ValueError("Потрібно ввести число") from exc

    if memory_value < 0:
        raise ValueError("Значення пам'яті не може бути від'ємним")

    if memory_value > 70:
        return "Значення більше 70, пам'ять використовується помилка"

    return "Значення в межах норми"


def main():
    init_sentry()

    try:
        print("Введіть значення використання пам'яті:")
        user_input = input()
        result = check_memory(user_input)
        print(result)
    except Exception as error:
        sentry_sdk.capture_exception(error)
        raise


if __name__ == "__main__":
    main()
