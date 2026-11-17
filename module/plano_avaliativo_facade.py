import logging

import keyboard

from module import PlanoAvaliativoLoad
from module.plano_de_avaliacoes.plano_de_avaliacoes_dto import (
    PlanoDeAvaliacoesDto,
    QuadroCurricularDto,
)

logger = logging.getLogger(__name__)

plano_ctrl = PlanoAvaliativoLoad()


def load_csv(plano_path, quadro_path):
    logger.info("Carregando Dados")

    planos = plano_ctrl.export_plano_csv(plano_path)
    logger.info(f"{len(planos)} Planos Avaliativos carregados")

    quadro = plano_ctrl.export_quadro_csv(quadro_path)
    logger.info(f"{len(quadro)} Quadros Curriculares mapeados\n\n\n")

    return (planos, quadro)


def run(plano: list[PlanoDeAvaliacoesDto], quadro: list[QuadroCurricularDto]):

    print("F8 para iniciar Meu nobre")
    keyboard.wait("f8")

    for idx, elem in enumerate(plano):

        logger.info("========================================================")
        logger.info(f"{idx+1} / {len(plano)}")
        logger.info(f"Turma -> {elem.turma}")
        logger.info(f"Disciplina -> {elem.disciplina}")
        logger.info("========================================================")

        plano_ctrl.abrir_quadro_curricular(
            turma=elem.turma, x=229, y=157, cor=(0, 0, 0)
        )

        plano_ctrl.selecionar_disciplina(
            turma=elem.turma,
            disciplina=elem.disciplina,
            quadro=quadro,
            x=116,
            y=236,
            cor=(240, 240, 240),
        )

        logger.info(f"Corrigindo plano avaliativo {elem.tipo_avaliativo}")
        plano_ctrl.alterar_plano_de_avaliacao(
            nome_avaliativo=elem.nome,
            plano_avaliativo=elem.tipo_avaliativo,
            x=229,
            y=204,
            cor=(169, 181, 208),
            pl_ava_x=841,
            pl_ava_y=199,
            next_x=444,
            next_y=153,
            next_cor=(0, 0, 0),
            input_plano_x=856,
            input_plano_y=274,
            input_plano_cor=(255, 255, 255),
            save_x=367,
            save_y=156,
            save_cor=(240, 240, 240),
            close_x=1022,
            close_y=614,
        )

        logger.info(
            f"Plano de ensino Alterado e Salvo meu nobre {elem.tipo_avaliativo} \n\n"
        )

        plano_ctrl.close_quadro_curricular(
            close_x=25,
            close_y=50,
            close_cor=(243, 242, 241),
            select_turma_x=1114,
            select_turma_y=367,
        )
