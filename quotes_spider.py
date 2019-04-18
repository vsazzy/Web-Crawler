import scrapy
from ..items import headings

class UCLinfo(scrapy.Spider):
    name = 'ucl'
    start_urls = [
        "https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/"
    ]

    def parse(self, response):
        info = []
        # getSub = input("Enter Subject Name")
        for subjects in response.css("td.degree-list__item>a"):
            info.append(
                [subjects.css('::text').get(),
                 subjects.css('::attr(href)').get()]
            )
        looksubject = 'Computer Science '

        link = ''
        for i in info:
            if (looksubject == i[0]):
                link = "https:" + i[1]
        print(link)

        if link != '':
            yield scrapy.Request(link, callback=self.parse2)

    def parse2(self, response):
        items=headings()
        mainhead= response.css("h3::text").extract()
        subhead= response.css("#entry-requirements dt::text").extract()
        value=response.css("#entry-requirements dd::text").extract()


        items['mainhead'] = mainhead
        items['subhead'] = subhead
        items['value'] = value

        yield items




