from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import DmozItem

class DmozSpider(Spider):
  name = "dmoz"
  allowed_domains = ["dmoz.org"]
  start_urls = [
    "http://www.flightclub.com/air-jordan-9-retro-johnny-kilroy-black-metallic-platinum-gym-red-011630"
  ]
  
  def parse(self, response):
    sel = Selector(response)
    sites = sel.xpath('//ul/li')
    for site in sites:
      item = DmozItem()
      item['title'] = site.xpath('//*[@id="entire-page-wrap"]/div[3]/div[2]/div/div[2]/div[2]/div[1]/h1').extract()
      item['link'] = site.xpath('//*[@id="entire-page-wrap"]/div[3]/div[2]/div/div[2]/div[1]/div[1]/a/img').extract()
      item['desc'] = site.xpath('//*[@id="entire-page-wrap"]/div[3]/div[2]/div/div[2]/div[2]/ul/li[1]/text()').extract()
      return item
      
 