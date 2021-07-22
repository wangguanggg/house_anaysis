import scrapy
from ..items import resthouseItem
import re
class ResthousespiderSpider(scrapy.Spider):
    name = 'resthouseSpider'
    allowed_domains = ['bj.zu.ke.com']
    start_urls = ['https://bj.zu.ke.com/zufang/rt200600000001/']
    num = 2
    def parse(self, response):
        currentpage_houses = response.xpath('//div[@class="content__list--item"]')
        print(currentpage_houses)
        for houseItem in currentpage_houses:
            try:
                house = resthouseItem()
                house['title'] = houseItem.xpath('div/p[1]/a/text()').extract()[0].replace(" ", "").replace("\n", "")
                house['room_type'] = houseItem.xpath('div/p[2]/text()[last()-1]').extract()[0].replace(" ", "").replace("\n", "")
                house['toward'] = houseItem.xpath('div/p[2]/text()[last()-2]').extract()[0].replace(" ", "").replace("\n", "")
                house['area'] = re.findall("\d+\.?\d*", houseItem.xpath('div/p[2]/text()[last()-3]').extract()[0])[0]
                house['month_price'] = houseItem.xpath('div/span/em/text()').extract()[0]
                yield house
            except Exception as e:
                print(e)
        if self.num <= 100:
            yield scrapy.Request('https://bj.zu.ke.com/zufang/pg%srt200600000001/#contentList' % self.num, callback=self.parse)
            self.num = self.num + 1
        pass
