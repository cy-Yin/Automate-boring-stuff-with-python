#! python
# Opens several Bing search results.

import bs4, requests, sys, webbrowser


print("Searching ...") # display text while downloading the Bing page.
res = requests.get("https://cn.bing.com/search?q=" + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

# Retrieve top search result links.
BingSoup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result.
linkElems = BingSoup.select('.b_algo a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):    
    webbrowser.open(linkElems[i].get('href'))