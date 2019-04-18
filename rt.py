import scrapy


class links(scrapy.Spider):
    name = "ucllink"

    def start_requests(self):
        urls = [
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-history-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-year-abroad-ba/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-biomedical-meng/2019',
            'http://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-chemical-beng/2019'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.txt' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)