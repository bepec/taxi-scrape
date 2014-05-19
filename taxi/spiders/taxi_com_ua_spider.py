from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from taxi.items import TaxiServiceItem


def generate_urls():
    template = "http://taxi.com.ua/category/{0}"
    return [template.format(num) for num in range(1, 28)]


def xpath_one(selector, xpath):
    return xpath_all(selector, xpath)[0]


def xpath_all(selector, xpath):
    return selector.xpath(xpath).extract()


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
        location = xpath_one(breadcumbs, 'a[2]/text()')
        name = xpath_one(breadcumbs, 'span/text()')
        phones = xpath_all(sel, '//div[@id="contSingleBlog"]//td[2]/text()')[1:]

        print location, name, phones

        item = TaxiServiceItem()
        item['name'] = name
        item['location'] = location[6:]
        item['phones'] = [phone.strip() for phone in phones]

        return item
