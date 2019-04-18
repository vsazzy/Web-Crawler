import scrapy
from ..items import headings

class exeterentry(scrapy.Spider):
    name = "exeter"

    start_urls = [
        "https://www.exeter.ac.uk/undergraduate/degrees/computerscience/comsci/#Entry-requirements"
    ]

    def parse(self, response):
        items = headings()

        mainhead=response.css("h3::text").extract()
        subhead=response.css("#Entry-requirements p::text").extract()
        #value=response.css("::text").extract()

        items['mainhead'] = mainhead
        items['subhead'] = subhead
        #items['value'] = value

        yield items

