from module.plano_de_avaliacoes.user_case.csvHandler import CsvHandler
from module.plano_de_avaliacoes.user_case.executar_handler import ExecutarHandler


class PlanoAvaliativoLoad(CsvHandler, ExecutarHandler):
    def __init__(self):
        CsvHandler.__init__(self)
        ExecutarHandler.__init__(self)
