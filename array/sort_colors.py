from typing import List
from utils import printarResultadoEsperado


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        current_index = 0
        while current_index < len(nums):
            min_index = None
            for i in range(current_index, len(nums), 1):
                if min_index is None or nums[i] < nums[min_index]:
                    min_index = i
            nums[current_index], nums[min_index] = nums[min_index], nums[current_index]
            current_index += 1

    def sortColors_1(self, nums: List[int]) -> None:
        zero_counter = 0
        one_counter = 0
        two_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
            elif num == 1:
                one_counter += 1
            else:
                two_counter += 1
        for i in range(zero_counter):
            nums[i] = 0
        for i in range(zero_counter, zero_counter + one_counter):
            nums[i] = 1
        for i in range(zero_counter + one_counter, zero_counter + one_counter + two_counter):
            nums[i] = 2


if __name__ == '__main__':
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors_1(nums)
    printarResultadoEsperado(nums, [0, 0, 1, 1, 2, 2])
    print(s.sortColors_1([2,0,1]), " EXPECTED: " + str([0,1,2]))
