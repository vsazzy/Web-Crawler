import scrapy
from ..items import headings

class ucllinks(scrapy.Spider):
    name = "ex"

    start_urls = [
        "https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/"
    ]

    def parse(self, response):
        items=headings()
        mainhead = response.css("#results a::attr(href)").extract()
        length=len(mainhead)
        subhead=[""]
        for i in range (length):
            x="http:"+str(mainhead[i])
            subhead.insert(0,x)
            #print(x)

        for url in subhead:
            yield scrapy.Request(url=url, callback=self.parse2)


    def parse2(self, response):
        items = headings()
        page = response.url.split("/")[-2]
        filename = 'ucl-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename)



        items['mainhead']=mainhead
        items['subhead']=subhead


        yield items

