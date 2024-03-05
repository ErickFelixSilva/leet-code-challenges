from typing import List, Optional

from utils import printarResultadoEsperado

# Challenge 03/03/2024
# https://leetcode.com/problems/bag-of-tokens/?envType=daily-question&envId=2024-03-04


class Solution:
    score: int = 0
    power: int = 0

    def tokenAvailable(self, tokens: List[int]) -> bool:
        return len(tokens) > 0 and tokens.__getitem__(0) <= self.power

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        self.score = 0
        self.power = power
        tokens.sort()

        while (len(tokens) > 1 and self.score > 0) or self.tokenAvailable(tokens):
            # Earn some score
            while self.tokenAvailable(tokens):
                self.playTokenFaceUp(tokens.__getitem__(0), tokens)

            if len(tokens) > 1 and self.score > 0:
                # Try to exchange score for power
                highest_token = tokens.__getitem__(len(tokens) - 1)
                self.playTokenFaceDown(highest_token, tokens)

        return self.score

    def playTokenFaceDown(self, token: int, tokens: List[int]):
        if self.score > 0:
            self.power += token
            tokens.remove(token)
            self.score -= 1

    def playTokenFaceUp(self, token: int, tokens: List[int]):
        self.power -= token
        tokens.remove(token)
        self.score += 1


if __name__ == '__main__':
    s = Solution()

    # printarResultadoEsperado(s.bagOfTokensScore(tokens=[100], power=50), 0)
    # printarResultadoEsperado(s.bagOfTokensScore(tokens=[200, 100], power=150), 1)
    printarResultadoEsperado(s.bagOfTokensScore(tokens=[26], power=51), 1)
    # printarResultadoEsperado(s.bagOfTokensScore(tokens=[100, 200, 300, 400, 700], power=400), 3)
