from dataclasses import dataclass


@dataclass
class Company:
        inn: int | str
        ogrn: int | str
        status: str
        director_name: str
        full_name: str
        okved: str = None
        phones: list[str] = None
        emails: list[str] = None
        social_medias: list[str] = None
        www: list[str] = None

        def to_row(
                self,
                name_colum: int,
                inn_colum: int,
                status_colum: int,
                dir_colum: int,
                okved_colum: int,
                phones_colum: int,
                emails_colum: int,
                www_colum: int,
                social_colum: int
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
                        social_colum: '\n'.join(self.social_medias)
                }

                row: tuple = tuple(colum_places.get(index)
                             for index
                             in range(1, max(colum_places.keys()) + 1))
                
                return row
                        