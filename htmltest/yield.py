def foo():
    print("starting...")
    while True:
        res = yield 4
        print('12321')
        if res:
            print('res=%s'% res)
        else:
            print('res值为%s'% res)
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
#print("-"*20)
#print(next(g))