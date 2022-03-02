import random
import statistics
from random import randrange, randint


class Quiz01Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        if self.op == '+':
            return self.num1 + self.num2
        elif self.op == '-':
            return self.num1 - self.num2
        elif self.op == '*':
            return self.num1 * self.num2
        elif self.op == '/':
            return self.num1 / self.num2


class Quiz02Bmi(object):
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getBmi(self):
        bmires = self.weight / (self.height * self.height) * 10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade:
    def __init__(self, name, eng, kor, math):
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math

    def sum(self):
        return self.eng + self.kor + self.math

    def avg(self):
        return self.eng + self.kor + self.math / 3


class Quiz04GradeAuto:
    def __init__(self, name, eng, kor, math):
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math

    def sum(self):
        return self.eng + self.kor + self.math

    def avg(self):
        return self.eng + self.kor + self.math / 3

    def getGrade(self):
        pass

    def chkPass(self):
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz07RandomChoice(object):
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def choiceMember(self):
        ran = myRandom(0, 24)
        return self.members[ran]


class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.rps = ['가위', '바위', '보']
        self.com = random.randint(1, 3)

    def battle(self):
        if self.user == self.com:
            return f'Draw'
        elif (self.user - 1) % 3 == self.com % 3:
            return f'Win'
        else:
            return f'Lose'


class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object):  # 책받침구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    while True:
        menu = input('0.Exit 1.계산기 (+, -,*,/) 2.bmi 3.Grade 4.AutoGrade 5.Dice '
                     '6.RandomGenerator 7.RandomChoice 8.Rps 9.GetPrime 10.LeapYear '
                     '11.NumberGolf 12.Lotto 13.Bank 14.Gugudan')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), str(input('연산자')), int(input('두번째 수')))
            res = f'{q1.num1} {q1.op} {q1.num2} = {q1.calc()}'
        elif menu == '2':
            bmi = Quiz02Bmi(input('이름 : '), int(input('키 : ')), int(input('몸무게 : ')))
            res = f'이름: {bmi.name}, 키: {bmi.height},' \
                  f'몸무게: {bmi.weight}, BMI 상태:{bmi.getBmi()}'
        elif menu == '3':
            pass
        elif menu == '4':
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                res = i
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            # grade =Grade(name,kor,eng,math)
            # print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')
        elif menu == '5':
            res = f'{Quiz05Dice.cast()}'
        elif menu == '6':
            q6 = None
            res = f'{q6.ran()}'

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            res = f'{q7.choiceMember()}'
        elif menu == '8':
            q8 = Quiz08Rps(int(input('1.가위 2.바위 3.보')))
            res = f'User : {q8.rps[q8.user -1]} Com:{q8.com-1} 결과:{q8.battle()}'

        elif menu == '9':
            pass
        elif menu == '10':
            pass
        elif menu == '11':
            pass
        elif menu == '12':
            pass
        elif menu == '13':
            pass
        elif menu == '14':
            pass
        else:
            res = f'잘못된 선택입니다.'
        print(res)
