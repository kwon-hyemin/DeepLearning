import random
import urllib.request
from turtle import title
from urllib.request import urlopen

from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd

from hello import Quiz00
from hello.domains import myMember


def myRandom(start, end):
    return random.randint(start, end)


class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        return None

    def quiz23listcom(self) -> None:
        print('----------- legacy ------------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('----------- comprehension ------------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser
        # artists = soup.find_all('p', {'class': 'artist'})
        # artists = [i.get_text() for i in artists]
        # abc = soup.find_all('p', {'class': 'title'})
        # abc = [i.get_text() for i in abc]
        # print(''.join(i for i in abc))
        # b = [i for i in self.zip24(soup, i)]
        # for i, j in enumerate(['artist', 'title']):
        #     print('\n\n\n'.join(i for i in [i for i in self.zip24(soup, j)]))
        # print('*' * 100)
        # self.zip24(soup, 'title')
        ls1 = self.find_music(soup, "title")
        ls2 = self.find_music(soup, 'artist')
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        # self.dict1(ls1, ls2)
        dt = {i: j for i, j in zip(ls1, ls2)}
        # for i, j in enumerate(ls1):
        #     dict[j] = ls2[i]
        # print(dict)
        # self.dict2(ls1, ls2)
        # for i, j in zip(ls1, ls2):
        #     dict[i] = j
        #     print(dict)
        # return dict
        print(d1)
        return d1

    def print_music_list(self, soup):
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        # print(''.join(i for i in abc))
        return [i.get_text() for i in ls]

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            # print(type(f'타입: {ls1[i]}'))
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2):
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[j] = ls2[i]
        return dict

        # print(type(artists))
        # soup.find_all("url", class_="워너비")
        # soup.find_all(artists=soup.find_all({'class': 'email'}))
        # songs = soup.select('tr th p a')[0].text
        # titles = soup.select('tr th p a')

        # song_title = []
        # for song in songs:
        #     title = song.text
        #     song_title.append(title)
        # print(soup.a)

        # print(soup.prettify())

    def quiz25dictcom(self):
        # for i in range(5):
        #     abc.append( Quiz00().quiz06memberChoice())
        # print(abc)
        # for i, j in enumerate(ls1):
        #     dict[j] = ls2[i]
        # for i, j in enumerate(code2):
        #     dict3[j] = code2[i]
        # list(set(Quiz00().quiz06member_choice()))
        # scores_students = list()
        # scores_students = [i+j for i, j in zip(scores,students)]
        # scores = [myRandom(0, 100) for i in range(5)]
        # students = [Quiz00().quiz06member_choice() for i in range(5)]
        # d1 = dict(zip(students, scores))
        # return print(d1)
        # scores = [i for i in [myRandom(0, 100)]]
        # print(students, scores)
        # dt = {i: j for i, j in zip(ls1, ls2)}
        # # q = Quiz00()
        # # c = set([q.quiz06member_choice() for i in range(5)])
        # # # le = len(c)
        # print(f'set size : {len(c)}')
        # while len(c) != 5:
        #     c.add(q.quiz06member_choice())
        # students = list(c)
        # scores = [myRandom(0, 100) for i in range(5)]
        # # d1 = {i: j for i, j in zip(students, scores)}
        # # dict(zip(students, scores))
        # return {i: j for i, j in zip(students, scores)}
        pass

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self):
        headers = {
            'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')  # html.parser

        # ls = soup.find_all('div', {'class': 'ellipsis rank01'})
        # print(''.join([i.get_text() for i in ls]))
        self.music_find(soup, 'ellipsis rank01')

    @staticmethod
    def music_find(soup, a):
        ls = soup.find_all('div', {'class': a})
        print(''.join([i.get_text() for i in ls]))

    def quiz28dataframe(self) -> str:
        # dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')
        return None

    '''
    다음 결과 출력 
        a    b    c
    1   1    3    5
    2   2    4    6
    '''

    def quiz29_pandas_df(self) -> object:
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        d2 = {'1': [1, 3, 5], '2': [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        # c = ['a', 'b', 'c']
        column = [chr(i) for i in range(97, 100)]

        d3 = {'1': [1, 3, 5]}
        d4 = {'2': [2, 4, 6]}
        # df3 = pd.DataFrame.from_dict(d2, orient='index', columns=c)
        abc = []
        efd = []

        e = [abc.append(i) if i % 2 == 0 else efd.append(i) for i in range(1, 7)]  # 홀수 짝수 집어넣기
        d5 = ['1', '2']
        d6 = [abc, efd]
        e2 = {i: j for i, j in zip(d5, d6)}
        ef2 = pd.DataFrame.from_dict(e2, orient='index', columns=column)
        print(ef2)



        return None
