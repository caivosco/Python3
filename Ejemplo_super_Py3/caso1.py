class Padre:

    def foo(self):
        return 10


class Hija(Padre):

    def foo(self):
        return 0

    def bar(self):
        n = super().foo()
        return n

instancia1 = Hija()
print(instancia1.foo()) # 0
print(instancia1.bar()) # 10

    
