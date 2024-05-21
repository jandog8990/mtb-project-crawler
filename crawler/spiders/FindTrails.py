import requests
from bs4 import BeautifulSoup

urls = 'https://www.mtbproject.com/directory/areas'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
links = soup.find_all("a")

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

# loop through the links and extract refs
trailAreas = []
count = 0
f = open("trail_areas.txt", "w")
for link in links:
    href = link.get('href')
    if href != None and "directory" in href: 
        if has_numbers(href): 
            f.write(href)
            f.write("\n")
            count += 1 
f.close() 
