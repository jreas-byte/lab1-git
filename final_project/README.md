# Final Project

## Варіант 4

Додаток аналізує лог-файли на наявність слова `ERROR`.

Користувач вводить рядок логів. Якщо рядок порожній, програма викликає помилку.
Якщо рядок містить `ERROR`, програма повідомляє про знайдену помилку.
Якщо `ERROR` немає, програма повідомляє, що помилок не знайдено.

## Встановлення залежностей

make install

або

pip install -r requirements.txt

## Запуск програми

make run

або

python app.py

## Запуск тестів

make test

## Перевірка форматування

make lint

## Форматування коду

make format

## Перевірка вразливостей

make audit

## Sentry

Для запуску із Sentry у Git Bash:

export SENTRY_DSN="ВАШ_DSN"
python app.py

Для перевірки помилки введіть порожній рядок або некоректні дані.

## Git Hook pre-commit

Створіть файл:

.git/hooks/pre-commit

Вміст файлу:

#!/bin/sh
echo "Перевірка форматування..."
flake8 final_project/app.py final_project/test_app.py
if [ $? -ne 0 ]; then
    echo "Помилка форматування. Коміт скасовано."
    exit 1
fi
echo "Перевірка пройшла успішно."
exit 0

Потім виконайте:

chmod +x .git/hooks/pre-commit
