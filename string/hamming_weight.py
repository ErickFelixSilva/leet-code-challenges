from utils import printarResultadoEsperado


class Solution:
    def hammingWeight(self, n: int) -> int:
        return format(n, 'b').count('1')


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.hammingWeight(0o0000000000000000000000000001011), 3)

