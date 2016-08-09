import urllib.request
from http.cookiejar import CookieJar

url = 'http://www.cnblogs.com/txw1958/archive/2011/12/21/2295698.html'

# The first way
response = urllib.request.urlopen(url)
html = response.read()
status = response.getcode()
print(status)
print(html)

# The second way
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
html2 = response2.read()
status2 = response2.getcode()
print(status)
print(html)

# The third way
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
html = response3.read()
status = response3.getcode()
print(status)
print(cj)
print(html)
