import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://quotesfrombooks.tumblr.com']

    def parse(self, response):
        for title in response.css('.post'):
            yield {'text': title.css('.quote ::text').extract_first(), 
            		'author': title.css('.caption p ::text').extract_first()}

        next_page = response.css('.footer .pagination a.right  ::attr(href)').extract_first()
        print('NEXT PAGE URL: ' + str(response.urljoin(next_page)))
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse, dont_filter = True)