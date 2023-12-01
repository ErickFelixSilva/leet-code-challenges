from functools import reduce
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return reduce((lambda x, y: x + y), word1) == reduce((lambda x, y: x + y), word2)


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]), False)

