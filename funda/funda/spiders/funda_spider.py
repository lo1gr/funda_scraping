import scrapy
from ..items import FundaItem
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = "funda"

    def start_requests(self):
        urls = [
            'https://www.funda.nl/koop/amsterdam/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        yield {
            'price': response.xpath('//span[@class="search-result-price"]/text()').extract(),
            'address': response.xpath('//h4[@class="search-result__header-subtitle fd-m-none"]/text()').extract(),
            'size1': response.xpath('//ul[@class="search-result-kenmerken "]/li[1]/span[1]/text()').extract(),
            'size2': response.xpath('//ul[@class="search-result-kenmerken "]/li[1]/span[2]/text()').extract(),
            'rooms': response.xpath('//ul[@class="search-result-kenmerken "]/li[2]/text()').extract(),
            'link': response.xpath('//div[@class="search-result__header-title-col"]/a[1]/@href').extract()
        }

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        # //*[@id="default"]/div[1]/div/div/div/section/div[2]/ol/li[1]/article/h3/a




        # for house in response.css('search-result'):
        #     item["price"]    = house.css('div.search-result-info.search-result-info-price > span > font > font')
        #     item["size"]     = house.css('div.search-result-content > div > div:nth-child(3) > ul > li:nth-child(1) > span:nth-child(1) > font > font')
        #     item["address"]  = house.css('div.search-result-content > div > div:nth-child(3) > ul > li:nth-child(1) > span:nth-child(3) > font > font')

            # yield item

        # next_page = response.xpath('//*[@id="content"]/form/div[2]/nav/a/font/font').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)

        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')