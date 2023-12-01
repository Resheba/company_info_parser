from bs4 import BeautifulSoup
from dataclasses import dataclass

from .company import Credits, Finance, Founder, LawSuit, SimCompany


class InfoResponse:
    def __init__(self, 
                 data: dict,
                 okved: str|int,
                 founders: list[Founder],
                 finance: Finance,
                 lawsuit: LawSuit,
                 employeers: str,
                 simcompanies: list[SimCompany],
                 credits: Credits,
                 ) -> None:
        self.okved: str|int = okved
        self.founders: list[Founder] = founders
        self.finance: Finance = finance
        self.lawsuit: LawSuit = lawsuit
        self.employeers: str = employeers
        self.simcompanies: list[SimCompany] = simcompanies
        self.credits: Credits = credits

        self.phones = self.emails = self.social_medias = self.www = list()   
    
        if _phones_html := data.get('phone'):
            self.phones = [BeautifulSoup(html.replace('\\', ''), 'html.parser').get_text() 
                           for html 
                           in _phones_html.values()]
        
        if _emails_html := data.get('email'):
            self.emails = [BeautifulSoup(html.replace('\\', ''), 'html.parser').get_text() 
                           for html 
                           in _emails_html.values()]
        
        if _socials_html := data.get('socialMedia'):
            self.social_medias = [BeautifulSoup(html.replace('\\', ''), 'html.parser').get_text() 
                           for html 
                           in _socials_html.values()]
            
        if _www_html := data.get('www'):
            self.www = [BeautifulSoup(html.replace('\\', ''), 'html.parser').get_text() 
                           for html 
                           in _www_html.values()]
    
    def __str__(self) -> str:
        return str(dict(self.__dict__))
        

@dataclass
class SearchIPResult:
    id: str = None
    inn: str = None
    ogrn: str = None
    status: str = None
    full_name: str = None
        

class SearchIPResponse:
    def __init__(self,
                 data: dict
                 ) -> None:
        _docs: list[dict] = data.get('docs')
        self.result: list[SearchIPResult] = list()

        if _docs:
            for result in _docs:
                id: str = result.get('_id')
                _FNS: dict = result.get('_source').get('ФНС')
                ogrn: str = _FNS.get('ОГРНИП')
                inn: str = _FNS.get('ИННФЛ')
                full_name: str = f"{_FNS.get('Имя', '')} {_FNS.get('Фамилия', '')} {_FNS.get('Отчество', '')}"
                status: str = 'Действующий' if _FNS.get('Активность') == 1 else 'Деятельность прекращена'

                self.result.append(SearchIPResult(id, inn, ogrn, status, full_name))
        else:
            self.result = None


@dataclass
class SearchULResult(SearchIPResult):
    director_full_name: str = None
    director_inn: str = None


class SearchULResponse:
    def __init__(self,
                 data: dict
                 ) -> None:
        _docs: list[dict] = data.get('docs')
        self.result: list[SearchULResult] = list()

        if _docs:
            for result in _docs:
                id: str = result.get('_id')
                _FNS: dict = result.get('_source').get('ФНС')
                ogrn: str = _FNS.get('ОГРН')
                inn: str = _FNS.get('ИНН')
                full_name: str = _FNS.get('НаимЮЛПолн')
                status: str = 'Действующий' if _FNS.get('Активность') == 1 else 'Деятельность прекращена'
                director_full_name = None
                director_inn = None
                
                if directors := _FNS.get('Руководители'):
                    director_full_name: str = directors[0].get('ФИО')
                    director_inn: str = directors[0].get('ИННФЛ')


                self.result.append(SearchULResult(id, inn, ogrn, status, full_name, director_full_name, director_inn))
        else:
            self.result = None
