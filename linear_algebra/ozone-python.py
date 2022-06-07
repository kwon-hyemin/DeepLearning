from matplotlib import rc, font_manager
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from my_library import numerical_derivative
# 미분함수를 다른 파일에 갖다 두고 사용

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())


class Solution:
    def __init__(self):
        self.df = pd.read_csv('./data/ozone.csv')

        # 2. Data Preprocessing(데이터 전처리)
        # 필요한 column(Temp, Ozone)만 추출
        self.training_data = self.df[['temp', 'ozone']]

        # 결측치 제거 - dropna() 함수 이용
        self.training_data = self.training_data.dropna(how='any')

        # 3. Training Data Set
        self.x_data = self.training_data['temp'].values.reshape(-1, 1)
        self.t_data = self.training_data['ozone'].values.reshape(-1, 1)

        # 4. Simple Linear Regression 정의
        self.W = np.random.rand(1, 1)
        self.b = np.random.rand(1)

        # 7. 프로그램에서 필요한 변수들 정의
        self.learning_rate = 1e-5
        self.f = lambda x: self.loss_func(self.x_data, self.t_data)

    # 5. loss function 정의
    def loss_func(self, x, t):
        y = np.dot(x, self.W) + self.b
        return np.mean(np.power((t - y), 2))  # 최소제곱법

    # 6. 학습종료 후 예측값 계산 함수
    def predict(self, x):
        return np.dot(x, self.W) + self.b

    def solution(self):
        # 8. 학습 진행
        for step in range(90000):
            self.W -= self.learning_rate * numerical_derivative(self.f, self.W)
            self.b -= self.learning_rate * numerical_derivative(self.f, self.b)

            if step % 9000 == 0:
                print('W : {}, b : {}, loss : {}'.format(self.W, self.b, self.loss_func(self.x_data, self.t_data)))

        # 9. 예측
        result = self.predict(62)
        print(result)  # [[34.56270003]]

        # 10. 그래프로 확인
        plt.scatter(self.x_data, self.t_data)
        plt.plot(self.x_data, np.dot(self.x_data, self.W) + self.b, color='r')
        plt.show()


if __name__ == '__main__':
    Solution().solution()
