from utils import printarResultadoEsperado


class Solution:
    one_bits_positions = []
    number_operations_needed = {0: 1, 2: 3, 4: 7, 8: 15, 16: 31, 32: 63, 64: 127, 128: 255, 256: 511}

    def printBits(self, n: int) -> str:
        return str(bin(n)).replace('0b', '')

    def update_one_bits_positions(self, updated_number: int, index: int):
        if (updated_number >> index) & 1 == 1:
            self.one_bits_positions.append(index)
            self.one_bits_positions.sort()
        elif index in self.one_bits_positions:
            self.one_bits_positions.remove(index)

    def first_operation(self, n: int) -> int:
        updated_number = n ^ (1 << 0)
        self.update_one_bits_positions(updated_number, 0)
        #print(f"{self.printBits(updated_number)} - FIRST OPERATION - {list(self.one_bits_positions)} ")
        return updated_number

    def second_operation(self, n: int) -> int:
        updated_index = self.one_bits_positions[0] + 1
        updated_number = n ^ (1 << updated_index)
        self.update_one_bits_positions(updated_number, updated_index)
        #print(f"{self.printBits(updated_number)} - SECOND OPERATION - {list(self.one_bits_positions)} ")
        return updated_number

    def should_begin_with_second(self, n: int):
        copy = n
        index = 0
        while copy > 0:
            current_bit = copy & 1
            if current_bit == 1:
                self.one_bits_positions.append(index)
            index += 1
            copy >>= 1

        first_and_last_bits_one = {0, (n.bit_length() - 1)} == set(self.one_bits_positions)
        two_last_bits_one = {(n.bit_length() - 1), (n.bit_length() - 2)} == set(self.one_bits_positions)
        if two_last_bits_one or first_and_last_bits_one:
            return True
        return False

    def minimumOneBitOperations(self, n: int) -> int:
        print(f"{format(n, 'b')} - INÍCIO")
        self.one_bits_positions = []
        operations_counter = 0
        if n == 0:
            return 0
        if self.should_begin_with_second(n):
            while n != 0 and n not in self.number_operations_needed:
                n = self.second_operation(n)
                operations_counter += 1
                if n == 0:
                    continue
                n = self.first_operation(n)
                operations_counter += 1
        while n != 0 and n not in self.number_operations_needed:
            n = self.first_operation(n)
            operations_counter += 1
            if n == 0:
                continue
            n = self.second_operation(n)
            operations_counter += 1
        return self.number_operations_needed[n] + operations_counter if n in self.number_operations_needed else operations_counter


if __name__ == '__main__':
    s = Solution()

    # resultado = s.minimumOneBitOperations(n=3)
    # printarResultadoEsperado(resultado, 2)

    # resultado = s.minimumOneBitOperations(n=100)
    # printarResultadoEsperado(resultado, 71)

    # resultado = s.minimumOneBitOperations(n=8)
    # printarResultadoEsperado(resultado, 15)

    # resultado = s.minimumOneBitOperations(n=6)
    # printarResultadoEsperado(resultado, 4)

    # resultado = s.minimumOneBitOperations(n=9)
    # printarResultadoEsperado(resultado, 14)

    # resultado = s.minimumOneBitOperations(n=333)
    # printarResultadoEsperado(resultado, 393)

    resultado = s.minimumOneBitOperations(n=88)
    printarResultadoEsperado(resultado, 7)
