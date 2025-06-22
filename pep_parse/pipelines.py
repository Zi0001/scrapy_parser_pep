# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
from collections import defaultdict
from datetime import datetime


class PepParsePipeline:
    def process_item(self, item, spider):
        return item


class StatusSummaryPipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)
        self.total = 0

    def process_item(self, item, spider):
        status = item['status']
        self.status_counts[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        filename = f'results/status_summary_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            
            for status, count in sorted(self.status_counts.items()):
                writer.writerow([status, count])
            
            writer.writerow(['Total', self.total])