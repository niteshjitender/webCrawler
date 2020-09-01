import scrapy
#scrapy startproject spider
# scrapy shell
# scrapy
# fetch('https://mohsinweb.herokuapp.com/quotes/')
# response.css('title::text').extract()
# quotes = response.css('div.quotes')
# author = quotes.css('p.author::text').extract()
# scrapy runspider quotes.py
# scrapy runspider quotes.py -o quotes.csv
# scrapy runspider quotes.py -o quotes.xml

###################Advance Spider functionality################
# scrapy shell "quotes.toscrape.com"
# response.xpath("//*[@class='quote']")
# Now dynamic xpath
# quote.xpath('.//a') //Dot for dynamic xpath
# quote.xpath('.//*[@class = "text"]/text()').extract()
# quote.xpath('.//*[@class = "text"]/text()').extract_first()
## OR
# quote.xpath('.//*[@itemprop = "text"]/text()').extract_first()
# quote.xpath('.//*[@class = "author"]/text()').extract_first()
# quote.xpath('.//*[@class = "keywords"]/@content').extract_first()
# scrapy crawl crawler1
# scrapy crawl crawler1 -o scraped_quotes.csv
# scrapy crawl crawler1 -o scraped_quotes.json
# scrapy crawl crawler1 -o scraped_quotes.xml

#To run spider on cloud visit https://www.scrapinghub.com/






class QuotesSpider(scrapy.Spider): #inherited
    name = 'crawler1' #name of spider
    # start_urls = [
    #     'https://mohsinweb.herokuapp.com/quotes'
    # ]
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # for quote in response.css("div.quotes"):
        #     yield {
        #         'quote': quote.css('p.aquote::text').extract(),
        #         'author':quote.css('p.author::text').extract_first(),
        #     } #They generate iterable on the fly
        container = response.xpath("//*[@class='quote']")
        for quote in container:
           text = quote.xpath('.//*[@class = "text"]/text()').extract_first()
           author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
           keywords = quote.xpath('.//*[@class = "keywords"]/@content').extract_first()

           # print('x'*20)
           # print(text)
           # print(author)
           # print(keywords)
           # print('x'*20)

           yield {
               'Text':text,
               'Author':author,
               'Key':keywords
           }

           #To traverse every page
           next_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
           abs_next_url = response.urljoin(next_url)
           yield scrapy.Request(abs_next_url)


