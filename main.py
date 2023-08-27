from parser.service import ParserSerivce
from database.service import DataBaseSerivce

def main():
    inns: tuple[str] = DataBaseSerivce.get_inns()

    for inn in inns:
        if company := ParserSerivce.get_company(inn):
            DataBaseSerivce.append_company(company)
        else:
            print(inn, 'missed')
    
if __name__ == '__main__':
    main()