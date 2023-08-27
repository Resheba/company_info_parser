from parser.typping.request import RequestZach, SearchIPResponse, SearchULResponse, InfoResponse
from parser.typping.company import Company
from parser.typping.response import SearchIPResult, SearchULResult


class ParserSerivce:

    @classmethod
    def get_company(
        cls,
        inn: int|str
    ) -> Company | None:
        inn: str = str(inn)

        if len(inn) == 12:
            return cls._get_ip(inn)
        elif len(inn) == 10:
            return cls._get_ul(inn)

    @classmethod
    def _get_ul(
        cls,
        inn: str|int
    ) -> Company | None:
        ul_credential: SearchULResult = cls.__get_ul_info(inn=inn)
        if ul_credential:
            ul_info: InfoResponse = RequestZach.get_info(id=ul_credential.id)

            return Company(
                inn=ul_credential.inn,
                ogrn=ul_credential.ogrn,
                status=ul_credential.status,
                director_name=ul_credential.director_full_name,
                full_name=ul_credential.full_name,
                okved=ul_info.okved,
                emails=ul_info.emails,
                phones=ul_info.phones,
                social_medias=ul_info.social_medias,
                www=ul_info.www
            )
    @classmethod
    def _get_ip(
        cls,
        inn: str|int
    ) -> Company | None:
        ip_credential: SearchIPResult = cls.__get_ip_info(inn=inn)
        if ip_credential:
            ip_info: InfoResponse = RequestZach.get_info(id=ip_credential.id)

            return Company(
                inn=ip_credential.inn,
                ogrn=ip_credential.ogrn,
                status=ip_credential.status,
                director_name=ip_credential.full_name,
                full_name='ИП ' + ip_credential.full_name,
                okved=ip_info.okved,
                emails=ip_info.emails,
                phones=ip_info.phones,
                social_medias=ip_info.social_medias,
                www=ip_info.www
            )

    @staticmethod
    def __get_ip_info(
        inn: str|int
    ) -> SearchIPResult | None:
        search_response: SearchIPResponse = RequestZach.searchIP(inn=inn)

        for ip_credential in search_response.result:
            if ip_credential.inn == inn:
                return ip_credential
            
    @staticmethod
    def __get_ul_info(
        inn: str|int
    ) -> SearchULResult | None:
        search_response: SearchULResponse = RequestZach.searchUL(inn=inn)

        for ul_credential in search_response.result:
            if ul_credential.inn == inn:
                return ul_credential

