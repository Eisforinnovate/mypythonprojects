#retreiving useful info from webpages
#stock quotes from google finance
#get content from page, look for stock, retreive it

#span_id as base for quotes

import urllib
import re
import sys

symbol = sys.argv[0]
#get stock symnbol from command line
url = 'http://finance.google.com/finance?q='
#go 2 google finance and get quote
content = urllib.urlopen(url+symbol).read()
#download url from site and symbol
m =re.search('span id="ref."*(.*)<', content)
#search quote for element for span_id, 2nd grouping is what stock actually is
if m:
    quote = m.group(1)
else:
    quote = 'not quote for symbol: ' +symbol
print (quote)
    #if we have a match get in group, otherwise print error