# from selenium import webdriver
#
# driver = webdriver.Chrome(r"C:/Users/bitcamp/djangoproject/nlp/data/chromedriver.exe")
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

from icecream import ic

from context.domains import File, Reader

'''
예제 출처
https://prlabhotelshoe.tistory.com/19?category=1003351
'''


class Solution(Reader):
    def __init__(self):
        self.file = File()
        self.file.context = './data/'
        self.names = ['title', 'score', 'comment', 'label']
        self.movie_comments = pd.DataFrame()

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 텍스트 마이닝 ')  # 데이터를 읽어오면 다 전처리  1.크롤링 2.text로 읽는것
            print('2. DF로 정형화.')
            print('3. 토큰화.')
            print('4. 임베딩')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.crawling()
            elif menu == '2':
                self.preprocess()
            elif menu == '3':
                self.tokenization()
            elif menu == '4':
                self.embedding()
            elif menu == '5':
                self.preprocess()
            elif menu == '0':
                break

    def preprocess(self):
        self.stereotype()
        ic(self.movie_comments.head(5))
        ic(self.movie_comments)

    def crawling(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        f = open(path, 'w', encoding='UTF-8')
        # -- 500페이지까지 크롤링
        for no in range(1, 501):
            url = 'https://movie.naver.com/movie/point/af/list.naver?&page=%d' % no
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')

            reviews = soup.select('tbody > tr > td.title')
            for rev in reviews:
                title = rev.select_one('a.movie').text.strip()
                score = rev.select_one('div.list_netizen_score > em').text.strip()
                comment = rev.select_one('br').next_sibling.strip()

                # -- 긍정/부정 리뷰 레이블 설정
                if int(score) >= 8:
                    label = 1  # -- 긍정 리뷰 (8~10점)
                elif int(score) <= 4:
                    label = 0  # -- 부정 리뷰 (0~4점)
                else:
                    label = 2

                f.write(f'{title}\t{score}\t{comment}\t{label}\n')
        f.close()

    def stereotype(self):
        file = self.file
        file.fname = 'movie_reviews.txt'
        path = self.new_file(file)
        self.movie_comments = pd.read_csv(path, delimiter='\t', names=['title', 'score', 'comment', 'label'])

    def review_count(self):
        pass

    def tokenization(self):
        pass

    def embedding(self):
        pass


if __name__ == '__main__':
    Solution().hook()
