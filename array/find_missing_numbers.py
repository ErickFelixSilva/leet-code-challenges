from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # for num in nums:
        #     index = abs(num) - 1  # abs is used to handle numbers already marked as negative
        #     nums[index] = -abs(nums[index])  # Ma
        # return nums
        desired_array = range(1, len(nums), 1)
        nums.sort()
        return list(set(desired_array) - set(nums))
        # disappeared_numbers = []
        # expected_number = 1
        # while expected_number != len(nums)-1:
        #     if expected_number in nums:
        #         expected_number += 1
        #     else:
        #         disappeared_numbers.append(expected_number)
        #         expected_number += 1
        # return disappeared_numbers


if __name__ == '__main__':
    s = Solution()
    # print(s.thirdMax([1,2,3]), " EXPECTED: " + str(1))
    # [1,2,3,4,7,8]
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]), " EXPECTED: " + str([5,6]))
    print(s.findDisappearedNumbers([1,1]), " EXPECTED: " + str([5,6]))
