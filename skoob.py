import scrapy

#scrapy runspider skoob.py -o reviews.json
#scrapy runspider skoob.py

class QuotesSpider(scrapy.Spider):
    name = 'reviews'
    start_urls = [
        'https://www.skoob.com.br/livro/resenhas/247555/edicao:277187'
    ]
    #download_delay = 1.5

    def parse(self, response):
        for quote in response.css('.curva2-5'):
            yield {
                'texto': quote.css('div').extract_first(),
                
            }

        
        link_next = response.css('div.proximo a::attr("href")').extract_first()
        if link_next:
            yield scrapy.Request(response.urljoin(link_next))