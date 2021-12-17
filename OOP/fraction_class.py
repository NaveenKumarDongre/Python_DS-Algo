class Fraction:

    def __init__(self, num=0, den=1):
        if den == 0:
            # Throw error
            den = 1
        self.num = num
        self.den = den

    def print(self):

        if self.num == 0:
            print(0)
        elif self.den == 1:
            print(self.num)
        else:
            print(self.num, '/', self.den)

    def simplify(self):
        if self.num == 0:
            self.den = 1
            return
        current = min(self.num, self.den)
        while current > 1:
            if self.num % current == 0 and self.den % current == 0:
                break
            current -= 1

        self.num = self.num//current
        self.den = self.den//current

    def add(self, other_fraction):
        new_num = other_fraction.den*self.num + other_fraction.num*self.den
        new_den = other_fraction.den * self.den
        self.num = new_num
        self.den = new_den
        self.simplify()

    def multiply(self, other_fraction):
        new_num = other_fraction.num*self.num
        new_den = other_fraction.den*self.den

        self.num = new_num
        self.den = new_den

        self.simplify()


f1 = Fraction(2, 3)
f2 = Fraction(1, 3)
# f1.add(f2)
f1.multiply(f2)
f1.print()
