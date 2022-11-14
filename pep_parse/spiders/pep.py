from urllib.parse import urljoin

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_list = response.css('section#numerical-index tbody tr')
        for pep_url in pep_list:
            pep = urljoin(PepSpider.start_urls[0],
                          pep_url.css('td a::attr(href)').getall()[0])
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get().strip()
        status = response.css('dt:contains("Status") + dd::text').get()
        number = name.partition(' – ')[0]

        data = {
            'number': number.replace('PEP ', ''),
            'name': name,
            'status': status,
         }
        yield PepParseItem(data)
