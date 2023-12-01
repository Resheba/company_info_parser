from dataclasses import dataclass


@dataclass        
class Founder:
        name: str
        inn: str = None


@dataclass
class Finance:
        income: str = None
        outcome: str = None
        profit: str = None


@dataclass
class LawSuit:
        count: int | str = None
        consider: str = None
        completed: str = None


@dataclass
class Credits:
        FSSP: str = None
        taxes: str = None
        penalties: str = None


@dataclass
class SimCompany:
        name: str
        link: str


@dataclass
class Company:
        inn: int | str
        ogrn: int | str
        status: str
        director_name: str
        director_inn: str
        full_name: str
        okved: str = None
        phones: list[str] = None
        emails: list[str] = None
        social_medias: list[str] = None
        www: list[str] = None
        founders: list[Founder] = None
        finance: Finance = None
        lawsuit: LawSuit = None
        employeers: str = None
        simcompanies: list[SimCompany] = None
        credits: Credits = None

        def to_row(
                self,
                name_colum: int,
                inn_colum: int,
                status_colum: int,
                dir_inn_colum: int,
                dir_colum: int,
                okved_colum: int,
                phones_colum: int,
                emails_colum: int,
                www_colum: int,
                social_colum: int,
                founder_colum: int,
                founder_inn_colum: int,
                founders_colum: int,
                founders_inn_colum: int,
                income_colum: int,
                profit_colum: int,
                outcome_colum: int,
                lawsuit_count_colum: int,
                lawsuit_consider_colum: int,
                lawsuit_completed_colum: int,
                employeers_colum: int,
                simcomp_colum: int,
                fssp_colum: int,
                taxes_colum: int,
                penal_colum: int
        ) -> tuple[str|None]:
                colum_places: dict = {
                        name_colum: self.full_name,
                        inn_colum: self.inn,
                        status_colum: self.status,
                        dir_colum: self.director_name,
                        okved_colum: self.okved,
                        phones_colum: '\n'.join(self.phones),
                        emails_colum: '\n'.join(self.emails),
                        www_colum: '\n'.join(self.www),
                        social_colum: '\n'.join(self.social_medias),
                        dir_inn_colum: self.director_inn,
                        founder_colum: self.founders[0].name if self.founders else None,
                        founder_inn_colum: self.founders[0].inn if self.founders else None,
                        founders_colum: '\n'.join(founder.name or '-' for founder in self.founders[1:]),
                        founders_inn_colum: '\n'.join(founder.inn or '-' for founder in self.founders[1:]),
                        income_colum: self.finance.income,
                        profit_colum: self.finance.profit,
                        outcome_colum: self.finance.outcome,
                        lawsuit_count_colum: self.lawsuit.count,
                        lawsuit_consider_colum: self.lawsuit.consider,
                        lawsuit_completed_colum: self.lawsuit.completed,
                        employeers_colum: self.employeers,
                        # simcomp_colum: '=' + '\n '.join(f'ГИПЕРССЫЛКА("{comp.link}"; "{comp.name}")' for comp in self.simcompanies or ()),
                        simcomp_colum: '\n'.join(comp.name for comp in self.simcompanies or ()),
                        fssp_colum: self.credits.FSSP,
                        taxes_colum: self.credits.taxes,
                        penal_colum: self.credits.penalties,
                }
                row: tuple = tuple(colum_places.get(index)
                             for index
                             in range(1, max(colum_places.keys()) + 1))
                return row
                        