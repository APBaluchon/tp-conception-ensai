from datetime import datetime
import pytz
import logging

timezone = pytz.timezone('Europe/Paris')

logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)

logging.info(f"Lancement du programme.")
logging.debug(f"Demande d'heure sur le timezone : {timezone}")

if timezone is None:

    logging.error("aucune timezone n'a été renseignée")

    raise ValueError("aucune timezone n'a été renseignée")