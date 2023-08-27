import requests
from requests_html import HTMLSession, Element

from database.config import HEADERS, COOKIES
from parser.typping.response import SearchIPResponse, SearchULResponse, InfoResponse


class RequestZach:
    _company_url: str = 'https://zachestnyibiznes.ru/company/ul/'
    _search_url: str = 'https://zachestnyibiznes.ru/site/get-autocomplete-api'

    _js_contact_func: str = '() => { let temp = $(".hide-contact-one")[0]; if (temp) { return  $._data(temp, "events").click[0].handler.toString() } else { return null } }' #open('contact.js').read()
    _contact_js_sleep: float = .5
    _session: HTMLSession = HTMLSession()

    @classmethod
    def searchIP(cls, 
                 inn: int|str
                 ) -> SearchIPResponse:
        with requests.post(cls._search_url,
                            headers=HEADERS,
                            cookies=COOKIES,
                            params={
                                'index': 'ip',
                                'query': str(inn)
        }) as response:
            data: dict = response.json()
            return SearchIPResponse(data)
    
    @classmethod
    def searchUL(cls, 
                 inn: int|str
                 ) -> SearchULResponse:
        with requests.post(cls._search_url,
                            headers=HEADERS,
                            cookies=COOKIES,
                            params={
                                'index': 'ul',
                                'query': str(inn)
        }) as response:
            data: dict = response.json()
            return SearchULResponse(data)
    
    @classmethod
    def get_info(cls, 
                    id: int|str
                    ) -> InfoResponse:
        '''
        ID and OGRN usually match.
        '''
        url: str = cls._company_url + str(id)

        with cls._session.get(url) as response:
            response.html.render(sleep=cls._contact_js_sleep)

            okved: str = cls._get_okved(response)

            _function: str = response.html.render(script=cls._js_contact_func, reload=False)

            if _function:
                contacts: dict = eval(_function[23:-186])
            else:
                contacts: dict = dict()

            return InfoResponse(contacts, okved)
    
    @staticmethod
    def _get_okved(
        response: requests.Response
                  ) -> str | None:
        html_block: Element = response.html.find('div.tpanel-body', first=True)

        html_rows: list[Element] = html_block.find('div.row')
        for row in html_rows:
            if 'Основной вид деятельности' in row.text:
                # okved: str = row.text.replace('Основной вид деятельности', '').strip()
                # print(okved, len(okved))
                p_html: Element = row.find('p.sub-title-content', first=True)
                
                if p_a_html:= p_html.find('a', first=True):
                    okved: str = p_html.text.replace(p_a_html.text, '')
                else:
                    okved: str = p_html.text
                
                okved: str = okved.strip()

                return okved or None
        