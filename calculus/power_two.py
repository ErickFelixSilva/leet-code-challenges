from math import log2

from utils import printarResultadoEsperado


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        result = log2(n)
        return result.is_integer()


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.isPowerOfTwo(n=1), True)
    printarResultadoEsperado(s.isPowerOfTwo(n=16), True)
    printarResultadoEsperado(s.isPowerOfTwo(n=3), False)
    printarResultadoEsperado(s.isPowerOfTwo(n=8), True)
    printarResultadoEsperado(s.isPowerOfTwo(n=0), True)
