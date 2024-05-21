from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner
import re
import extruct
from sys import path
import os

PATH='/home/jandogonzales/Development/MachineLearning/mtb-project-crawler/crawler/spiders' 
path.append(PATH)
from JsonLineParser import JsonLineParser 

# clean the links that contain the same url with different query params
def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

# find the trail areas to parse
trailAreas = "trail_areas.txt"
def find_trail_areas():
    start_urls = []
    for line in open(trailAreas, "r"):
        start_urls.append(line.strip())
    return start_urls

# crawler that loops through current html page, extracts urls
# then passes this to a function for parsing html page contents
class MtbProjectCrawler(CrawlSpider):
    name = 'mtbproject'
    allowed_domains = ['www.mtbproject.com']
    #start_urls = ['https://www.mtbproject.com/directory/8009314/albuquerque']
    #start_urls = ['https://www.mtbproject.com/directory/8006911/arizona', 'https://www.mtbproject.com/directory/8007418/colorado']
    #start_urls = ['https://www.mtbproject.com/directory/8011785/southwestern-alberta']
    start_urls = []
    trail_urls = []
    #jlFile = os.getcwd() + "/mtbproject.jl"
    jlFile = "../../mtbproject.jl"

    # initialize method to open current jsonlines file and find
    # previously crawled urls, that way we don't save twice
    def __init__(self, name=None, **kwargs):
        super(MtbProjectCrawler, self).__init__()
        print("Check the list of parsed urls...")
        # import the JsonLineParser and parse the input jl file 
        parser = JsonLineParser()
        self.trail_urls = parser.parse(self.jlFile)
        self.start_urls = find_trail_areas() 
        print(f"start urls len = {len(self.start_urls)}")
        print(self.start_urls)
        print("----- json lines file parsed -----\n")

    # eliminate scraped urls that don't match mtbproject
    #        LinkExtractor(),
    #follow=True # allows the following of links from each response
    rules = [ 
        Rule(
            LinkExtractor(allow='trail/'),
            process_links=process_links,
            callback="parse_item",
            follow=True
        )
    ] 

    def parse_item(self, response):
        # extract contents from the trail url
        if response.url not in self.trail_urls:
            print(f"URL DNE: {response.url}") 
            data = {
                "url": response.url,
                "metadata": extruct.extract(
                    response.text,
                    response.url,
                    syntaxes=['opengraph', 'json-ld']
                )
            }
            print(data)
            print("\n")
            yield data 
        else:
            print(f"URL: {response.url} ALREADY EXISTS!\n") 
