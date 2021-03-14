# funda_scraping
Scraping housing market nl through funda + playing with Scrapy


Scrapy documentation: 
https://docs.scrapy.org/en/latest/intro/tutorial.html

Funda website, for sale, only for amsterdam: https://www.funda.nl/koop/amsterdam/


## How to run:
To install the required packages:
`pip install -r requirements.txt`
1. cd to the folder funda
2. command line: scrapy crawl funda -O houses.json   (overwrites the json file previously created)
   scrapy crawl funda -o houses.json                 (appends to json file previously created)
   scrapy crawl funda                                (runs without saving information)