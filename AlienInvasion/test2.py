from turtle import *

#input("Press <enter>")

'''
forward(100)
left(120)
forward(100)
left(120)
forward(100)
'''

people = {
'Alice': {
'phone': '2341',
'addr': 'Foo drive 23'
},
'Beth': {
'phone': '9102',
'addr': 'Bar street 42'
},

'Cecil': {
'phone': '3158',
'addr': 'Baz avenue 90'
}
}
#print(people['Alice']['phone'])
d = people.get('Alice','getget')
print(d)
print('Age:',',',42)
print('Hello,', end='换默认的换行符')
print('world!')
print('Hello,')
print('world!')
'''
name = ('What is your name?')
status = "friend" if name.endswith("?") else "stranger"
print(status)
'''
name = ''
while not name:
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))
help(print)

# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
'phone': 'phone number',
'addr': 'address'
}
name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 仅当名字是字典包含的键时才打印信息：
if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
