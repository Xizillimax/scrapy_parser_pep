import csv

from .constants import BASE_DIR, DIR_OUTPUT, FIELDS_NAME, FILE_NAME, TIME_NOW


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = dict()
        self.result_dir = BASE_DIR / DIR_OUTPUT
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        pep_status = item['status']
        if self.results.get(pep_status):
            self.results[pep_status] += 1
        else:
            self.results[pep_status] = 1
        return item

    def close_spider(self, spider):
        file_dir = self.result_dir / FILE_NAME.format(time=TIME_NOW)
        with open(file_dir, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='unix')
            writer.writerow(FIELDS_NAME)
            for key, value in self.results.items():
                writer.writerow([key, value])
            writer.writerow(['Всего', sum(self.results.values())])
