#!/usr/bin/python

class Creeper:

    # Function that get requested url from the Internet
    def get_page(self, url):
        try:
            import urllib
            return urllib.urlopen(url).read()
        except:
            return ""

    # Help function that return first link and end position of the link
    def get_next_target(self, page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

    # Function that extracts all links from requested page
    def get_all_links(self, page):
        links = set([])
        while True:
            url,endpos = self.get_next_target(page)
            if url:
                links.add(url)
                page = page[endpos:]
            else:
                break
        return links

    # Initial function that starts the web crawling on a particular URL
    def crawl_web(self, seed):
        tocrawl = set([seed])
        crawled = set([])
        index = {}
        graph = {}
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = self.get_page(page)
                self.add_page_to_index(index,page,content)
                outlinks = self.get_all_links(content)
                graph[page] = outlinks
                tocrawl.union(outlinks)
                crawled.add(page)
        return index, graph

    # Function that add word to the index
    def add_to_index(self, index, keyword, url):
        if keyword in index:
            index[keyword].append(url)
        else:
            # not found, add new keyword to index
            index[keyword] = [url]

    # Function that splits page into words and adds them to index
    def add_page_to_index(self, index, url, content):
        words = content.split()
        for keyword in words:
            self.add_to_index(index,keyword,url)


c = Creeper()
# TODO: make crawler behave accoridng robots.txt to be polite to others
index, graph = c.crawl_web('http://www.udacity.com/cs101x/urank/index.html');

from pprint import pprint
pprint(index)
