from utils import printarResultadoEsperado


class Solution:
    def totalMoney(self, n: int) -> int:
        week_start = 1
        week_amount = 1
        total_amount = 0
        for i in range(0, n):
            if i != 0 and i % 7 == 0:
                week_start += 1
                week_amount = week_start
            total_amount += week_amount
            week_amount += 1
        return total_amount


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.totalMoney(n=4), 10)
    printarResultadoEsperado(s.totalMoney(n=10), 37)

