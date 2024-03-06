from utils import printarResultadoEsperado

# 04/03/2024
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05


class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = -1

        while s != "" and len(s) > 1 and s[start] == s[end]:
            s = self.removePrefix(s, start)
            if s:
                s = self.removeSuffix(s, end)
        return len(s)

    def removePrefix(self, s: str, index: int):
        max_index = index
        while max_index < len(s)-1 and s[index] == s[max_index+1]:
            max_index += 1
        return s[max_index+1:len(s)]

    def removeSuffix(self, s: str, index: int):
        min_index = index
        while s[index] == s[min_index-1]:
            min_index -= 1
        return s[0:min_index]


if __name__ == '__main__':
    sol = Solution()
    # printarResultadoEsperado(sol.minimumLength("cabaabac"), 0)
    # printarResultadoEsperado(sol.minimumLength("aabccabba"), 3)
    printarResultadoEsperado(sol.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"), 1)

