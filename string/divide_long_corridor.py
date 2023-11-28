from functools import reduce
from typing import Tuple, List

from utils import printarResultadoEsperado


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        intersections_positions: List[Tuple[int, int]] = []
        total_seat_counter = 0
        seat_counter = 0
        empty_room_start = 0
        for i in range(len(corridor)):
            letter = corridor[i]
            if letter == 'S':
                seat_counter += 1
                total_seat_counter += 1
                if seat_counter == 1 and total_seat_counter > 1:
                    intersections_positions.append((empty_room_start, i))
                if seat_counter == 2:
                    empty_room_start = i
                    seat_counter = 0

        if total_seat_counter == 2:
            return 1
        if len(intersections_positions) < 1 or total_seat_counter % 2 != 0:
            return 0
        intersections_sizes = list(map(lambda intersection: intersection[1] - intersection[0], intersections_positions))
        return reduce((lambda x, y: x * y), intersections_sizes) % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()

    # printarResultadoEsperado(s.numberOfWays("SSPPSPS"), 3)
    # printarResultadoEsperado(s.numberOfWays("PPSPSP"), 1)
    # printarResultadoEsperado(s.numberOfWays("PPSPPSSSSSSSPSPS"), 2)
    # printarResultadoEsperado(s.numberOfWays("SPPPPPPPSPPPSPSSSPPPPPPPPPPPPPPPPPSPPPPPPPPPPPPPPPPSPPPPPSPSPPPPPPSPSPPSPSPPPSPSPPSSPPPPPSPPSSPP"), 0)
    printarResultadoEsperado(s.numberOfWays("PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"), 0)

