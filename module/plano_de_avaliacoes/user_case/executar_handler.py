import logging

import keyboard
import pyautogui as gui
import pyperclip

from module.plano_de_avaliacoes.plano_de_avaliacoes_dto import (
    QuadroCurricularDto,
)

logger = logging.getLogger(__name__)


class ExecutarHandler:
    def __init__(self):
        self.sleep_time = 3

    def get_plano_avaliativo(self, tipo_avaliativo: str):
        mapper_plano_avaliativo: dict[str, str] = {
            "AV- Atividade Avaliativa": "AV-Atividade Avaliativa",
            "Estágio": "Tema Integrador",
            "Vivência Pedagógica": "Tema Integrador",
            "Trabalho de Conclusão de Curso": "Tema Integrador",
            "Inativo": "Inativo",
        }
        try:
            valor_original = mapper_plano_avaliativo.get(
                tipo_avaliativo.strip(), tipo_avaliativo.strip()
            )

            logger.info(f"Plano de ensino que estava {tipo_avaliativo}")
            logger.info(f"Alterado para {valor_original}")
            return valor_original
        except Exception:  # noqa: BLE001
            input(f"ERROR! Dados inconsistente meu nobre -> {tipo_avaliativo}")
            raise ValueError(f"Tipo inválido ! {tipo_avaliativo}")

    def abrir_quadro_curricular(self, turma: str, x: int, y: int, cor: tuple):

        gui.sleep(self.sleep_time)
        gui.press("esc")
        gui.sleep(self.sleep_time)
        keyboard.write(turma, delay=0.04)
        gui.sleep(self.sleep_time)
        gui.press("enter")
        gui.sleep(5)
        gui.hotkey("win", "up")
        gui.sleep(self.sleep_time)
        gui.sleep(self.sleep_time)

        if not gui.pixelMatchesColor(x, y, cor, tolerance=10):
            input("TEMPO EXEDIDO")

        gui.click(x, y)
        gui.sleep(self.sleep_time)

    def selecionar_disciplina(
        self,
        turma: str,
        disciplina: str,
        quadro: list[QuadroCurricularDto],
        x: int,
        y: int,
        cor: tuple,
    ):
        _turma = next((e for e in quadro if e.turma == turma), None)
        index_disc = next(i for i, v in enumerate(_turma.disciplina) if v == disciplina)

        if not gui.pixelMatchesColor(x, y, cor, tolerance=10):
            input("ERROR!")
            return

        for el in range(index_disc):
            gui.sleep(self.sleep_time)
            gui.click(x, y)

    def alterar_plano_de_avaliacao(
        self,
        nome_avaliativo: str,
        plano_avaliativo: str,
        x: int,
        y: int,
        cor: tuple,
        pl_ava_x: int,
        pl_ava_y: int,
        next_x: int,
        next_y: int,
        next_cor: tuple,
        input_plano_x: int,
        input_plano_y: int,
        input_plano_cor: tuple,
        save_x: int,
        save_y: int,
        save_cor: tuple,
        close_x: int,
        close_y: int,
    ):
        pyperclip.copy("")
        gui.sleep(self.sleep_time)

        if not gui.pixelMatchesColor(x, y, cor, tolerance=10):
            input("TEMPO EXEDIDO")

        gui.click(x, y)
        gui.sleep(self.sleep_time)

        gui.click(pl_ava_x, pl_ava_y)
        gui.sleep(self.sleep_time)

        while True:

            gui.rightClick(pl_ava_x, pl_ava_y)
            gui.sleep(self.sleep_time)

            gui.press("down", presses=6, interval=0.1)
            gui.sleep(self.sleep_time)

            gui.press("enter")
            gui.sleep(self.sleep_time)

            gui.hotkey("ctrl", "c")

            content_type_ava = pyperclip.paste().strip()

            logger.info(f"Buscando PLano de ensino -> {nome_avaliativo}")
            if content_type_ava == nome_avaliativo:
                break
            logger.info("Buscando o Proximo")

            gui.sleep(self.sleep_time)

            if not gui.pixelMatchesColor(next_x, next_y, next_cor, tolerance=10):
                input("TEMPO EXEDIDO")

            gui.click(next_x, next_y)

        if not gui.pixelMatchesColor(
            input_plano_x, input_plano_y, input_plano_cor, tolerance=10
        ):
            input("TEMPO EXEDIDO")

        gui.click(input_plano_x, input_plano_y)
        content_plano = self.get_plano_avaliativo(plano_avaliativo)
        keyboard.write(content_plano, delay=0.04)

        if not gui.pixelMatchesColor(save_x, save_y, save_cor, tolerance=10):
            input("TEMPO EXEDIDO")

        gui.sleep(self.sleep_time)
        gui.click(save_x, save_y)

        gui.sleep(self.sleep_time)
        gui.click(close_x, close_y)

    def close_quadro_curricular(
        self,
        close_x: int,
        close_y: int,
        close_cor: tuple,
        select_turma_x: int,
        select_turma_y: int,
    ):
        if not gui.pixelMatchesColor(close_x, close_y, close_cor, tolerance=10):
            input("TEMPO EXEDIDO")

        gui.sleep(self.sleep_time)
        gui.click(close_x, close_y)

        gui.sleep(self.sleep_time)
        gui.click(select_turma_x, select_turma_y)
