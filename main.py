import logging
from logging.handlers import RotatingFileHandler

from src import holidays

if __name__ == '__main__':
    logging.basicConfig(
        handlers=[RotatingFileHandler('holiday.log', maxBytes=200000, backupCount=1)],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt='%Y-%m-%dT%H:%M:%S')

    holidays.execute()
