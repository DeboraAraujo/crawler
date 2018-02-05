import scrapy

#scrapy runspider skoob.py -o stars.json
#scrapy runspider skoob.py

class QuotesSpider(scrapy.Spider):
    name = 'stars'
    start_urls = [
        'https://www.skoob.com.br/livro/resenhas/354/edicao:228'
    ]
    #download_delay = 1.5

    def parse(self, response):
        for quote in response.css('.div style'):
            yield {
                'texto': quote.css('starting rate').extract_first(),
                
            }

        
        link_next = response.css('div.proximo a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))