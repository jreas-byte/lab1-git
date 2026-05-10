import os

import sentry_sdk


def init_sentry():
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        traces_sample_rate=1.0,
    )


def analyze_log(log_text):
    """
    Аналізує рядок логів на наявність слова ERROR.

    >>> analyze_log("INFO Application started")
    'Помилок не знайдено'
    >>> analyze_log("ERROR Database connection failed")
    'Знайдено помилку ERROR'
    """
    if not isinstance(log_text, str):
        raise ValueError("Лог має бути рядком")

    if not log_text.strip():
        raise ValueError("Рядок логів не може бути порожнім")

    if "ERROR" in log_text:
        return "Знайдено помилку ERROR"

    return "Помилок не знайдено"


def main():
    init_sentry()

    try:
        user_input = input("Введіть рядок логів: ")
        result = analyze_log(user_input)
        print(result)
    except Exception as error:
        sentry_sdk.capture_exception(error)
        raise


if __name__ == "__main__":
    main()
