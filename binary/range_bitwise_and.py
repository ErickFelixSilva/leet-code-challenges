from utils import printarResultadoEsperado


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.rangeBitwiseAnd(5, 7), 4)
    printarResultadoEsperado(s.rangeBitwiseAnd(0, 0), 0)
    printarResultadoEsperado(s.rangeBitwiseAnd(1, 2147483647), 0)
    printarResultadoEsperado(s.rangeBitwiseAnd(600000000, 2147483645), 0)
