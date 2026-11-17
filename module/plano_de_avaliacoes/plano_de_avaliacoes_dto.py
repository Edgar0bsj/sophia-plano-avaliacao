from dataclasses import dataclass


@dataclass
class PlanoDeAvaliacoesDto:
    nome: str
    situacao: str
    turma: str
    disciplina: str
    tipo_avaliativo: str


@dataclass
class QuadroCurricularDto:
    turma: str
    disciplina: list[str]
