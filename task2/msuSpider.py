from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
import lxml
import json
import os

from urllib.parse import urlparse
import validators

IGNORED_EXTENSIONS = [
    '7z', '7zip', 'xz', 'gz', 'tar', 'bz2',   # archives
    'cdr',  # Corel Draw files
    'apk', # Android packages
]


def is_domen(st, base_domen):
    return (urlparse(st).netloc == urlparse(base_domen).netloc)
    

def count_links(links, base_domen, base_domen_short):
    internal = set()
    sub_domens = set()
    other = set()
    for item in links:
        if is_domen(item, base_domen):
            internal.add(item)
        elif not is_domen(item, base_domen) and base_domen_short in item:
            sub_domens.add(item)
        else:
            other.add(item)
    return len(internal), len(sub_domens), len(other)


def is_page(link):
    docs = [".pdf", ".jpg", ".jpeg", ".png", ".docx", ".doc"]
    for item in docs:
        if link.endswith(item):
            return False
    return True


class MySpider(CrawlSpider):

    name = 'myspider'
    allowed_domains = ['msu.ru']
    start_urls = ['https://msu.ru/', ]
    rules = (
        Rule(LxmlLinkExtractor(allow=(),deny=(r'^(https?)?//([^./]+\.){2,}[^./]+(/|$)'), deny_extensions=(['rtf']+IGNORED_EXTENSIONS)), callback='parse_item', follow=True),
    )
   
    def parse_item(self, response):
        root = lxml.html.fromstring(response.body)
        lxml.etree.strip_elements(root, lxml.etree.Comment, "script", "head")
        # page text
        # raw_text = lxml.html.tostring(root, method="text", encoding="utf-8")
        
        links = list(root.iterlinks())
        urls_for_count =[]
        
        for item in links:
            value = item[2]
            if item[1] == "href":
                if value.startswith("http") or value.startswith("www."):
                    urls_for_count.append(value)
                else:
                    flag = is_domen(self.start_urls[0] + value, self.start_urls[0]) and validators.url(self.start_urls[0] + value)
                    if flag:
                        urls_for_count.append(self.start_urls[0] + value)
        internal, sub_domens, other = count_links(urls_for_count,
                                                  base_domen=self.start_urls[0],
                                                  base_domen_short=self.allowed_domains[0])

        out = dict(
            link=response.url,
            internal_count=internal,
            sub_domens_count=sub_domens, 
            external_count=other,
            files=int(is_page(response.url))
            )
        
        with open('msu.txt', 'a') as outfile:
            json.dump(out, outfile)    


def start_new_crawl():
    settings = get_project_settings()
    settings.set('FEED_FORMAT', 'json')
    settings.set('FEED_URI', 'result.json')
    settings.set("FEED_EXPORT_ENCODING", 'utf-8')
    settings.set("CONCURRENT_REQUESTS", 32)
    settings.set("CONCURRENT_REQUESTS_PER_DOMAIN", 32)
    settings.set("RETRY_ENABLED", False)
    settings.set("DOWNLOAD_TIMEOUT", 5)
    settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36")
    # settings.set("DEPTH_LIMIT", 3)
    settings.set("LOG_ENABLED", True)
    configure_logging()
    runner = CrawlerRunner(settings)
    runner.crawl(MySpider)
    reactor.run()


if __name__ == "__main__":
    start_new_crawl()