from utils import printarResultadoEsperado


class Solution:
    possible_moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }

    number_possibilities = {
        0: [1],
        1: [1],
        2: [1],
        3: [1],
        4: [1],
        5: [1],
        6: [1],
        7: [1],
        8: [1],
        9: [1],
    }

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return sum([self.number_possibilities[x][0] for x in self.number_possibilities])

        for i in range(len(self.number_possibilities[0]), n):
            for number in self.possible_moves:
                counter = 0
                for possible_move in self.possible_moves[number]:
                    counter += self.number_possibilities[possible_move][i-1]
                self.number_possibilities[number].append(counter)
        distinct_possibilities_counter = sum([self.number_possibilities[x][n-1] for x in self.number_possibilities])
        return distinct_possibilities_counter % (10**9 + 7)


if __name__ == '__main__':
    s = Solution()

    resultado = s.knightDialer(n=1)
    printarResultadoEsperado(resultado, 10)

    resultado = s.knightDialer(n=2)
    printarResultadoEsperado(resultado, 20)

    resultado = s.knightDialer(n=3)
    printarResultadoEsperado(resultado, 46)

    resultado = s.knightDialer(n=4)
    printarResultadoEsperado(resultado, 104)
