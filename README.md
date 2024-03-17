# scrapy_parser_pep

# Руководство пользователя

Этот проект предназначен для сбора информации о документах Python Enhancement Proposal (PEP) с
веб-сайта [PEPs Python](https://peps.python.org/).

## Установка

1. Убедитесь, что у вас установлен Python версии 3.x.
2. Клонируйте репозиторий проекта:

    ```bash
    git clone https://github.com/username/project.git
    ```
3. Перейдите в директорию проекта:

    ```bash
    cd pep_parse
    ```
4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

### Запуск паука

Чтобы запустить паука для сбора информации о PEP-документах, выполните следующую команду:

```bash
scrapy crawl pep
```

# Результаты

После завершения работы паука результаты будут сохранены в CSV-файлы.

Файлы будут доступны в директории `results` проекта.
Один из файлов будет содержать список всех PEP: номер, название и статус.
Второй будет содержать сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В
последней строке этого файла в колонке «Статус» должно стоять слово Total - общее количество всех документов.
