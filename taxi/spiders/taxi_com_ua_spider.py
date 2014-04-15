from scrapy.spider import Spider


def generate_urls():
    template = "http://taxi.com.ua/category/{0}"
    return [template.format(num) for num in range(1, 28)]


class TaxiComUaSpider(Spider):
    name = "taxi.com.ua"
    allowed_domains = ["taxi.com.ua"]
    start_urls = generate_urls()

    def parse(self, response):
        pass
