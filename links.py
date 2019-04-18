import scrapy
from ..items import headings

class ucllinks(scrapy.Spider):
    name = "ucllinks"

    start_urls = [
        "https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/"
    ]

    def parse(self, response):
        mainhead="https:"+str(response.css("#results a::attr(href)").extract())


        for url in mainhead:
            yield scrapy.Request(url=url, callback=self.parse2)

    def parse2(self,response):
        items=headings()
        page = response.url.split("/")[-2]
        filename = 'ucl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)

        items['mainhead'] = mainhead



        yield items


