import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, NAME_PEPSPIDER, START_URLS
from pep_parse.items import PepParseItem

MESSAGE_RESPONSE_ERROR = 'Возникла ошибка {error} при загрузке страницы {url}'


class PepSpider(scrapy.Spider):
    name = NAME_PEPSPIDER
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        try:
            href_pep = response.css('section#numerical-index tbody '
                                    'a[class="pep reference internal"]')
            for pep_url in href_pep:
                yield response.follow(pep_url,
                                      callback=self.parse_pep)
        except ConnectionError as error:
            raise ConnectionError(
                MESSAGE_RESPONSE_ERROR.format(error=error, url=href_pep))

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().split(' – ')
        data = {
            'number': title[0][4:],
            'name': title[1],
            'status': response.css('dt:contains("Status") + '
                                   'dd > abbr::text').get()
        }
        yield PepParseItem(data)
