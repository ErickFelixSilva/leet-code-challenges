from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_data: Dict = {"holding": 0 - prices[0], "not_holding": 0}
        for i in range(1, len(prices)):
            profit_data[i] = {}
            previous_holding = profit_data[i-1]["holding"]
            previous_not_holding = profit_data[i-1]["not_holding"]

            buying_profit = previous_not_holding - prices[i]
            holding = buying_profit if buying_profit > previous_holding else previous_holding

            selling_profit = previous_holding + prices[i] - fee
            not_holding = previous_not_holding if previous_not_holding > selling_profit else selling_profit

            profit_data[i] = {"holding": holding, "not_holding": not_holding}
        return profit_data[len(prices) - 1]["not_holding"]


if __name__ == '__main__':
    s = Solution()

    resultado = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    printarResultadoEsperado(resultado, 8)
