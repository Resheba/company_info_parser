import dotenv, os, json, gspread


dotenv.load_dotenv()


SERVICE_ACCOUNT = json.loads(os.getenv('SERVICE_ACCOUNT'))

SHEET_KEY = os.getenv('SHEET_KEY')
LIST_WRITER_NAME = os.getenv('LIST_WRITER_NAME')
LIST_READ_NAME = os.getenv('LIST_READ_NAME')

COLUMN_NAME = int(os.getenv('COLUMN_NAME'))
COLUMN_INN_WRITE = int(os.getenv('COLUMN_INN_WRITE'))
COLUMN_STATUS = int(os.getenv('COLUMN_STATUS'))
COLUMN_DIRECTOR = int(os.getenv('COLUMN_DIRECTOR'))
COLUMN_OKVED = int(os.getenv('COLUMN_OKVED'))
COLUMN_PHONES = int(os.getenv('COLUMN_PHONES'))
COLUMN_EMAILS = int(os.getenv('COLUMN_EMAILS'))
COLUMN_WWW = int(os.getenv('COLUMN_WWW'))
COLUMN_SOCIALS = int(os.getenv('COLUMN_SOCIALS'))

COLUMN_INN_READ = int(os.getenv('COLUMN_INN_READ'))

HEADERS = json.loads(os.getenv('HEADERS'))
COOKIES = json.loads(os.getenv('COOKIES'))


gc = gspread.service_account_from_dict(SERVICE_ACCOUNT)

SHEET = gc.open_by_key(SHEET_KEY)

LIST_WRITER = SHEET.worksheet(LIST_WRITER_NAME)
LIST_READ = SHEET.worksheet(LIST_READ_NAME)
