# Проект парсинга scrapy_parser_pep
## Описание
Программа-парсер собирает данные о статусах PEP, смотрит новые версии и записывает в файл необходимую информацию на базе фреймворка Scrapy.

## Применяемые технологии

[![Python](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://scrapy.org/)

### Развертывание и запуск парсера

Клонировать репозиторий, перейти в папку в проектом, затем создать, активировать виртуальное окружение и установить зависимости:

```bash
git clone git@github.com:Xizillimax/scrapy_parser_pep.git
cd scrapy_parser_pep
python3 -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
```

## Работа с парсером
Запуск парсера
```
scrapy crawl pep
```

После завершения работы в папке `results` будут сохранены два файла:
1) Список всех PEP: номер, название и статус.
2) Сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла будет слово Всего, а напротив него — общее количество всех документов.

Автор - [Maxim Zelenin](https://github.com/Xizillimax)