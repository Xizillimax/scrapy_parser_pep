import scrapy

from pep_parse.items import PepParseItem

MESSAGE_RESPONSE_ERROR = 'Возникла ошибка {error} при загрузке страницы {url}'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        try:
            href_pep = response.xpath('//*[@id="numerical-index"]//tbody'
                                      '//a[@class="pep reference internal"]')
            for pep_url in href_pep:
                yield response.follow(pep_url,
                                      callback=self.parse_pep)
        except ConnectionError as error:
            raise ConnectionError(
                MESSAGE_RESPONSE_ERROR.format(error=error, url=href_pep))

    def parse_pep(self, response):
        title = response.xpath('//h1[@class="page-title"]/text()'
                               ).get().split(' – ')
        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.xpath(
                '//dt[contains(., "Status")]'
                '/following-sibling::dd/abbr/text()').get()
        }
        yield PepParseItem(data)
