from collections import defaultdict
import csv

from .constants import BASE_DIR, DIR_OUTPUT, FIELDS_NAME, FILE_NAME, TIME_NOW


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)
        self.result_dir = BASE_DIR / DIR_OUTPUT
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_dir = self.result_dir / FILE_NAME.format(time=TIME_NOW)
        self.results['Всего'] = sum(self.results.values())
        with open(file_dir, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(FIELDS_NAME)
            writer.writerows(self.results.items())
