class A:
    vc = 123  # Variável de classe

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()

a1.vc = 321

print(a1.vc)
print(a2.vc)  # Com a instância a var de classe não se altera
print(A.vc)

A.vc = 'alteração'

print(A.vc)