from collections import defaultdict
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result: List[bool] = []
        for i in range(0, len(l)):
            subarray = nums[l[i]:r[i] + 1]
            subarray.sort()

            difference = subarray[1] - subarray[0]
            arithmetic = True
            for i in range(1, len(subarray) - 1):
                if subarray[i + 1] - subarray[i] != difference:
                    arithmetic = False
            result.append(arithmetic)
        return result


if __name__ == '__main__':
    s = Solution()

    resultado = s.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5])
    printarResultadoEsperado(resultado, [True, False, True])

    resultado = s.checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                           l=[0, 1, 6, 4, 8, 7], r=[4, 4, 9, 7, 9, 10])
    printarResultadoEsperado(resultado, [False, True, False, False, True, True])
