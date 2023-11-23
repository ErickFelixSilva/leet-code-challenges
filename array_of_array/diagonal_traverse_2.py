from collections import defaultdict
from typing import List

from utils import printarResultadoEsperado


class Solution:
    vertical_size: int = 0
    horizontal_size: int = 0
    result: List[int] = []

    def appendNumber(self, x: int, y:int, nums: List[List[int]], result: List[int]):
        if len(nums[x]) > y:
            result.append(nums[x][y])

    def mountDiagonalPositions_beta(self, diagonal_index: int, nums: List[List[int]]):
        # vertical traverse
        if diagonal_index < self.vertical_size:
            position = 0
            for i in range(diagonal_index, -1, -1):
                self.appendNumber(i, position, nums)
                position += 1
        # horizontal
        else:
            position = diagonal_index - (self.vertical_size - 1)
            list_number = self.vertical_size-1
            while position < self.horizontal_size and list_number >= 0:
                self.appendNumber(list_number, position, nums)
                list_number -= 1
                position += 1

    def findDiagonalOrder_beta_2(self, nums: List[List[int]]) -> List[int]:
        vertical_size = len(nums)
        horizontal_size = max(len(x) for x in nums)
        result: List[int] = []

        diagonals_count: int = (vertical_size - 1) + horizontal_size
        for i in range(0, diagonals_count):
            list_position = 0 if i < vertical_size - 1 else i - (vertical_size - 1)
            list_number = i if i < vertical_size - 1 else vertical_size - 1

            # calculate diagonal path
            while list_number >= 0 and list_position < horizontal_size:
                if len(nums[list_number]) > list_position:
                    result.append(nums[list_number][list_position])
                list_number -= 1
                list_position += 1
        return result

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_dict = defaultdict(list)
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                diagonal_dict[i + j].append(num)

        result = []
        for k in diagonal_dict.keys():
            if len(diagonal_dict[k]) > 1:  # reverse even diagonals
                result.extend(diagonal_dict[k][::-1])
            else:
                result.extend(diagonal_dict[k])
        return result


if __name__ == '__main__':
    s = Solution()

    resultado = s.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    printarResultadoEsperado(resultado, [1, 4, 2, 7, 5, 3, 8, 6, 9])

    resultado = s.findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]])
    printarResultadoEsperado(resultado, [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16])

    resultado = s.findDiagonalOrder(nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]])
    printarResultadoEsperado(resultado, [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11])

    resultado = s.findDiagonalOrder(nums=[[1,2,3,4,5,6]])
    printarResultadoEsperado(resultado, [1, 2, 3, 4, 5, 6])