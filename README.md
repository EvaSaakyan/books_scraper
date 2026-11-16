# Сбор данных о книгах с сайта Books to Scrape

## Цель проекта

Сбор названий, цен, рейтингов, наличия, описаний и характеристик книг с сайта https://books.toscrape.com.

## Инструкция по запуску

Создать и активировать виртуальное окружение, установить зависимости:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Запустить парсер из корневой папки проекта:

python -c "from scraper import scrape_books; scrape_books(is_save=True)"

Данные сохраняются в artifacts/books_data.txt.

Запустить тесты:

python -m pytest tests/test_scraper.py

## Используемые библиотеки

- requests — получение веб-страниц.
- beautifulsoup4 — обработка HTML.
- schedule — запуск по расписанию.
- pytest — тестирование.
