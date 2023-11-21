from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def total_time(self, truck: Dict, travel: List[int]):
        travel_time = sum(travel[0:truck["maximum_house_visited"]]) if truck["maximum_house_visited"] > 0 else 0
        return truck["collection_time"] + travel_time

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metal_truck, paper_truck, glass_truck = ({"collection_time": 0, "maximum_house_visited": 0} for _ in range(3))
        for i in range(0, len(garbage)):
            house_garbage = garbage[i]
            if "M" in house_garbage:
                metal_truck["collection_time"] += house_garbage.count("M")
                metal_truck["maximum_house_visited"] = i
            if "P" in house_garbage:
                paper_truck["collection_time"] += house_garbage.count("P")
                paper_truck["maximum_house_visited"] = i
            if "G" in house_garbage:
                glass_truck["collection_time"] += house_garbage.count("G")
                glass_truck["maximum_house_visited"] = i
        return self.total_time(metal_truck, travel) + self.total_time(paper_truck, travel) + self.total_time(glass_truck, travel)


if __name__ == '__main__':
    s = Solution()

    resultado = s.garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3])
    printarResultadoEsperado(resultado, 21)
