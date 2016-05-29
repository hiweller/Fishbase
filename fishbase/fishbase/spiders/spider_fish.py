import scrapy
import urlparse
import re
from fishbase.items import FishItem

class FishSpider(scrapy.Spider):
    name = "fish"

    # CHANGE FAMILY NAME TO FAMILY YOU WANT PICTURES OF
    family = "Lethrinidae"
    allowed_domains = ["fishbase.tw"]
    start_urls = ["http://www.fishbase.tw/Nomenclature/FamilySearchList.php?Family="+family]

    def parse(self, response):

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


