# in bash:
# $ scrapy shell "http://www.fishbase.org/Nomenclature/FamilySearchList.php?Family=Lethrinidae"
# launches into ipython

# gets you the URLs for all species
# response.xpath('//body/table/tr/td/a/@href').extract()