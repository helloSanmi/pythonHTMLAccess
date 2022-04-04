#search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verfy_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())