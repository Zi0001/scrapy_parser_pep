import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        table_xpath = '//section[@id="numerical-index"]'
        link_xpath = './/a[contains(@href, "pep-")]/@href'
        for link in response.xpath(table_xpath).xpath(link_xpath):
            pep_url = link.get().rstrip('/') + '/'
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': response.css(
                'h1.page-title::text'
            ).re_first(r'PEP (\d+)'),

            'name': response.css(
                'h1.page-title::text'
            ).get().split(' – ')[-1],

            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get()
        }

        yield PepParseItem(data)
