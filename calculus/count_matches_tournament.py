from utils import printarResultadoEsperado


class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams = n
        matches = 0
        while teams > 1:
            if teams % 2 == 0:
                matches += teams/2
                teams = teams/2
            else:
                matches += (teams - 1) / 2
                teams = (teams - 1) / 2 + 1
        return int(matches)

if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.numberOfMatches(n=7), 6)
    printarResultadoEsperado(s.numberOfMatches(n=14), 13)

