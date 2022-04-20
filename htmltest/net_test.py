from urllib.request import urlopen
from subprocess import Popen, PIPE
import re
from urllib.request import urlopen
from html.parser import HTMLParser

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
#text = urlopen('http://python.org/jobs').read().decode()
#print(text)

def catch():
    for url, name in p.findall(text):
        print('{} ({})'.format(name, url))

#catch()

text2 = open('messy.html').read()
#print(text2)
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text2.encode())
tidy.stdin.close()
print(tidy.stdout.read().decode())


def isjob(url):
    try:
        a, b, c, d = url.split('/')
    except ValueError:
        return False
    return a == d == '' and b == 'jobs' and c.isdigit()

class Scraper(HTMLParser):
    in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get('href', '')
        if tag == 'a' and isjob(url):
            self.url = url
            self.in_link = True
            self.chunks = []
            #print('------------这是开始-------------------')

    def handle_data(self, data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_link:
            print('{} ({})'.format(''.join(self.chunks), self.url))
            #print('------------这是结束-------------------')
        self.in_link = False

text = urlopen('http://python.org/jobs').read().decode()
parser = Scraper()
parser.feed(text)
parser.close()


