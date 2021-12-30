a = 1
def fn():
    def fn2() :
        a = 4
        print(3, a)
    return fn2

tmp = fn()

def gn(f):
    f()


gn(tmp)


print(8, a)
