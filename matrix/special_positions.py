from collections import defaultdict
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        columns_count = defaultdict(int)
        special_rows = set()
        for i in range(len(mat)):
            one_counter = 0
            for j in range(len(mat[i])):
                num = mat[i][j]
                if num == 1:
                    one_counter += 1
                    one_index = j
                    columns_count[j] += 1
            if one_counter == 1:
                special_rows.add(one_index)
        special_columns = list(filter(lambda x: columns_count[x] == 1, columns_count))
        return len(list(set(special_columns) & special_rows))


if __name__ == '__main__':
    s = Solution()

    resultado = s.numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]])
    printarResultadoEsperado(resultado, 1)
    #
    resultado = s.numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    printarResultadoEsperado(resultado, 3)

    resultado = s.numSpecial(mat=[[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    printarResultadoEsperado(resultado, 2)

    resultado = s.numSpecial(
        mat=[[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0]])
    printarResultadoEsperado(resultado, 1)
