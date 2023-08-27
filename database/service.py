from database.models import Writer, Reader
from parser.typping.company import Company


class DataBaseSerivce:

    @staticmethod
    def get_inns() -> tuple[str]:
        return Reader.read()
    
    @staticmethod
    def append_company(
        company: Company
    ) -> None:
        Writer.append(company)