import scrapy
import urlparse
import re
from Lethrinids.items import FishItem

class LethrinidSpider(scrapy.Spider):
    name = "fish"
    allowed_domains = ["fishbase.tw"]
    start_urls = ["http://www.fishbase.tw/Nomenclature/FamilySearchList.php?Family=Lethrinidae"]

    # def parse(self, response):
    #   species_names = response.xpath('//td/a/i/text()').extract()
    #   species_urls = response.xpath('//td/a/@href').extract()

    #   for n in range(len(species_names)):
    #       item = FishItem()
    #       item['species'] = species_names[n]
    #       item['url'] = species_urls[n]
    #       yield item

    def parse(self, response):
        # dont_filter=True

        # picks up all the links to species pages for this family
        for href in response.xpath("//td/a/@href").extract():
            species_url = response.urljoin(href)

            # changes out PHP query with permalink to species page
            parl = urlparse.urlparse(species_url)
            parl2 = parl.scheme + "://" + parl.netloc + re.sub("SpeciesSummary.php", "", parl.path) + parl.query[3:]
            
            yield scrapy.Request(parl2, self.parse_species)

    def parse_species(self, response):
        # actually i think this works now?
        pics = response.css('span.slabel8').xpath("a[contains(., 'Pictures')]")
        pics_url = response.urljoin(pics.xpath("@href").extract_first())
        yield scrapy.Request(pics_url, self.parse_pics)

    def parse_pics(self, response):
        thumbs = response.xpath("//span/img/@src[contains(., 'species')]").extract()
        species = response.xpath("//td/font/i/a/text()").extract_first()

        for href in thumbs:
            url = response.urljoin(href)
            yield FishItem(species=species, image_urls=[url])
            # print(response.urljoin(href))

        # for n in range(len(species_names)):
        #   item = FishItem()
        #   item['species'] = species_names[n]
        #   item['url'] = response.urljoin(species_urls[n])
        #   yield item

        # for every link to a species in the page, parse_species it
        # for href in response.css("td > a::attr('href')"):
        # for n in range(len(species_urls)):
        #   # i have no idea if this is right
        #   url = response.urljoin(species_urls[n])
        #   print(url)
            # yield scrapy.Request(url, self.parse_species)


    # for every link, go to the pictures page and get info from every picture
    # def parse_species(self, response):
    #   pics = response.css('span.slabel8').xpath("a[contains(., 'Pictures')]")
    #   pics_url = response.urljoin(pics.xpath('@href').extract_first())
    #   yield scrapy.Request(pics_url, self.parse_pics)

    # def parse_pics(self, response):
    #   # once on picture thumbnails page, extracts all urls for images

    #   thumbs = response.xpath("//span/img/@src[contains(., 'species')]").extract()

    #   for n in range(len(thumbs)):
    #       thumb_url = response.urljoin(thumbs[n])
    #       print(thumb_url)



            
            # yield scrapy.Request(url, self.parse_species)
            # pics_url = response.
            # print url

    


