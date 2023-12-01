import requests
from seleniumbase import DriverContext
from requests_html import Element, HTML
from selenium.webdriver.chrome.webdriver import WebDriver

from database.config import HEADERS, COOKIES
from .response import SearchIPResponse, SearchULResponse, InfoResponse
from .company import Credits, Finance, Founder, LawSuit, SimCompany


class RequestZach:
    _zach_domain: str = 'https://zachestnyibiznes.ru'
    _company_url: str = 'https://zachestnyibiznes.ru/company/ul/'
    _search_url: str = 'https://zachestnyibiznes.ru/site/get-autocomplete-api'

    _js_contact_func: str = 'let temp = $(".hide-contact-one")[0]; if (temp) { return  $._data(temp, "events").click[0].handler.toString() } else { return null }' #open('contact.js').read()
    _contact_js_sleep: float = .5

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

        with DriverContext(headless=True) as driver:
            driver: WebDriver
            driver.get(url)

            driver.sleep(cls._contact_js_sleep)

            html: HTML = HTML(html=driver.page_source)

            okved: str = cls._get_okved(html=html)
            founders: list[Founder] = cls._get_founders(html=html)
            finance: Finance = cls._get_finance(html=html)
            lawsuit: LawSuit = cls._get_lawsuit(html=html)
            employeers: str = cls._get_employees(html=html)
            simcompanies: list[SimCompany] = cls._get_similar_companies_links(html=html)
            credits: Credits = cls._get_credits(html=html)

            _function: str = driver.execute_script(script=cls._js_contact_func)

            if _function:
                contacts: dict = eval(_function[23:-186])
            else:
                contacts: dict = dict()

            return InfoResponse(data=contacts, okved=okved, founders=founders, finance=finance, lawsuit=lawsuit, employeers=employeers, simcompanies=simcompanies, credits=credits)
    
    @staticmethod
    def _get_okved(
        html: HTML
                  ) -> str | None:
        html_rows: list[Element] = html.find("div:contains('Основной вид деятельности')")

        if html_rows:
            block: Element = html_rows[-1]
            p_html: Element = block.find('p.sub-title-content', first=True)

            if p_a_html:= p_html.find('a', first=True):
                okved: str = p_html.text.replace(p_a_html.text, '')
            else:
                okved: str = p_html.text
            okved: str = okved.strip()

            return okved or None
    
    @staticmethod
    def _get_founders(
        html: HTML
                    ) -> list[Founder]:
        founders_html: list[Element] = html.find("div.row.m-t-5:contains('Доля')")
        founders: list[Founder] = list()
        for founder_html in founders_html:
            name_tag: Element = founder_html.find('a', first=True)
            name: str = name_tag.text.strip() if name_tag else None
            inn_tag: Element = founder_html.find('span.copy-string', first=True)
            inn: str = inn_tag.text.strip() if inn_tag and inn_tag.text.isdecimal() else None
            founders.append(Founder(name=name, inn=inn))
        return founders
    
    @staticmethod
    def _get_finance(
        html: HTML
                    ) -> Finance:
        finance_html: Element = html.find("div.col-md-8:contains('Расходы')", first=True)
        income = profit = outcome = None
        if finance_html:
            income, profit, outcome, *_ = finance_html.text.split('\n')[1::2]
        
        return Finance(income=income, outcome=outcome, profit=profit)

    @staticmethod
    def _get_lawsuit(
        html: HTML
                    ) -> LawSuit:
        lawsuits_html: Element = html.find('div.row.m-b-5:contains("Ответчик")', first=True) # :not(['nav-tab-active-pane'])
        suit_count = consider = completed = None
        if lawsuits_html:
            consider_html: Element = lawsuits_html.find('p:contains("Рассматривается")', first=True)
            completed_html: Element = lawsuits_html.find('p:contains("Завершено")', first=True)
            if consider_html:
                cons_words: list[str] = consider_html.text.split()
                if len(cons_words) > 3:
                    suit_count: int = (suit_count or 0) + int(cons_words[1] if cons_words[1].isdigit() else 0)
                    consider: str = ' '.join(cons_words[-3:])
            if completed_html:
                comp_words: list[str] = completed_html.text.split()
                if len(comp_words) > 3:
                    suit_count: int = (suit_count or 0) + int(comp_words[1] if comp_words[1].isdigit() else 0)
                    completed: str = ' '.join(comp_words[-3:])
        return LawSuit(count=suit_count or None, consider=consider, completed=completed)
    
    @staticmethod
    def _get_employees(
        html: HTML
                    ) -> str:
        employ_html: Element = html.find('div.row.m-b-10:contains("Среднесписочная")', first=True)
        if employ_html:
            emp_count_html: Element = employ_html.find('span.m-r-7', first=True)
            if emp_count_html:
                employers_count, *_ = emp_count_html.text.split('+')
                return employers_count
            
    @classmethod
    def _get_similar_companies_links(
        cls,
        html: HTML
                            ) -> list[SimCompany]:
        companies_html: Element = html.find('ul.similar-companies', first=True)
        companies: list[SimCompany] = list()
        if companies_html:
            for company_html in companies_html.find('li') or ():
                name_html: Element = company_html.find('span.company-name', first=True)
                link_html: Element = company_html.find('a:not([class*="no-underline"])', first=True)
                if name_html or link_html:
                    name: str = name_html.text if name_html else None
                    link: str = cls._zach_domain + link_html.attrs.get('href') if link_html else None
                    simcompany: SimCompany = SimCompany(name=name, link=link)
                    name = link = None
                    companies.append(simcompany)
        return companies or None             

    @staticmethod
    def _get_credits(
        html: HTML
                    ) -> Credits:
        credits_html: Element = html.find('div.tpanel:contains("Долги")', first=True)
        credits: Credits = Credits()
        if credits_html:
            tabs: list[Element] = credits_html.find('div.nav-tab-pane') or ()
            if len(tabs) >= 3:
                FSSP_div: Element = tabs[0].find('div.row.m-t-30', first=True)
                if FSSP_div:
                    all_sum_tag: Element = FSSP_div.find('a', first=True)
                    credits.FSSP: str = all_sum_tag.text.strip() if all_sum_tag else None
                
                taxes: Element = tabs[1].find('b', first=True)
                if taxes:
                    credits.taxes: str = taxes.text.strip()
                
                row_html: Element = tabs[2].find('div.row', first=True)
                if row_html:
                    for p_tag in row_html.find('b') or ():
                        credits.penalties = (credits.penalties or '') + p_tag.text.strip() + '\n'
        return credits
                