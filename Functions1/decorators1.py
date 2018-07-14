def makebold(fn1):
    
    def wrapped1():
        return '<b>' + fn1() + '</b>'

    return wrapped1

def makeitalic(fn2):

    def wrapped2():
        return '<i>' + fn2() + '</i>'

    return wrapped2

@makebold
@makeitalic
def hello():
    return 'hello friends'

print(hello())


