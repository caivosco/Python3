def p_decorate(f1):

    def wrapper(x):
        return f1(x)
    return wrapper

class Person():

    def __init__(self):
        self.name='L'
        self.family='H'

    @p_decorate
    def get_fullname(self):
        return self.name+self.family


A=Person()   
print(A.get_fullname())

