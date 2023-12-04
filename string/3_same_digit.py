from utils import printarResultadoEsperado


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_number = ""
        good_number = ""
        for i in range(0, len(num)):
            if i == 0:
                good_number = num[i]
            elif num[i] == num[i-1]:
                good_number += num[i]
            else:
                good_number = num[i]
            if len(good_number) == 3:
                max_good_number = max(max_good_number, good_number)
        return max_good_number


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.largestGoodInteger(num="6777133339"), "777")
    printarResultadoEsperado(s.largestGoodInteger(num="2300019"), "000")
    printarResultadoEsperado(s.largestGoodInteger(num="42352338"), "")

