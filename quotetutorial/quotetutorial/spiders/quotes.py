import scrapy

from quotetutorial.items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domanins = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        # .urljoin获取一个绝对的url
        url = response.urljoin(next)
        # callback=self.parse回调函数 相当于重新请求url
        yield scrapy.Request(url=url, callback=self.parse)
