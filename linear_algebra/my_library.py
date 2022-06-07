import numpy as np


def numerical_derivative(f, x):
    # f : 미분하려고 하는 다변수 함수; f(x,y) = 2x + 3xy + y^3
    # x : 모든 변수를 포함하고 있어야 함 (ndarray)

    delta_x = 1e-4
    # 미분한 결과를 저장하기 위한 ndarray
    derivative_x = np.zeros_like(x)

    # iterator를 이용해서 입력변수 x에 대해 편미분을 수행
    it = np.nditer(x, flags=['multi_index'])

    # x에 대해서 수치미분 계산하고 다음루프 때 y에 대해서 수치미분 계산
    while not it.finished:
        idx = it.multi_index  # iterator의 현재 index를 tuple로 추출
        # 현재 칸의 값을 어딘가에 잠시 저장
        tmp = x[idx]

        x[idx] = tmp + delta_x
        fx_plus_delta = f(x)  # f(x + delta_x, y) / f(x, y + delta_x)
        x[idx] = tmp - delta_x
        fx_minus_delta = f(x)  # f(x - delta_x, y) / f(x, y - delta_x)

        derivative_x[idx] = (fx_plus_delta - fx_minus_delta) / (2 * delta_x)
        # 데이터 원상복구
        x[idx] = tmp
        it.iternext()
    return derivative_x


# f(x,y) = 2x + 3xy + np.power(y,3)
def my_func(input_data):
    x = input_data[0]
    y = input_data[1]
    return 2 * x + 3 * x * y + np.power(y, 3)


result = numerical_derivative(my_func, np.array([1.0, 2.0]))
print('결과 : {}'.format(result))  # 결과 : [ 8.         15.00000001]