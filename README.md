# company_info_parser
![image](https://static.zachestnyibiznes.ru/images/logo_new.png)

Парсер сайта zachestnyibiznes.ru. По ИНН получает: Статус, Руководителя, ОКВЭД, Номера, Почты, Сайты, Соц. сети и иное. Актуально также для ИП.

Структура `.env` файла:
``` bash
# GOOGLE API
SERVICE_ACCOUNT = {...}

# Zanchesny headers
COOKIES = {...}
HEADERS = {...}

# ID таблицы
SHEET_KEY = 10Cxkt-j4fQ_j...

# Имя листа для записи
LIST_WRITER_NAME = main
# Колонки для данных
COLUMN_NAME = 2
COLUMN_INN_WRITE = 1
COLUMN_STATUS = 3
COLUMN_DIRECTOR_INN = 5
COLUMN_DIRECTOR = 4
COLUMN_OKVED = 6
COLUMN_PHONES = 14
COLUMN_EMAILS = 15
COLUMN_WWW = 16
COLUMN_SOCIALS = 17
COLUMN_FOUNDER = 7
COLUMN_FOUNDER_INN = 8
COLUMN_FOUNDERS = 9
COLUMN_FOUNDERS_INN = 10
COLUMN_INCOME = 11
COLUMN_PROFIT = 12
COLUMN_OUTCOME = 13
COLUMN_LAWS_COUNT = 18
COLUMN_LAWS_CONSIDER = 19
COLUMN_LAWS_COMPLATED = 20
COLUMN_EMPLOYEERS = 21
COLUMN_SIMCOMP = 25

COLUMN_FSSP = 22
COLUMN_TAXES = 23
COLUMN_PENALTIES = 24

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