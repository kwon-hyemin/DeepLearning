import pandas as pd
from six import b

from hello.domains import my100, myRandom
from icecream import ic

class Quiz30:
    def quiz30_df_4_by_3(self):
        df = pd.DataFrame([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9],
                          [10, 11, 12]], index=range(1,5), columns=['A','B','C']
                          )
        ic(df)
        return None

    def quiz31(self):
        a = 10
        b = 5
        print(a / b)

        return None

    def quiz32(self) -> str: return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
