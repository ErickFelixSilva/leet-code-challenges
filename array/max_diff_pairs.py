from math import prod
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        minor_pair = nums[0:2]
        biggest_pair = nums[len(nums)-2:len(nums)]
        return prod(biggest_pair) - prod(minor_pair)


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxProductDifference(nums=[5, 6, 2, 7, 4])
    printarResultadoEsperado(resultado, 34)
