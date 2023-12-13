from typing import Optional

from utils import printarResultadoEsperado


class Solution:
    def largestOddNumber(self, num: str) -> str:
        furtest_odd: Optional[int] = None
        for i in range(len(num)-1, -1, -1):
            number = int(num[i])
            if number % 2 != 0:
                furtest_odd = i
                break
        return "" if furtest_odd is None else num[0:furtest_odd+1]


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.largestOddNumber(num="52"), "5")
    printarResultadoEsperado(s.largestOddNumber(num="4206"), "")
    printarResultadoEsperado(s.largestOddNumber(num="35427"), "35427")

