from typing import List

from utils import printarResultadoEsperado


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x = points[0][0]
        y = points[0][1]
        time_counter = 0
        for i in range(1, len(points)):
            x_target = points[i][0]
            y_target = points[i][1]
            while x != x_target or y != y_target:
                time_counter += 1
                if x_target > x:
                    x += 1
                elif x_target < x:
                    x -= 1
                if y_target > y:
                    y += 1
                elif y_target < y:
                    y -= 1
        return time_counter


if __name__ == '__main__':
    s = Solution()

    resultado = s.minTimeToVisitAllPoints(points=[[1,1],[3,4],[-1,0]])
    printarResultadoEsperado(resultado, 7)

    resultado = s.minTimeToVisitAllPoints(points=[[3,2],[-2,2]])
    printarResultadoEsperado(resultado, 5)
