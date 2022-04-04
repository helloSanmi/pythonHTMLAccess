import urllib.error
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

##using beautifulsoup library to parse HTML
url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# #retrieve all of the anchor tags
# tags = soup('a')
# counts = 0
# for tag in tags:
#     counts = counts + 1
#     print(tag.get('href', None))
# print('Count:', counts)


##using Beautiful soup to pull out various parts of each tag
#
# #retrieve all of the anchor tags
# tags = soup('a')
# #look at the parts of a tag
# for tag in tags:
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)


##scraping numbers from HTML using BeautifulSoup
#
# #retrieve span tag
# tags = soup('span')
# sum = 0
# for tag in tags:
#     sum = sum + int(tag.contents[0])
#     print('TAG:', tag)
# print(sum)


##using Beautiful soup to pull out various parts of each tag

# ignore SSL certificate errors
#
# #retrieve all of the anchor tags
# tags = soup('a')
# #look at the parts of a tag
# for tag in tags:
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)

##using position and count to retrieve tag
pos = int(input('Enter position: '))-1
repeat = int(input('Enter count: '))
# tags = soup('a')
# sequence = []
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # link = tags[pos].get('href', None)
    # print('Retrieving: ', link)
    # print(tags[pos].contents[0])
    # sequence.append(tags[pos].contents[0])
    counts = 0
    for tag in tags:
        counts = counts + 1

        if counts > pos: break
        url = tag.get('href', None)
        name = tag.contents[0]
        print('Retrieving:', url)

print(name)



