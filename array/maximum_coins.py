from typing import List

from utils import printarResultadoEsperado


class Solution:
    def maxCoins_beta(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        coins_counter = 0
        while piles.__len__() > 0:
            piles.pop(0) # Alice
            coins_counter += piles.pop(0) # target
            piles.pop() # Bob
        return coins_counter

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        coins_counter = 0
        second_largest_pile = 1
        smallest_pile = len(piles)
        while smallest_pile - second_largest_pile > 1:
            coins_counter += piles[second_largest_pile] # target
            smallest_pile -= 1
            second_largest_pile += 2
        return coins_counter


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxCoins(piles=[2, 4, 1, 2, 7, 8])
    printarResultadoEsperado(resultado, 9)

    resultado = s.maxCoins(piles=[2, 4, 5])
    printarResultadoEsperado(resultado, 4)

    resultado = s.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4])
    printarResultadoEsperado(resultado, 18)
