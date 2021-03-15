import scrapy
from ..items import FundaItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "funda"

    def start_requests(self):
        urls = [
            'https://www.funda.nl/koop/amsterdam'
            # 'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i, house in enumerate(response.css('li.search-result')):
            yield {
                'price': house.xpath('.//span[@class="search-result-price"]/text()').get(),
                'address': house.xpath('.//h4[@class="search-result__header-subtitle fd-m-none"]/text()').extract() or 'na',
                'usable_area': house.xpath('.//ul[@class="search-result-kenmerken "]/li[1]/span[1]/text()').extract() or 'na',
                'plot_area': house.xpath('.//ul[@class="search-result-kenmerken "]/li[1]/span[2]/text()').extract() or 'na',
                'rooms': house.xpath('.//ul[@class="search-result-kenmerken "]/li[2]/text()').extract() or 'na',
                'link': house.xpath('.//div[@class="search-result__header-title-col"]/a[1]/@href').extract() or 'na'
            }

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)