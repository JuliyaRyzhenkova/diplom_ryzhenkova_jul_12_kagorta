## **Автоматизация теста к API Ez-scooter**

Задание:

Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.

## Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.

Содержаться файлы: 
- data.py
- configuration.py
- sender_stand_request.py
- get_order_track.py
- .gitignor.py

- Diplomnaya_rabota – get_order_track.py 2024-01-31 13-26-41.png - скриншот теста
- SQL Рыженкова Юлия 12 кагорта.txt - SQL запросы


- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
