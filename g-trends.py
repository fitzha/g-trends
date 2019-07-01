"""
Date: 2019-05-30
Author: John Fitzharris / @fitzhaj

Licensed under MIT. 
Please visit https://github.com/fitzha/g-trends for more information.
"""

import os
import ssl
import datetime
import urllib.request
import xml.etree.ElementTree as xml_tree

ssl._create_default_https_context = ssl._create_unverified_context

local_folder_path = "/xyz/enter-local-path-here/" # You need to change this!
rss_locale = "NZ"

search_terms = []
time_period = "daily"
xml_output_file = "keywords.xml"
plaintext_output_file = "keywords.txt"

google_trends_url = ("https://trends.google.com/trends/trendingsearches/{0}/rss?geo={1}"
                .format(time_period, rss_locale))

urllib.request.urlretrieve(google_trends_url, "{0}/{1}"
                .format(local_folder_path, xml_output_file))

element_tree = xml_tree.parse("{0}/{1}"
                .format(local_folder_path, xml_output_file))

tree_root = element_tree.getroot()

for keyword in tree_root.iter("title"):
    search_terms.append(keyword.text)

search_terms.remove("Daily Search Trends")
popular_searches = "\n".join(search_terms)

output = open("{0}/{1}".format(local_folder_path, plaintext_output_file), "w+")
output.write(popular_searches)
output.close()

os.remove("{0}/{1}".format(local_folder_path, xml_output_file))

# Print out for terminal
print()
for keyword in search_terms:
    print(keyword)
print()
print("Total keywords: {0}".format(len(search_terms)))
print("Output written to: {0}{1}".format(local_folder_path, plaintext_output_file))