import random
import urllib.request
from turtle import title
from urllib.request import urlopen

from bs4 import BeautifulSoup
import pandas as pd


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
        # self.dict1(ls1, ls2)
        dict = {}
        # for i, j in enumerate(ls1):
        #     dict[j] = ls2[i]
        # print(dict)
        # self.dict2(ls1, ls2)
        for i, j in zip(ls1, ls2):
            dict[i] = j
            print(dict)
        return dict

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

    def quiz25dictcom(self) -> str:
        return None

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')  # html.parser

        return None

    def quiz28dataframe(self) -> str:
        # dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')
        return None

    def quiz29(self) -> str:
        return None
