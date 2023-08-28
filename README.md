# company_info_parser
![image](https://static.zachestnyibiznes.ru/images/logo_new.png)

Парсер сайта zachestnyibiznes.ru. По ИНН получает: Статус, Руководителя, ОКВЭД, Номера, Почты, Сайты, Соц. сети. Актуально также для ИП.

Структура `.env` файла:
``` bash
# GOOGLE API
SERVICE_ACCOUNT = { "type": "service_account", "project_id": "sheetspython-..." }

# Zanchesny headers
COOKIES = {"_ym_uid": "13259636..0"}
HEADERS = {"authority": "zachestnyib..Request"}


# ID таблицы
SHEET_KEY = 1p4DQeYbP2Iodbt24fs6DVDA1sg1UBjdTfltl-I

# Имя листа для записи
LIST_WRITER_NAME = main
# Колонки для данных
COLUMN_NAME = 2
COLUMN_INN_WRITE = 3
COLUMN_STATUS = 15
COLUMN_DIRECTOR = 16
COLUMN_OKVED = 17
COLUMN_PHONES = 18
COLUMN_EMAILS = 19
COLUMN_WWW = 20
COLUMN_SOCIALS = 21

# Имя листа для считывания 
LIST_READ_NAME = ИНН
# Колонки для данных
COLUMN_INN_READ = 1
```

> *Важно!* Из-за особенности Google API, скрытые столбцы в листах пропускаются (игнорируются).

# Быстрый старт
- Заполинть `.env` файл. Структура выше.
- Установить зависимости: 
    ```bash
    pip install -r requirements.txt
    ``` 
- Запуск:
    ```bash
    python main.py
    ```

## Заметки
- Скрипт не работает в режиме ожидания или хэндлера. Програма отрабатывает единоразово, считывая необходимые данные и записывая результирующие в соответствующие листы таблицы. 
- Зависимость ``Python3.8`` или выше.