import re
import constants.valiation_patterns as patterns


# Para quitar los espacios en blanco delante y detrás del texto.
def clean_text(text):
    text = text.strip()
    return text


# Comprueba el título.
def check_title(title):
    title = clean_text(title)
    pattern = re.compile(patterns.TITLE)
    result = pattern.match(title)
    return result != None


# Comprueba el interprete.
def check_performer(performer):
    performer = clean_text(performer)
    pattern = re.compile(patterns.PERFORMER)
    result = pattern.match(performer)
    return result != None
