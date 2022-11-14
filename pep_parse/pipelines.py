import collections
import csv
import datetime

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATE_MASK = "%Y-%m-%d_%H-%M-%S"


class PepParsePipeline:
    pep_sum = collections.defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.pep_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_path = BASE_DIR / 'results'
        result_path.mkdir(exist_ok=True)
        now_time = datetime.datetime.now().strftime(DATE_MASK)
        name_file = f'status_summary_{now_time}.csv'
        file_path = result_path / name_file
        results = ['Статус,Количество']
        with open(file_path, mode='w', encoding='utf-8') as f:
            csv_writer = csv.writer(f, dialect=csv.unix_dialect)
            total = sum(self.pep_sum.values())
            csv_writer.writerows([
                results,
                *self.pep_sum.items(),
                ['Total', total]
            ])
