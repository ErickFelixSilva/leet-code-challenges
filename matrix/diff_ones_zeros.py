from collections import defaultdict
from copy import copy
from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def counter(self) -> Dict[str, int]:
        return {'zeros': 0, 'ones': 0}

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = defaultdict(lambda: self.counter())
        cols = defaultdict(lambda: self.counter())
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num = grid[i][j]
                if num == 0:
                    rows[i]['zeros'] += 1
                    cols[j]['zeros'] += 1
                else:
                    rows[i]['ones'] += 1
                    cols[j]['ones'] += 1

        result: List[List[int]] = copy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result[i][j] = rows[i]['ones'] + cols[j]['ones'] - rows[i]['zeros'] - cols[j]['zeros']
        return result


if __name__ == '__main__':
    s = Solution()

    resultado = s.onesMinusZeros(grid = [[0,1,1],[1,0,1],[0,0,1]])
    printarResultadoEsperado(resultado, [[0,0,4],[0,0,4],[-2,-2,2]])
