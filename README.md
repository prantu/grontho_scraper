# Grontho Scraper
A Web crawler to create a list of all (download links) available books on http://grontho.com

# Usage
>>scrapy crawl grontho -o yourfilename.json

# Output 
[
  {
    "bookNumber": 1,
    "bookLink": "http://50.30.47.15/Ebook/English/Peace_and_its_Discontents.pdf",
    "bookTitle": "Peace and It’s Discontents",
    "pageLink": "http://www.grontho.com/peace-and-its-discontents/"
  },
  {
    "bookNumber": 2,
    "bookLink": "No PDF link is available",
    "bookTitle": "The Zahir",
    "pageLink": "http://www.grontho.com/the-zahir/"
  },
]
See full dump on this gist https://gist.github.com/prantu/2172bf412b5cb56b82f0858767fc2ea2
