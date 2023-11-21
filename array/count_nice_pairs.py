from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def rev(self, num: int) -> int:
        str_num = str(num)[::-1]
        return int(str_num)

    def countNicePairs_beta(self, nums: List[int]) -> int:
        counter = set()
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[i] + self.rev(nums[j]) == nums[j] + self.rev(nums[i]) and 0 <= i < j < len(nums):
                    counter.add((i, j))
        return len(counter)

    def countNicePairs(self, nums: List[int]) -> int:
        differences: List[int] = list()
        for i in range(0, len(nums)):
            differences.append(nums[i]-self.rev(nums[i]))
        pairs_counter = 0
        for difference in set(differences):
            occurrence = differences.count(difference)
            pairs_counter += (occurrence * (occurrence - 1)) / 2
        return int(pairs_counter) % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()

    resultado = s.countNicePairs(nums=[42, 11, 1, 97])
    printarResultadoEsperado(resultado, 2)

    resultado = s.countNicePairs(nums=[13, 10, 35, 24, 76])
    printarResultadoEsperado(resultado, 4)
