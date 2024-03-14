import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DIR_OUTPUT = 'results'

FIELDS_NAME = ('Статус', 'Количество')
FILE_NAME = 'status_summary_{time}.csv'

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
TIME_NOW = dt.datetime.now().strftime(DT_FORMAT)

NAME_PEPSPIDER = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']
