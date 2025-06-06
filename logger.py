import logging
import os
from datetime import datetime

_logger = None

def get_logger():
    global _logger
    if _logger:
        return _logger

    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(logs_dir, f"run_{timestamp}.log")

    logger = logging.getLogger("readme_improver")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter("%(asctime)s - %(message)s", "%H:%M:%S")

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    _logger = logger
    return logger
