MTB project crawler for scraping mtb trails and inserting to json lines file.

## Crawl websites to extract trail url data

1. This project uses scrapy crawler to crawl for mtb trail data
    * Run the crawler using:<br>
        $ scrapy crawl mtbproject --logfile mtbproject.log -o mtbproject.jl:jsonlines
