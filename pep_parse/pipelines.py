import collections
import csv
import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
FILE_DIR = 'results'
DATE_MASK = "%Y-%m-%d_%H-%M-%S"
PEP_FILE = FILE_DIR + '/pep_%(time)s.csv'


class PepParsePipeline:
    pep_sum = collections.defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_path = BASE_DIR / FILE_DIR
        result_path.mkdir(exist_ok=True)
        now_time = datetime.datetime.now().strftime(DATE_MASK)
        file_path = result_path / f'status_summary_{now_time}.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv_writer = csv.writer(f, dialect=csv.unix_dialect)
            csv_writer.writerows([
                [('Статус'), ('Количество')],
                *self.pep_sum.items(),
                ['Total', sum(self.pep_sum.values())]
            ])
