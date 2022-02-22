import os

import requests
import markdownify
from bs4 import BeautifulSoup

path = os.getcwd()
output_directory = path + "/output"
node = 100

for node in range(101):
    url = "http://www.badorius.com/?q=node/" + str(node)
    file_md = str(output_directory) + str(node) + ".md"

    html = requests.get(url).text

    # convert html to markdown
    h = markdownify.markdownify(html, heading_style="ATX")

    # print markdown
    #print(h)

    carname="Swift"
    caryear="2000"
    carcolor="white"
    file = open(file_md, "w")
    file.write(h)
    file.close
