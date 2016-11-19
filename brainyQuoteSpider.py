import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    page = 0
    start_urls = ["https://www.brainyquote.com/search_results.html?q=morning&pg=%s" % page for page in xrange(1,10), "https://www.brainyquote.com/search_results.html?q=life&pg=%s" % page for page in xrange(1,10)]

    def parse(self, response):
        for title in response.css('.bq_list_i'):
        	if(len(title.css('.bqQuoteLink a ::text').extract_first())<160):
        		yield {'text': title.css('.bqQuoteLink a ::text').extract_first(), 
        		'author': title.css('.bq-aut a ::text').extract_first()}

      #  next_page = response.css('ul.pagination li.active ::attr(href)').extract_first()
      #  print('NEXT PAGE URL: ' + str(response.urljoin(next_page)))
      #  if next_page:
      #      yield scrapy.Request(response.urljoin(next_page), callback=self.parse, dont_filter = True)