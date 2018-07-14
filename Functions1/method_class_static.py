class A():
    
    def foo(self, x):
        print('executing foo(%s, %s)'%(self, x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo(%s, %s)'%(cls, x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)'%x)

a=A()

A.class_foo(1)
a.class_foo(10)
print(a.class_foo)
print(A.class_foo)

a.static_foo(5)
A.static_foo(15)
print(a.static_foo)
print(A.static_foo)

a.foo('a')
A.foo('b')
