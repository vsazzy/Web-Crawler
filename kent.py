import scrapy
from ..items import headings

class kententry(scrapy.Spider):
    name = "kent"

    start_urls = [
        "https://www.kent.ac.uk/courses/undergraduate/124/computer-science#entry"
    ]

    def parse(self, response):
        items = headings()

        mainhead=response.css("#entry h3::text").extract()
        subhead=response.css("tr td::text").extract()
        value=response.css(".ug-entry-requirements p::text").extract()

        items['mainhead'] = mainhead
        items['subhead'] = subhead
        items['value'] = value

        yield items

