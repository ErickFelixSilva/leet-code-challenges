from copy import copy
from math import prod, floor
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def getCellAverage(self, x: int, y: int, img: List[List[int]]):
        sum = img[x][y]
        values_counter = 1
        if x - 1 >= 0 and y - 1 >= 0:
            values_counter += 1
            sum += img[x - 1][y - 1]
        if x - 1 >= 0:
            values_counter += 1
            sum += img[x - 1][y]
        if x - 1 >= 0 and y + 1 < len(img[x]):
            values_counter += 1
            sum += img[x - 1][y + 1]
        if y - 1 >= 0:
            values_counter += 1
            sum += img[x][y - 1]
        if y + 1 < len(img[x]):
            values_counter += 1
            sum += img[x][y + 1]
        if x + 1 < len(img) and y - 1 >= 0:
            values_counter += 1
            sum += img[x + 1][y - 1]
        if x + 1 < len(img):
            values_counter += 1
            sum += img[x + 1][y]
        if x + 1 < len(img) and y + 1 < len(img[x]):
            values_counter += 1
            sum += img[x + 1][y + 1]
        return floor(sum / values_counter)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        for x in range(len(img)):
            result.append([])
            for y in range(len(img[x])):
                result[x].append(self.getCellAverage(x, y, img))
        return result


if __name__ == '__main__':
    s = Solution()

    resultado = s.imageSmoother(img=[[100, 200, 100], [200, 50, 200], [100, 200, 100]])
    printarResultadoEsperado(resultado, [[137, 141, 137], [141, 138, 141], [137, 141, 137]])

    resultado = s.imageSmoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    printarResultadoEsperado(resultado, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
