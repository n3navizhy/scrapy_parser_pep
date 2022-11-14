import collections
import csv
import datetime

from pep_parse.settings import BASE_DIR, FILE_DIR, DATE_MASK


class PepParsePipeline:
    def __init__(self):
        self.result_path = BASE_DIR / FILE_DIR
        self.result_path.mkdir(exist_ok=True)
        self.pep_sum = {}

    def open_spider(self, spider):
        self.pep_sum = collections.defaultdict(int)

    def process_item(self, item, spider):
        self.pep_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        now_time = datetime.datetime.now().strftime(DATE_MASK)
        file_path = self.result_path / f'status_summary_{now_time}.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv.writer(f, dialect=csv.unix_dialect).csv_writer.writerows([
                [('Статус'), ('Количество')],
                *self.pep_sum.items(),
                ['Total', sum(self.pep_sum.values())]
            ])
