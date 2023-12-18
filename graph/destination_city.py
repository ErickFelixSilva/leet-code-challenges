from collections import defaultdict
from typing import List

from utils import printarResultadoEsperado


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination = {}
        for path in paths:
            origin = path[0]
            destination[origin] = False
            dest = path[1]
            if dest not in destination:
                destination[dest] = True
            # if dest in destination and not destination[dest]:
            #     continue
            # elif dest not in destination:
            #     destination[dest] = True
        return list(filter(lambda d: destination[d] is True ,destination.keys()))[0]


if __name__ == '__main__':
    resultado = Solution().destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
    printarResultadoEsperado(resultado, "Sao Paulo")

    resultado = Solution().destCity(paths = [["B","C"],["B","Z"],["Z","A"],["D","B"],["C","A"]])
    printarResultadoEsperado(resultado, "A")
