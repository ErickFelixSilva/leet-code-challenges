from typing import List

from utils import printarResultadoEsperado


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        possible_judge = {}
        trusts_somebody = set()
        for t in trust:
            if t[0] not in trusts_somebody:
                trusts_somebody.add(t[0])
                if t[0] in possible_judge:
                    del possible_judge[t[0]]

            t1_trusts_nobody = t[1] not in trusts_somebody
            if t[1] not in possible_judge and t1_trusts_nobody:
                trusts_required = n - 2
                possible_judge[t[1]] = trusts_required
            elif t[1] in possible_judge and t1_trusts_nobody:
                possible_judge[t[1]] -= 1

        for key in possible_judge.keys():
            if possible_judge[key] == 0:
                return key
        return -1


if __name__ == '__main__':
    s = Solution()

    resultado = s.findJudge(n=3, trust=[[1, 3], [2, 3]])
    printarResultadoEsperado(resultado, 3)
    printarResultadoEsperado(s.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]), -1)
    printarResultadoEsperado(s.findJudge(n=2, trust=[[1, 2]]), 2)
    printarResultadoEsperado(s.findJudge(n=3, trust=[[1,2],[2,3]]), -1)
