import csv
import os

from pep_parse.settings import BASE_DIR

RESULTS_DIR = BASE_DIR / 'results'


class PepParsePipeline:
    def __init__(self):
        self.status_counts = {}
        self.total_count = 0
        self.RESULTS_DIR = RESULTS_DIR
        self.RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.base_dir = BASE_DIR

    def process_item(self, item, spider):
        status = item['status']
        self.status_counts.setdefault(status, 0)
        self.status_counts[status] += 1
        self.total_count += 1
        return item

    def close_spider(self, spider):
        filename = os.path.join(self.base_dir, 'results', f'status_summary_{spider.time}.csv')
        with open(filename, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in self.status_counts.items():
                writer.writerow([status, count])
            writer.writerow(['Total', self.total_count])
