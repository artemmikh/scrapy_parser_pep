import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Cобирает ссылки на документы PEP."""
        table = response.css('section#numerical-index table')
        tbody_tr = table.css('tbody tr')
        for tr in tbody_tr:
            link = tr.css('a.pep.reference.internal::attr(href)').get()
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит страницы с документами и формирует Items."""
        number_name = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': number_name[0].split(' ')[1],
            'name': number_name[1],
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
