import os,re
import fileinput, re
from random import choice,randrange
from distutils.log import warn
import bisect
import random
import openpyxl
from openpyxl import Workbook
#import pypiwin32
#import win32com.Client as win32

# 实例化
wb = Workbook()
# 激活 worksheet
ws = wb.active
# 保存表格
wb.save("test1.xlsx")

emphasis_pattern = r'\*+([^\*]+)\*+'
a = re.sub(emphasis_pattern, r'<em>\1</em>', 'Hell*o, ***wor*ld*!')
print(a)

b = re.sub(r'\*+(.+?)\*+',r'<em>\1</em>','pages of *World W**ide Sp*am***,')
print(b)


str = 'Subject: Re: Spam \
       From: Foo Fie <foo@bar.baz>\
    To: Magnus Lie Hetland <magnus@bozz.floop>\
    CC: <Mr.Gumby@bar.baz>\
    Message-ID: <B8467D62.84F%foo@baz.com>\
    In-Reply-To: <20041219013308.A2655@bozz.floop> Mime- version: 1.0\
    Content-type: text/plain; charset="US-ASCII" Content-transfer-encoding: 7bit\
    Status: RO\
    Content-Length: 55\
    Lines: 6\
    So long, and thanks for all the spam!\
    Yours,\
    Foo Fie'



pat = re.compile('From: (.*) <.*?>$')
for line in fileinput.input('1.txt'):
    m = pat.match(line)
    if m:
        print(m.group(1))


pat2 = re.compile(r'[a-z\-\.]+@[a-z\-\.]+', re.IGNORECASE)
addresses = set()
for line in fileinput.input('1.txt'):
    for address in pat2.findall(line):
        addresses.add(address)
for address in sorted(addresses):
    print(address)
    #warn(address)


fs = os.popen('tasklist /nh','r')
for eachLine in fs:
    #print(re.findall(r'([\w.]+(?: ([\w.]+)*))\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',eachLine.rstrip()))
    #print(re.findall(r'([\w.]+ ([\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)', eachLine.rstrip()))
    pass
fs.close()

print("choice('A String') : ",choice('A String'))

d = ''.join(choice('A String test hha') for i in range(randrange(1,10)))
print(d)
f = randrange(1,4)
print(f)
print(range(f))
print(randrange(10))
print(range(10))


SIZE=7
random.seed(1749)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)



