from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


def generate_urls():
    template = "http://taxi.com.ua/category/{0}"
    return [template.format(num) for num in range(1, 28)]


class TaxiComUaSpider(CrawlSpider):
    name = "taxi.com.ua"
    allowed_domains = ["taxi.com.ua"]
    start_urls = generate_urls()
    rules = (
        Rule(SgmlLinkExtractor(allow=('ru/\d+',)),
             callback='parse_taxi'),
    )

    def parse_taxi(self, response):
        self.log('Parsing page: {0}'.format(response.url))

        sel = Selector(response)
     
        breadcumbs = sel.xpath('//div[@id="DMbreadcumbs"]')
        location = breadcumbs.xpath('a[2]/text()').extract()[0]
        name = breadcumbs.xpath('span/text()').extract()[0]
        phones = sel.xpath('//div[@id="contSingleBlog"]//td[2]/text()').extract()

        self.log('Item: {0} - {1} - {2}'.format(location, name, phones))
