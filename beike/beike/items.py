# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from beikeapp.models import sellhouse, resthouse
class BeikeItem(DjangoItem):
	django_model = sellhouse
	pass

class resthouseItem(DjangoItem):
	django_model = resthouse
	pass
