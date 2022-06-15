from context.domains import Reader, File
import pandas as pd
import numpy as np

import platform
import matplotlib.pyplot as plt

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
import openpyxl


class Solution(Reader):

    def __init__(self):
        self.file = File()
        self.file.context = './data/'

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. draw_korea')
            print('2. draw_korea_raw.')
            print('3. election_result')
            print('4. population_raw_data')
            print('5. pop_municipalities_geo_simple.')
            print('6. 2018년 삼성사업계획서를 분석해서 워드클라우드를 작성하시오.')
            print('9. nltk 다운로드')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.draw_korea()
            elif menu == '2':
                self.draw_korea_raw()
            elif menu == '3':
                self.election_result()
            elif menu == '4':
                self.population_raw_data()
            elif menu == '5':
                self.pop_municipalities_geo_simple()
            elif menu == '6':
                self.document_embedding()
            elif menu == '7':
                self.document_embedding()
            elif menu == '0':
                break




if __name__ == '__main__':
    Solution().hook()
