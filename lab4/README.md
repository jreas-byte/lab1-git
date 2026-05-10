# Лабораторна робота 4

## Варіант 4
Створити додаток, що буде емулювати роботу кафе.

## Опис
Додаток містить функції:
- add_menu_item — додає позицію до меню;
- create_order — формує замовлення;
- calculate_bill — обчислює загальну вартість замовлення.

## Створення віртуального оточення

python -m venv venv

## Активація

source venv/Scripts/activate

## Встановлення залежностей

pip install -r requirements.txt

## Запуск програми

python cafe.py

## Форматування коду

black cafe.py

## Перевірка лінтером

flake8 cafe.py
