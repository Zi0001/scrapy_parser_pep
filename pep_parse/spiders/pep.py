import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for link in response.css('a.pep::attr(href)'):
            yield response.follow(link, callback=self.parse_pep)


            # yield {
            #     'link': link.get()
            # }
        # for pep in response.css('tbody tr::text'):
        #     yield {
        #         'number': pep.css('a.pep reference internal::text').get()
        #     }
    def parse_pep(self, response):
        data = {
            'number': response.css('h1.page-title::text').re_first(r'PEP (\d+)'),
            'name': response.css('h1.page-title::text').get().split(' – ')[-1],
            'status': response.css('dt:contains("Status") + dd abbr::text').get()
        }

        yield PepParseItem(data)
