from functools import reduce
from typing import List, Dict

from utils import printarResultadoEsperado


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_words_sum = 0
        for word in words:
            chars_copy = str(chars)
            good_word = True
            for letter in word:
                if letter in chars_copy:
                    chars_copy = chars_copy.replace(letter, '', 1)
                elif letter not in chars_copy:
                    good_word = False
                    break
            if good_word:
                good_words_sum += len(word)
        return good_words_sum


if __name__ == '__main__':
    s = Solution()

    printarResultadoEsperado(s.countCharacters(["hello","world","leetcode"], "welldonehoneyr"), 10)

