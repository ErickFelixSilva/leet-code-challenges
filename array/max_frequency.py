from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        start = 0
        max_freq = 1
        window_sum = nums[0]
        for end in range(1, len(nums)):
            window_sum += nums[end]
            total_increments = nums[end] * (end - start + 1) - window_sum

            while total_increments > k:
                window_sum -= nums[start]
                start += 1
                total_increments = nums[end] * (end - start + 1) - window_sum

            max_freq = max(max_freq, end - start + 1)
        return max_freq


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxFrequency(nums = [1,2,4], k = 5)
    printarResultadoEsperado(resultado, 3)

    resultado = s.maxFrequency(nums = [1,4,8,13], k = 5)
    printarResultadoEsperado(resultado, 2)

    resultado = s.maxFrequency(nums = [1,2,3,4], k = 3)
    printarResultadoEsperado(resultado, 3)


