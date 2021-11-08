from matrix import *
import random


class DiagonalMatrix(Matrix):
    def __init__(self):
        self.__matrix = None
        self.__length = 0

    def read_from_file(self, str_array, i):
        self.__length = int(str_array[i])
        i += 1

        self.__matrix = [0.0] * self.__length
        for k in range(0, self.__length):
            self.__matrix[k] = float(str_array[i])
            i += 1
        return i

    def random_input(self):
        self.__length = random.randint(1, 20)

        self.__matrix = [0.0] * self.__length
        for k in range(0, self.__length):
            self.__matrix[k] = round(random.uniform(-10, 10), 2)
        pass

    def print_to_console(self):
        print("\n\n\nDiagonal matrix (" + str(self.__length) + "x" + str(self.__length) + ")\n\n")
        for i in range(0, self.__length):
            for j in range(0, self.__length):
                if j == i:
                    print(str(self.__matrix[i]) + " ")
                else:
                    print(0, end=' ')
            print("" if i == self.__length - 1 else "\n")
        print("\n\nMean: " + str(round(self.get_mean(), 5)))
        pass

    def write_to_file(self, output_stream):
        output_stream.write("\n\n\nDiagonal matrix (" + str(self.__length) + "x" + str(self.__length) + ")\n\n")
        for i in range(0, self.__length):
            for j in range(0, self.__length):
                if j == i:
                    output_stream.write(str(self.__matrix[i]) + " ")
                else:
                    output_stream.write("0 ")
            output_stream.write("" if i == self.__length - 1 else "\n")
        output_stream.write("\n\nMean: " + str(round(self.get_mean(), 5)))
        pass

    def get_mean(self):
        elements_sum = 0.0
        for i in range(0, self.__length):
            elements_sum += self.__matrix[i]
        return elements_sum / (self.__length * self.__length)