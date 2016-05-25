# import packages
import scrapy
class DmozSpider(scrapy.Spider):
	name = "dmoz" # identifies the Spider, must be unique
	allowed_domains = ["dmoz.org"]
	start_urls = [ # URLs where spider will begin to crawl from
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response): # called with the downloaded response object of each start URL
	# parses response data and extracts scraped data
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)