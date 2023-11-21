from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        index_1 = 0
        index_2 = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            number_1 = nums[index_1]**2
            number_2 = nums[index_2]**2
            if number_1 > number_2:
                result[i] = number_1
                index_1 += 1
            else:
                result[i] = number_2
                index_2 -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]), " EXPECTED: " + str([0,1,9,16,100]))
