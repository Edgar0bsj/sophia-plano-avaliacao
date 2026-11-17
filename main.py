from pathlib import Path

from module.logger.logger_config import configurar_logger
from module.plano_avaliativo_facade import load_csv, run

configurar_logger()


def main():
    file_path = Path("input/soph.csv")
    quadro_curricular_path = Path("input/quadro_curricular.csv")

    plano, quadro = load_csv(file_path, quadro_curricular_path)

    run(plano, quadro)


if "__main__" == __name__:
    main()
    # gui.mouseInfo()
