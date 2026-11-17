import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


def configurar_logger(
    nome_arquivo: str = "execucao.log", nivel: int = logging.INFO
) -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    formato = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 1. Handler para exibir no terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formato)

    # 2. Handler para salvar em arquivo (máx. 5MB por arquivo, mantém os últimos 3)
    file_handler = RotatingFileHandler(
        log_dir / nome_arquivo,
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formato)

    # Configura o logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(nivel)

    # Evita duplicar logs se a função for chamada mais de uma vez
    if not root_logger.handlers:
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)
