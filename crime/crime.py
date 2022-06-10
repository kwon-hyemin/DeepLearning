import pandas as pd
import googlemaps
import folium

from context.domains import Reader, File


class Solution(Reader):
    def __init__(self):
        self.file = File()
        # self.reader = Reader()

        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.file.context = './data/'
        # self.file.fname = './crime_in_seoul.csv'

    # crime in seoul.csv
    def save_police_pos(self):
        file = self.file
        file.fname = 'crime_in_seoul.csv'
        crime = self.csv(file)
        station_names = []
        for name in crime['관서명']:
            station_names.append(f'서울{str(name[:-1])}경찰서')
        # print(f'station_names range: {len(station_names)}')
        ''' 서울시내 경찰서는 31개이다. '''
        # print([{i:name} for i, name in enumerate(station_names) ])
        '''
        [{0: '서울중부경찰서'}, {1: '서울종로경찰서'}, {2: '서울남대문경찰서'}, ... , {21: '서울종암경찰서'}
        '''
        gmaps = self.gmaps()

        '''
        a = gmaps.geocode('서울중부경찰서', language='ko')
        print(a)
        [{'address_components': 
            [{'long_name': '２７', 'short_name': '２７', 'types': ['premise']}, 
            {'long_name': '수표로', 'short_name': '수표로', 'types': ['political', 'sublocality', 'sublocality_level_4']}, 
            {'long_name': '중구', 'short_name': '중구', 'types': ['political', 'sublocality', 'sublocality_level_1']}, 
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']}, 
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']}, 
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}], 
            'formatted_address': '대한민국 서울특별시 중구 수표로 27', 
            'geometry': {'location': 
                {'lat': 37.56361709999999, 'lng': 126.9896517}, 
                'location_type': 'ROOFTOP', 
                'viewport': {'northeast': {'lat': 37.5649660802915, 'lng': 126.9910006802915}, 
                'southwest': {'lat': 37.5622681197085, 'lng': 126.9883027197085}}}, 
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc', 
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시', 'global_code': '8Q98HX7Q+CV'}, 
                'types': ['establishment', 'point_of_interest', 'police']}]
        서울종암경찰서는 2021.12.20부터 이전함
        '''

        station_addrs = []
        station_lats = []
        station_lngs = []

        for i, name in enumerate(station_names) :
            if name != '서울종암경찰서':
                temp = gmaps.geocode(name, language='ko')
            else:
                temp = [{'address_components':
            [{'long_name': '32', 'short_name': '32', 'types': ['premise']},
            {'long_name': '화랑로7길', 'short_name': '화랑로7길', 'types': ['political', 'sublocality', 'sublocality_level_4']},
            {'long_name': '성북구', 'short_name': '성북구', 'types': ['political', 'sublocality', 'sublocality_level_1']},
            {'long_name': '서울특별시', 'short_name': '서울특별시', 'types': ['administrative_area_level_1', 'political']},
            {'long_name': '대한민국', 'short_name': 'KR', 'types': ['country', 'political']},
            {'long_name': '100-032', 'short_name': '100-032', 'types': ['postal_code']}],
            'formatted_address': '대한민국 서울특별시 성북구 화랑로7길 32',
            'geometry': {'location':
                {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'location_type': 'ROOFTOP',
                'viewport': {'northeast': {'lat': 37.60388169879458, 'lng': 127.04001571848704},
                'southwest': {'lat': 37.60388169879458, 'lng': 127.04001571848704}}},
                'partial_match': True, 'place_id': 'ChIJc-9q5uSifDURLhQmr5wkXmc',
                'plus_code': {'compound_code': 'HX7Q+CV 대한민국 서울특별시', 'global_code': '8Q98HX7Q+CV'},
                'types': ['establishment', 'point_of_interest', 'police']}]

            # station_addrs.append(temp[0].get('formatted_address'))
            # t_loc = temp[0].get('geometry')
            # station_lats.append(t_loc['location']['lat'])
            # station_lats.append(t_loc['location']['lng'])
            print(f'name {i} = {temp[0].get("formatted_address")}')


    # cctv in seoul
    def save_cctv_pos(self):
        # file = self.file
        # file.fname = 'cctv_in_seoul.csv'
        # cctv = self.csv(file)
        file = self.file
        file.fname = 'pop_in_seoul'
        pop = self.xls(self.file, skiprows=[0, 2], cols="B, D, G, J, N")

        print(pop)

    def save_police_norm(self):
        pass

    def folium_test(self):
        self.file.fname = 'us_unemployment.csv'
        us = self.csv(self.file)
        self.file.fname = 'us-states'
        state = self.json(self.file)
        print(us, state)

        # m = folium.Map(location=[45.5236, -122.6750])
        # m.save("./save/folium_test.html")

    # json
    def draw_crime_map(self):
        file = self.file
        file.fname = 'geo_simple'
        crime = self.csv(file)
        station_names = []


if __name__ == '__main__':
    # Solution().save_police_pos(),
    # Solution().save_cctv_pos(),
    # Solution().draw_crime_map(),
    Solution().folium_test(),
