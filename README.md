# Проект: парсинга scrapy_parser_pep

> Парсер документов PEP для сбора статистики по статусам PEP с использованием асинхронного фреймворка Scrapy.


##  Функциональность

- Парсинг ссылок на отдельные страницы PEP с официального сайта Python
- Парсинг каждой отдельной страницы PEP
- Подсчет количества PEP по статусам
- Генерация отчетов в формате CSV

## Установка и запуск

   ```
    git clone https://github.com/Zi0001/scrapy_parser_pep.git
    cd scrapy_parser_pep
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    scrapy crawl pep
  ```

## В проекте были использованы технологии:
1. Python 3.10
2. Scrapy
3. datetime
4. csv
5. pathlib

## Над проектом работал
> Учадзе З.Т. https://github.com/Zi0001/scrapy_parser_pep.git