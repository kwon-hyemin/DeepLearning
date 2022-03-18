import pandas as pd
from six import b

from hello import Quiz00
from hello.domains import my100, myRandom
from icecream import ic


class Quiz30:
    def quiz30_df_range(self):
        df = pd.DataFrame([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],
                           [10, 11, 12]], index=range(1, 5), columns=['A', 'B', 'C']
                          )
        ic(df)
        return None

    def quiz31_rand_2_by_3(self):
        a = 10
        b = 5
        print(a / b)

        return None

    def quiz32_df_grade(self) -> dict | None:
        q = Quiz00()
        c = set([q.quiz06member_choice() for i in range(5)])
        le = len(c)
        print(f'set size : {le}')
        while le != 5:
            c.add(q.quiz06member_choice())
        students = list(c)
        scores = [myRandom(0, 100) for i in range(5)]
        print({i: j for i, j in zip(students, scores)})
        abc = []
        for i in range(5):
            abc.append(Quiz00().quiz06member_choice())
        print(abc)









    def quiz33_df_loc(self) -> str: return None

    def quiz34_df_iloc(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str:
        type(range(3))
        return None

    def quiz39(self) -> str: return None
