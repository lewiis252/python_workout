import logging
logger = logging.getLogger(__name__) # make nonstandard log
handler = logging.StreamHandler()  # definition of stream

logger.setLevel(logging.WARNING)
handler.setLevel(logging.ERROR)
format_c = logging.Formatter("%(name)s - $(levelname)s - %(message)s")
handler.setFormatter(format_c)
logger.addHandler(handler)

def division(divident, divisor):
    try:
        return divident/divisor
    except ZeroDivisionError:
        logger.error('Dividing by 0')

num = division(4, 0)