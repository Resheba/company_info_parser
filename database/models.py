from gspread import Worksheet

from database.config import LIST_WRITER, LIST_READ, COLUMN_NAME, COLUMN_INN_WRITE, COLUMN_STATUS, COLUMN_DIRECTOR, COLUMN_OKVED, COLUMN_PHONES, COLUMN_EMAILS, COLUMN_WWW, COLUMN_SOCIALS, COLUMN_INN_READ
from parser.typping.company import Company


class Writer:
    _list: Worksheet = LIST_WRITER

    @classmethod
    def append(
        cls,
        company: Company
    ) -> None:
        row: tuple = company.to_row(
            name_colum=COLUMN_NAME,
            inn_colum=COLUMN_INN_WRITE,
            dir_colum=COLUMN_DIRECTOR,
            emails_colum=COLUMN_EMAILS,
            okved_colum=COLUMN_OKVED,
            phones_colum=COLUMN_PHONES,
            social_colum=COLUMN_SOCIALS,
            status_colum=COLUMN_STATUS,
            www_colum=COLUMN_WWW
            )
        cls._list.append_row(row)


class Reader:
    _list: Worksheet = LIST_READ
    _start_row: int = 2

    @classmethod
    def read(cls) -> tuple[str]:
        inn_list: tuple = tuple(cls._list.col_values(COLUMN_INN_READ))
        return inn_list[1:]