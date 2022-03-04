from random import random

from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self):
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        ran = myRandom(0, 4)

        if o[ran] == '+':
            print(self.add(a, b))
        elif o[ran] == '-':
            print(self.sub(a, b))
        elif o[ran] == '*':
            print(self.mul(a, b))
        elif o[ran] == '/':
            print(self.div(a, b))
        elif o[ran] == '%':
            print(self.mod(a, b))

        return None

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(self):
        name = members()
        ran = myRandom(0, 23)
        print(name[ran])
        height = myRandom(100, 200)
        weight = myRandom(30, 100)
        res = weight / (height * height) * 10000

        if res > 25:
            print(f'비만{res}')
        elif res > 23:
            print(f'과체중{res}')
        elif res > 18.5:
            print(f'정상{res}')
        else:
            print(f'저체중{res}')

    def quiz02dice(self):
        return myRandom(1, 6)

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = input('가위', '바위', '보')
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == '3':
                res = f'플레이어: {rps[0]} , 컴퓨터: {rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = '승리'
            elif c == 2:
                res = '무승부'
            elif c == 3:
                res = '패배'
        elif p == 3:
            if c == 1:
                res = '패배'
            elif c == 2:
                res = '승리'
            elif c == 3:
                res = '무승부'
        else:
            res = '1~3 입력'
        print(res)
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        pass

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.agv(kor, eng, math)
        grade = self.getGrade()
        passChk = self.passChk()
        return [sum, avg, grade, passChk]

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.kor + self.eng + self.math / 3

    def grade(self):
        pass

    def passChk(self):  # 60점이상이면 합격
        pass

    def quiz06memberChoice(self):

        return members[myRandom(0, 23)]

    def quiz07lotto(self):

        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass
