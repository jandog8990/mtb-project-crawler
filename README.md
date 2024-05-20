MTB project crawler for scraping mtb trails and inserting to json lines file.
This json lines file will be used to extract trail data/metadata for DBs.

## Crawl websites to extract trail url data

1. This project uses scrapy crawler to crawl for mtb trail data
    * Run the crawler using:<br>
        $ cd crawler/spiders 
        $ scrapy crawl mtbproject --logfile mtbproject.log -o mtbproject.jl

    * View the updated json list file
        $ tail -f mtbproject.jl
