import csv
import os
from collections import defaultdict

from pep_parse.settings import BASE_DIR

RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline:
    def __init__(self):
        self.RESULTS_DIR = RESULTS_DIR
        self.RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.base_dir = BASE_DIR
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_counts[status] += 1
        return item

    def close_spider(self, spider):
        filename = os.path.join(
            self.base_dir,
            'results',
            f'status_summary_{spider.time}.csv')
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([
                ['Статус', 'Количество'],
                *self.status_counts.items(),
                ['Total', sum(self.status_counts.values())]
            ])
