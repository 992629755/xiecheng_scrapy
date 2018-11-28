# -*- coding: utf-8 -*-

# Scrapy settings for xiecheng_inland project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiecheng_inland'

SPIDER_MODULES = ['xiecheng_inland.spiders']
NEWSPIDER_MODULE = 'xiecheng_inland.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiecheng_inland (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
"Accept-Encoding": "gzip, deflate",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "_RSG=ZYKlH6j3z48HrkPK_sXi78; _RDG=28ee7dbb0465782286119067d8cd812376; _RGUID=813d0ed1-91bd-48a3-81ec-876fd466ed51; _abtest_userid=19107765-485c-45b7-bf69-9266b3b55dcd; _ga=GA1.2.923273751.1542181990; StartCity_Pkg=PkgStartCity=32; Visitor=1; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; traceExt=campaign=CHNbaidu81&adid=index; Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; gad_city=a4f35f7b1b0a14c597bf3a50fb024f55; ASP.NET_SessionSvc=MTAuOC4xODkuNTl8OTA5MHxqaW5xaWFvfGRlZmF1bHR8MTUzODA1MDQ4NTE5Ng; ASP.NET_SessionId=2rdn32x10uob1aufiaq2x2ps; _RF1=121.33.144.79; _gid=GA1.2.344611402.1543291984; MKT_Pagesource=PC; appFloatCnt=5; _bfa=1.1542181987050.2c3r09.1.1542626047142.1543291978907.4.26; _bfs=1.4; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1543292020326%7D%5D; _jzqco=%7C%7C%7C%7C1543291984760%7C1.1485011868.1542181990182.1543292002886.1543292020350.1543292002886.1543292020350.undefined.0.0.19.19; __zpspc=9.5.1543291984.1543292020.3%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfi=p1%3D104317%26p2%3D104317%26v1%3D26%26v2%3D25",
"Host": "vacations.ctrip.com",
"Upgrade-Insecure-Requests": 1,
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiecheng_inland.middlewares.XiechengInlandSpiderMiddleware': 543,
#
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'xiecheng_inland.middlewares.XiechengInlandDownloaderMiddleware': 543,
'xiecheng_inland.middlewares.SeleniumMiddleware':543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiecheng_inland.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


KEYWORDS = ['hainan']
MAX_PAGE = 3
SELENIUM_TIKEOUT = 20
PHANTOMJS_SERVICE_ARGS = None
MONGO_URI = 'localhost'
MONGO_DB = 'Xiecheng'