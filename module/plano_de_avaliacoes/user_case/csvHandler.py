from pathlib import Path

import pandas as pd

from module.plano_de_avaliacoes.plano_de_avaliacoes_dto import (
    PlanoDeAvaliacoesDto,
    QuadroCurricularDto,
)


class CsvHandler:
    def __init__(self):
        pass

    def export_plano_csv(self, file_path: Path):
        data = (
            pd.read_csv(file_path, sep=";", encoding="utf-8")
            .fillna("")
            .to_dict("records")
        )

        _buffer = []
        for e in data:
            descricao = e["Descrição"]
            situacao = e["Situação"]
            turma = e["Turma"]
            disciplina = e["Disciplina"]
            tipo_avaliacao = e["Tipo de avaliação"]

            _buffer.append(
                PlanoDeAvaliacoesDto(
                    nome=descricao,
                    situacao=situacao,
                    turma=turma,
                    disciplina=disciplina,
                    tipo_avaliativo=tipo_avaliacao,
                )
            )

        return _buffer

    def export_quadro_csv(self, file_path: Path):
        data = (
            pd.read_csv(file_path, sep=";", encoding="utf-8")
            .fillna("")
            .to_dict("records")
        )

        _buffer: dict[str, QuadroCurricularDto] = {}
        for e in data:
            turma = str(e["TURMA"])
            disciplina = str(e["DISCIPLINA"])

            if not turma in _buffer:
                _buffer[turma] = QuadroCurricularDto(turma, disciplina=[])

            _buffer[turma].disciplina.append(disciplina)

        return list(_buffer.values())
