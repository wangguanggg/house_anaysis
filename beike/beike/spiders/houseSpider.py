import scrapy
from ..items import BeikeItem
import re
class HousespiderSpider(scrapy.Spider):
    name = 'houseSpider'
    allowed_domains = ['bj.ke.com']
    start_urls = ['https://bj.ke.com/ershoufang/pg1/']
    num = 2
    def parse(self, response):
        currentpage_houses = response.xpath('//li[@class="clear"]')
        for houseItem in currentpage_houses:
            try:
                house = BeikeItem()
                house['title'] = houseItem.xpath('div/div/a/text()').extract()[0]
                house['address'] = houseItem.xpath('div/div[2]/div/div/a/text()').extract()[0]
                house_info = houseItem.xpath('div/div[2]/div[2]/text()[2]').extract()[0].split("|")
                house['unit_type'] = house_info[0].replace("\n", "").replace(" ", "")
                house['created_time'] = house_info[1].replace("\n", "").replace(" ", "")
                house['room_type'] = house_info[2].replace("\n", "").replace(" ", "")
                house['area'] = re.findall("\d+\.?\d*", house_info[3].replace("\n", "").replace(" ", ""))[0]
                house['toward'] = house_info[4].replace("\n", "").replace(" ", "")
                house['total_price'] = int(houseItem.xpath('div/div[2]/div[5]/div[1]/span/text()').extract()[0])
                house['unit_price'] = \
                re.findall('\d+\.?\d*', houseItem.xpath('div/div[2]/div[5]/div[2]/span/text()').extract()[0])[0]
                house['follows'] = re.findall('\d+\.?\d*', houseItem.xpath('div/div[2]/div[3]/text()[2]').extract()[0])[
                    0]
                yield house
            except Exception as e:
                print(e)
        if self.num <= 100:
            yield scrapy.Request('https://bj.ke.com/ershoufang/pg%s/' % self.num, callback=self.parse)
            self.num = self.num + 1
        pass


