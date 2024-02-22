from typing import List

from utils import printarResultadoEsperado


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        previous_number: int = None
        if nums[0] != 0:
            return 0
        for num in nums:
            if previous_number is not None and num - previous_number > 1:
                return num - 1
            previous_number = num
        return len(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        soma = 0
        for i in range(0, len(nums)+1):
            soma += i
        return soma - sum(nums)


if __name__ == '__main__':
    s = Solution()

    resultado = s.missingNumber2(nums=[3, 0, 1])
    printarResultadoEsperado(resultado, 2)

    resultado = s.missingNumber(nums=[0, 1])
    printarResultadoEsperado(resultado, 2)
    printarResultadoEsperado(s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
