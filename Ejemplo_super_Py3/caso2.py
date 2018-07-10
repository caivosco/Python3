class A:

    def foo(self):
        print('Metodo foo desde la clase A')

class B(A):

    def foo(self):
        print('Metodo foo desde la clase B')

class C(A):
    
    pass

class D(C, B):
    
    def bar(self):
        super().foo()

instancia1 = D()
instancia1.bar()

print([clase.__name__ for clase in D.__mro__])
print(D.__mro__)
