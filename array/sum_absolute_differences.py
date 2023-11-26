from typing import List

from utils import printarResultadoEsperado


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = sum(nums)
        suffix_sum = 0
        result = []
        for i in range(len(nums)-1, -1, -1):
            prefix_sum -= nums[i]
            sum_absolute_differences = (nums[i] * i - prefix_sum) + (suffix_sum - nums[i] * (len(nums) - i - 1))
            suffix_sum += nums[i]
            result.append(sum_absolute_differences)
        result.reverse()
        return result


if __name__ == '__main__':
    resultado = Solution().getSumAbsoluteDifferences(nums=[2, 3, 5])
    printarResultadoEsperado(resultado, [4, 3, 5])

    resultado = Solution().getSumAbsoluteDifferences(nums=[1,4,6,8,10])
    printarResultadoEsperado(resultado, [24, 15, 13, 15, 21])
