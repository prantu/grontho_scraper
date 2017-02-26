# Scrapy settings for grontho project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'grontho'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['grontho.spiders']
NEWSPIDER_MODULE = 'grontho.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
#ITEM_PIPELINES = ['grontho.pipelines.BeevaPipeline']
