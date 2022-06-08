import pandas as pd

from context.domains import Reader, File


class Solution(Reader):
    def __init__(self, fname):
        self.file = File()
        # self.reader = Reader()

        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/'
        # self.file.fname = './crime_in_seoul.csv'
        self.file.fname = fname

    # seoul.csv
    def save_police_pos(self) -> object:
        return self.myprint(self.csv(self.file))

    # cctv in seoul
    def save_cctv_pos(self) -> object:
        return self.myprint(self.csv(self.file))

    def save_police_norm(self):
        pass

    def folium_test(self):
        pass

    # json
    def draw_crime_map(self) -> object:
        return self.myprint(self.json(self.file))


if __name__ == '__main__':
    Solution('crime_in_seoul.csv').save_police_pos(),
    Solution('cctv_in_seoul.csv').save_cctv_pos(),
    Solution('geo_simple.json').draw_crime_map(),
