from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
FILE_DIR = 'results'
PEP_FILE = FILE_DIR + '/pep_%(time)s.csv'
DATE_MASK = "%Y-%m-%d_%H-%M-%S"
BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    PEP_FILE: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
