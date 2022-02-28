from operator import add


class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    while True:
        menu = input('0.Exit 1.연산자 (+, -, *,/)')
        if menu == 0:
            break
        if menu == '+':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            calc = Calculator(num1, num2)
            print('*'*30)
            print(f'{calc.add()}')


