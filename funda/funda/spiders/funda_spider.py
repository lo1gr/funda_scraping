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
 
        # for results in response.xpath('//ol[@class="search-results"]'):
        #     yield {
        #         #  'price': results.css('li.search-result div.search-result-content div.search-result-content-inner::text').get()
        #         'test': str(results),
        #         'price': str(results.xpath('//li[@class="search-result"]/div/div[2]/div/div[2]/span/text()'))
        #         # li[1]/div/div[2]/div/div[2]/span
        #     }
            

        #     # print(results.xpath('//li[1]/span[@class="search-result-price"]/text()').get())
        #     # print(results.xpath('//li[2]/span[@class="search-result-price"]/text()').get())
        #     # print(results.xpath('//li[3]/span[@class="search-result-price"]text()').get())
        #     # print('count')
        # #     print(results.xpath('//ol/@start').get())
        for j, results in enumerate(response.css('ol.search-results')):
            for i, house in enumerate(results.css('li.search-result')):
                string = '//li['+str(i+1+j)+']/div/div[2]/div/div[2]/span/text()'
                yield {
                    'lol': str(house),
                    'price': house.xpath(string).get(),
                    # 'price2': response.xpath('//span[@class="search-result-price"]/text()').extract(),
                    # 'address': house.xpath('//h4[@class="search-result__header-subtitle fd-m-none"]/text()').extract() or 'na',
                    # 'size1': house.xpath('//ul[@class="search-result-kenmerken "]/li[1]/span[1]/text()').extract() or 'na',
                    # 'size2': house.xpath('//ul[@class="search-result-kenmerken "]/li[1]/span[2]/text()').extract() or 'na',
                    # 'rooms': house.xpath('//ul[@class="search-result-kenmerken "]/li[2]/text()').extract() or 'na',
                    # 'link': house.xpath('//div[@class="search-result__header-title-col"]/a[1]/@href').extract() or 'na'
                }

        # for quote in response.css('div.quote'):
        #     yield {
        #         'lol': str(quote),
        #         'text': quote.css('span.text::text').get(),
        #         'text2': quote.xpath('//span//text()').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }


        # next_page = response.xpath('//a[@rel="next"]/@href').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)