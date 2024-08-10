import scrapy


class SvetilniknewparsSpider(scrapy.Spider):
    name = "svetilniknewpars"
    allowed_domains = ["svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/svetilniki-podvesnye"]

    custom_settings = {
        'FEEDS': {
            'output.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['name', 'price', 'url'],
            },
        },
    }

    def parse(self, response):
        svetilniks = response.css('li.item')
        for svetilnik in svetilniks:
            yield {
                'name': svetilnik.css('div.item-content p.product-name a').attrib['title'],
                'price': svetilnik.xpath('.//div[@class="price-box"]//span[@class="pprice"]/text()').get().strip(),
                'url': svetilnik.css('div.item-content p.product-name a').attrib['href']
            }
