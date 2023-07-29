class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,number):
        real=self.real + number.real
        imag=self.imag + number.imag
        result=complex(real,imag)
        return result
    n1=complex(5, 6)
    n2=complex(-4, 6)
    result = n1.add(n2)
    print("Real:",result.real)
    print("Imag",result.imag)

       