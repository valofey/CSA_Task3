from matrix import *
import random


class NormalMatrix(Matrix):
    def __init__(self):
        self.__matrix = None
        self.__length = 0

    def read_from_file(self, str_array, i):
        self.__length = int(str_array[i])
        i += 1

        self.__matrix = [[0.0] * self.__length for a in range(self.__length)]
        for k in range(0, self.__length):
            for j in range(0, self.__length):
                self.__matrix[k][j] = float(str_array[i])
                i += 1
        return i

    def random_input(self):
        self.__length = random.randint(1, 20)
        self.__matrix = [[0.0] * self.__length for k in range(self.__length)]
        for i in range(0, self.__length):
            for j in range(0, self.__length):
                self.__matrix[i][j] = round(random.uniform(-10, 10), 2)
        pass

    def print_to_console(self):
        print("\n\n\nNormal matrix (" + str(self.__length) + "x" + str(self.__length) + ")\n\n")
        for i in range(0, self.__length):
            for j in range(0, self.__length):
                print(str(self.__matrix[i][j]) + " ")
            print("" if i == self.__length - 1 else "\n")
        print("\n\nMean: " + str(round(self.get_mean(), 5)))
        pass

    def write_to_file(self, output_stream):
        output_stream.write("\n\n\nNormal matrix (" + str(self.__length) + "x" + str(self.__length) + ")\n\n")
        for i in range(0, self.__length):
            for j in range(0, self.__length):
              output_stream.write(str(self.__matrix[i][j]) + " ")
            output_stream.write("" if i == self.__length - 1 else "\n")
        output_stream.write("\n\nMean: " + str(round(self.get_mean(), 5)))
        pass

    def get_mean(self):
        elements_sum = 0.0
        for i in range(0, self.__length):
            for j in range(0, self.__length):
                elements_sum += self.__matrix[i][j]
        return elements_sum / (self.__length * self.__length)