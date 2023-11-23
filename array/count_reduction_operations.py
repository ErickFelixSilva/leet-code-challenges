from typing import List

from utils import printarResultadoEsperado


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        if len(distinct) == 1:
            return 0
        distinct.sort()

        map_distinct = {}
        for i in range(0, len(distinct)):
            map_distinct[distinct[i]] = i
        smallest = distinct[0]
        counter = 0
        for num in nums:
            if num != smallest:
                counter += map_distinct[num]
        return counter


if __name__ == '__main__':
    s = Solution()

    resultado = s.reductionOperations(nums=[5, 1, 3])
    printarResultadoEsperado(resultado, 3)

    resultado = s.reductionOperations(nums=[1,1,2,2,3,5,6,8,8,10])
    printarResultadoEsperado(resultado, 27)


# 2 = 1 x 2 = 2
# 3 = 2
# 5 = 3
# 6 = 4
# 8 = 5 x 2 = 10
# 10 = 6