from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        difference_counter: List[int] = []
        for i in range(len(nums)-1, -1, -1):
            j = i-1
            frequency_counter = 1
            operations = k
            while j >= 0 and operations > 0:
                operations -= (nums[i] - nums[j])
                if operations >= 0:
                    frequency_counter += 1
                j -= 1
            difference_counter.append(frequency_counter)
        return max(difference_counter)


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxFrequency(nums = [1,2,4], k = 5)
    printarResultadoEsperado(resultado, 3)

    resultado = s.maxFrequency(nums = [1,4,8,13], k = 5)
    printarResultadoEsperado(resultado, 2)

    resultado = s.maxFrequency(nums = [1,2,3,4], k = 3)
    printarResultadoEsperado(resultado, 3)


