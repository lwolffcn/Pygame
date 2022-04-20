#import sys

dictA = {}
dictB = {}
dictC = {}
#print(dictC.keys())
#print(dictC.values())
def a(strings):
    for s in strings:
        if len(dictA) == 0:
            dictA[s] = 1
            #print(dictA)
        else:
            for k, v in dictA.items():
                if s == k:
                    dictA[s] = int(v) +1
                    break
                else:
                    dictA[s] = 1
                    break

def b(strings):
    for s in strings:
        if len(dictB) == 0:
            dictB[s] = 1
            #print(dictA)
        else:
            if s not in dictB.keys():
                dictB[s] = 1
                #print("字母%s不重复，次数设为1" %s)
            else:
                dictB[s] = dictB[s] + 1
                #print("字母%s重复，次数为%d" %(s, dictB[s]))

def c(strings):
    for s in strings:
        if s not in dictC.keys():
            dictC[s] = 1
            #print("字母%s不重复，次数设为1" %s)
        else:
            dictC[s] = dictC[s] + 1
            #print("字母%s重复，次数为%d" %(s, dictC[s]))
    #return dictC



#a("qazq")
#print(dictA)
#b("qeqweq")
#print(dictB)

c("wwq")
#print(dictC)

for k, v in dictC.items():
    #print(k + v)
    print("字母%s出现了：%d次；"%(k,v))

print('''This is a very long string. 'It'continues here.
And it's not over yet. "Hello, world!"
Still here.''')
print('C:\nowhere')
print(r'C:\nowhere')
print(r'C:\nowhere\\')

a = "This is a cat: \N{Pig}"
#print(a)


storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]

print(storage)
print(storage['middle']['Lie'])