from six import b

from hello.domains import my100, myRandom


class Quiz30:
    def quiz30(self):
        list1 = [1, 2, 3, 4]
        list2 = ['math', 'english']
        list3 = [1, '2', [1, 2, 3]]
        list4 = [1, 2, 3]
        list5 = [4, 5]
        a = [1, 2]
        b = [0, 5]
        c = [a, b]

        print(list1, type(list1))

        print(list1[0], list1[-1], list1[-2], list1[1:3])

        print(list2[0], list2[0][1])

        print(list3)

        print(list4 + list5)

        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)
        print(sum(a))
        b = [2, 10, 0, -2]
        sorted(b)

        b.index(0)
        len(b)
        print(b.index(0), len(b))
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
