from math import prod
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        horizontal_points = []
        for point in points:
            horizontal_points.append(point[0])
        horizontal_points.sort()
        maximum_diff = 0
        for i in range(len(horizontal_points)-1):
            maximum_diff = max(maximum_diff, horizontal_points[i+1] - horizontal_points[i])
        return maximum_diff


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxWidthOfVerticalArea(points=[[8,7],[9,9],[7,4],[9,7]])
    printarResultadoEsperado(resultado, 1)

    resultado = s.maxWidthOfVerticalArea(points=[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
    printarResultadoEsperado(resultado, 3)

