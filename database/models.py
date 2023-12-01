from gspread import Worksheet

from database.config import LIST_WRITER, LIST_READ, COLUMN_NAME, COLUMN_INN_WRITE, COLUMN_STATUS, COLUMN_DIRECTOR, COLUMN_OKVED, COLUMN_PHONES, COLUMN_EMAILS, COLUMN_WWW, COLUMN_SOCIALS, COLUMN_INN_READ, COLUMN_DIRECTOR_INN, \
                            COLUMN_FOUNDER, COLUMN_FOUNDER_INN, COLUMN_FOUNDERS, COLUMN_FOUNDERS_INN, COLUMN_INCOME, COLUMN_PROFIT, COLUMN_OUTCOME, COLUMN_LAWS_COUNT, COLUMN_LAWS_CONSIDER, COLUMN_LAWS_COMPLATED, COLUMN_EMPLOYEERS, \
                            COLUMN_SIMCOMP, COLUMN_FSSP, COLUMN_PENALTIES, COLUMN_TAXES
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
            dir_inn_colum=COLUMN_DIRECTOR_INN,
            emails_colum=COLUMN_EMAILS,
            okved_colum=COLUMN_OKVED,
            phones_colum=COLUMN_PHONES,
            social_colum=COLUMN_SOCIALS,
            status_colum=COLUMN_STATUS,
            www_colum=COLUMN_WWW,
            founder_colum=COLUMN_FOUNDER,
            founder_inn_colum=COLUMN_FOUNDER_INN,
            founders_colum=COLUMN_FOUNDERS,
            founders_inn_colum=COLUMN_FOUNDERS_INN,
            income_colum=COLUMN_INCOME,
            profit_colum=COLUMN_PROFIT,
            outcome_colum=COLUMN_OUTCOME,
            lawsuit_count_colum=COLUMN_LAWS_COUNT,
            lawsuit_completed_colum=COLUMN_LAWS_COMPLATED,
            lawsuit_consider_colum=COLUMN_LAWS_CONSIDER,
            employeers_colum=COLUMN_EMPLOYEERS,
            simcomp_colum=COLUMN_SIMCOMP,
            fssp_colum=COLUMN_FSSP,
            penal_colum=COLUMN_PENALTIES,
            taxes_colum=COLUMN_TAXES
            )
        cls._list.append_row(row) # value_input_option='USER_ENTERED'


class Reader:
    _list: Worksheet = LIST_READ
    _start_row: int = 2

    @classmethod
    def read(cls) -> tuple[str]:
        inn_list: tuple = tuple(cls._list.col_values(COLUMN_INN_READ))
        return inn_list[1:]
    