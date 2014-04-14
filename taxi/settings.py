# Scrapy settings for taxi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'taxi'

SPIDER_MODULES = ['taxi.spiders']
NEWSPIDER_MODULE = 'taxi.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taxi (+http://www.yourdomain.com)'
