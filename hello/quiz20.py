import random
import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup


def myRandom(start, end):
    return random.randint(start, end)


class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        return None

    def quiz23listcom(self) -> str:
        print('----------- legacy ------------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('----------- comprehension ------------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self):
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        return None
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

    def quiz28(self) -> str:
        return None

    def quiz29(self) -> str:
        return None
