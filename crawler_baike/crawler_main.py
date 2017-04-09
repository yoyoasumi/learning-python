# -*- coding: utf8 -*-

from crawler_baike import url_manager, html_downloader, html_parser, html_outputer


class Crawler(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url, url_amount):
        count = 1
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("[ Crawling No.%d URL: %s ... ]" % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == url_amount:
                    print("Crawling Finished")
                    break
                count += 1
            except Exception as e:
                print(e)
                print("Crawling Failure")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    url_amount = 10
    obj_crawler = Crawler()
    obj_crawler.crawl(root_url, url_amount)
