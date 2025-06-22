# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path

# from settings import RESULTS_PATH

# class PepParsePipeline:
#     def process_item(self, item, spider):
#         return item
class PepParsePipeline:
    def __init__(self):
        self.status_counts = defaultdict(int)
        self.total = 0

    def open_spider(self, spider):
        # Используем RESULTS_PATH из settings.py
        from pep_parse.settings import RESULTS_PATH
        self.results_dir = RESULTS_PATH
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def process_item(self, item, spider):
        status = item['status']
        self.status_counts[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        filename = self.results_dir / f'status_summary_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, count in sorted(self.status_counts.items()):
                f.write(f'{status},{count}\n')
            f.write(f'Total,{self.total}\n')