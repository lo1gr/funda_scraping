# funda_scraping
Scraping housing market nl through funda + playing with Scrapy


Scrapy documentation: 
https://docs.scrapy.org/en/latest/intro/tutorial.html

## Not to escape every time for loop element (took me a while)
https://stackoverflow.com/questions/37732649/scrapy-loop-xpath-selector-escaping-object-it-is-applied-to-and-returning-all

Funda website, for sale, only for amsterdam: https://www.funda.nl/koop/amsterdam/


## How to run:
To install the required packages:
`pip install -r requirements.txt`
1. cd to the folder funda
2. command line: scrapy crawl funda -O houses.json   (overwrites the json file previously created)
   scrapy crawl funda -o houses.json                 (appends to json file previously created)
   scrapy crawl funda                                (runs without saving information)

## Glossary
at the end of the prices in the raw file you can see:
k.k. & v.o.n.
The letters KK in housing adverts stand for ‘kosten koper’ (buyer’s costs). This means that all the costs involved in buying a house –  transferring ownership in the land registry, notarial costs for drawing up the contract and the 2% property transfer tax – are to be paid by the buyer. Together with the cost of your estate agent and mortgage broker, this adds around 6% to the price of a house, some of which is tax deductible. ‘VON’ (Vrij op Naam)  means that part of the costs involved are paid for by the seller. This relates to the transfer tax.

Read more at DutchNews.nl: