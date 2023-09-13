import time

from parser.service import ParserSerivce
from database.service import DataBaseSerivce


def processing(inn: int) -> None:
    if company := ParserSerivce.get_company(inn):
        DataBaseSerivce.append_company(company)
    else:
        print(inn, 'missed')


def main():
    inns: tuple[str] = DataBaseSerivce.get_inns()

    for inn in inns:
        while True:
            try:
                processing(inn)
                print(inn, 'COMPLATE')
                break
            except Exception as ex:
                print(inn, ex)
                time.sleep(30)
        
if __name__ == '__main__':
    main()