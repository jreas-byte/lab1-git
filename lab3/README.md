# Лабораторна робота 3

## Тема
Створення C++ проєкту з декількох файлів, Makefile та Docker.

## Варіант 4
Створити додаток, що буде емулювати магазин електроніки.

У файлах Product.h та Product.cpp реалізовано клас товару.
У файлах Store.h та Store.cpp реалізовано логіку магазину.
Файл main.cpp додає товари та розраховує загальну вартість замовлення.

## Компіляція проєкту

make

## Запуск проєкту

./app

## Очищення файлів збірки

make clean

## Запуск через Docker

docker build -t store_app .
docker run store_app

## Запуск через Docker Compose

docker compose up --build
