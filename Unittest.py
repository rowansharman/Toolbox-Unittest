import unittest
from random import randint


def generateList(len):
    lis = []
    for i in range(len):
        lis.append(randint(-5, 5))
    return lis


def sortMyList(lis):
    lis.sort()
    lastNegative = 0
    for i in range(len(lis)):
        if lis[i] < 0:
            lastNegative = i
        else:
            break
    lis = lis[lastNegative+1:]
    return lis


class TestMyListSorter(unittest.TestCase):
    def test_working(self):
        self.assertEqual(sortMyList([1, -4, 1, -3, -3, 4, 0, 2, -2, 3, 1]), [0, 1, 1, 1, 2, 3, 4])


if __name__ == '__main__':
    # myList = generateList(10)
    # print(myList)
    # print(sortMyList(myList))
    unittest.main()
