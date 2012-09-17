#!/usr/bin/python
import sys
import time
import getopt
from pprint import pprint

# Function that get requested url from the Internet
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

# Help function that return first link and end position of the link
def get_next_target(page):
    # TODO: Add ability to restrict creeper for domain only
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Function that extracts all links from requested page
def get_all_links(page):
    links = set([])
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.add(url)
            page = page[endpos:]
        else:
            break
    return links

# Initial function that starts the web crawling on a particular URL
def crawl_web(seed, max_depth):
    # TODO: make crawler behave accoridng robots.txt to be polite to others
    url_parse(seed) 
    tocrawl = set([seed]) # Set of links that will be crawled
    crawled = set([]) # Set of links that has been crawled
    nextcrawl = set([]) # Set of links with current depth
    depth = 0
    index = {}
    graph = {}
    while tocrawl and max_depth >= depth:
        page = tocrawl.pop()
        if page not in crawled:
            start_time = time.time() # measure crawling time
            content = get_page(page)
            add_page_to_index(index,page,content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            nextcrawl = nextcrawl.union(outlinks) # outlinks for next depth
            crawled.add(page)
            if verbose:
                print 'URL: ' + page
                print 'Number of links: ' + str(len(outlinks))
                print 'Crawl time: ' + str(time.time() - start_time) + ' sec'
        if not tocrawl: # test if anything is in current depth to crawl
            # move stored links for next depth to crawl Set
            tocrawl, nextcrawl = nextcrawl, set([])
            depth += 1 # increase depth to next level
            if verbose:
                print '-----------------------'
                print 'Entering depth: ' + str(depth)
                print 'Links to crawl: ' + str(len(tocrawl))
    return index, graph

# Function for URL parsing
def url_parse(url):
    from urlparse import urlparse
    o = urlparse(url)
        pprint(o)

# Function that add word to the index
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        # not found, add new keyword to index
        index[keyword] = [url]

# Function that splits page into words and adds them to index
def add_page_to_index(index, url, content):
    # TODO: Add  better algorithm to get the key words
    # TODO: Make keywords collection optional
    words = content.split()
    for keyword in words:
        add_to_index(index,keyword,url)

# Function that shows manual page to user
def usage():
    print '''NAME
    Creeper - Python web crawler

SYNOPSIS
    creeper [-u|--url <value>] [-d|--depth] [-v|--verbose] [-h|--help]

DESCRIPTION
    Simple web crwaler written in Python.

OPTIONS
    -u, --url <value>
        The <value> is mandatory argument, with website url that starts the
        crawling.
    -d, --depth <value>
        Define depth how far should Creeper crawl from the root url. The
        <value> is mandatory argumnet and can be any positive integer. If not
        specified default value 10 is used.
    -v, --verbose
        Cause Creeper to be verbose, showing url crawled, with some statistical
        data that has been retrieved.
    -h, --help
        Prints the synopsis and a list of the most commonly used commands.

LICENCE
    Copyright (C) 2012  Richard Kellner

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

def main(argv):
    start_time = time.time() # measure script execution time
    try:
        opts, args = getopt.getopt(argv, "u:d:vh", ["url=", "depth=", "verbose", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    # predefined values that can be passed as parameter
    global verbose
    verbose = False
    url = 'http://www.udacity.com/cs101x/urank/index.html'
    depth = 10
    for opt, arg in opts: # Loop throught parameters and set variables
        if opt in ("-u", "--url"):
            url = arg
        if opt in ("-d", "--depth"):
            if arg.isdigit(): # Only positive integer is valid input
                depth = int(arg)
            else:
                print arg + ' is not an digit, please try run with parameter -h'
                sys.exit(2)
        if opt in ("-v", "--verbose"):
            verbose = True
        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    # TODO: Add ability to store / export / print
    index, graph = crawl_web(url, depth)
    #pprint(index)
    #pprint(graph)
    if verbose:
        print '==========================================='
        print 'Total pages crawled: ' + str(len(graph))
        print 'Total execution time: ' + str(time.time() - start_time) + ' seconds'

if __name__ == "__main__":
    main(sys.argv[1:])
