import scrapy
from ..items import FundaItem


class QuotesSpider(scrapy.Spider):
    name = "funda"

    def start_requests(self):
        urls = [
            'https://www.funda.nl/koop/amsterdam/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = FundaItem()

        print("HELLLO")

        for house in response.css('search-result'):
            item["price"]    = house.css('div.search-result-info.search-result-info-price > span > font > font')
            item["size"]     = house.css('div.search-result-content > div > div:nth-child(3) > ul > li:nth-child(1) > span:nth-child(1) > font > font')
            item["address"]  = house.css('div.search-result-content > div > div:nth-child(3) > ul > li:nth-child(1) > span:nth-child(3) > font > font')

            yield item

        next_page = response.xpath('//*[@id="content"]/form/div[2]/nav/a/font/font').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')