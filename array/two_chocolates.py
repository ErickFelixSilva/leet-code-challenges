from math import prod
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        two_price = prices[0] + prices[1]
        return money - two_price if money - two_price >= 0 else money


if __name__ == '__main__':
    s = Solution()

    resultado = s.buyChoco(money=3, prices=[1, 2, 2])
    printarResultadoEsperado(resultado, 0)

    resultado = s.buyChoco(money=3, prices=[3, 2, 3])
    printarResultadoEsperado(resultado, 3)
