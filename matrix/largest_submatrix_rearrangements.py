from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        num_cols = len(matrix[0])

        for col in range(num_cols):
            one_counter = 0
            for row in range(len(matrix)):
                if matrix[row][col] == 1:
                    one_counter += 1
                    matrix[row][col] = one_counter
                elif matrix[row][col] == 0:
                    one_counter = 0

        maximum_matrix_area = 0
        for row in matrix:
            row.sort(reverse=True)
            print(row)
            maximum_row_area = 0
            for col in range(len(row)):
                maximum_row_area = max(maximum_row_area, row[col] * (col+1))
            maximum_matrix_area = max(maximum_matrix_area, maximum_row_area)
        return maximum_matrix_area


if __name__ == '__main__':
    s = Solution()

    resultado = s.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]])
    printarResultadoEsperado(resultado, 4)

    resultado = s.largestSubmatrix([[1,1,0],[1,0,1]])
    printarResultadoEsperado(resultado, 2)

    resultado = s.largestSubmatrix([[1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0]])
Gue
