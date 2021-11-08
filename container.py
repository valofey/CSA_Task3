from diagonalMatrix import DiagonalMatrix
from normalMatrix import NormalMatrix
from lowerTriangularMatrix import LowerTriangularMatrix
import random


class Container:
    def __init__(self):
        self.store = []

    def print_container(self):
        print("There are ", len(self.store), "matrices currently in this container:\n")
        for matrix in self.store:
            matrix.print_to_console()
        pass

    def write_container(self, output_stream):
        output_stream.write("There are {} matrices currently in this container:\n".format(len(self.store)))
        for matrix in self.store:
            matrix.write_to_file(output_stream)
            output_stream.write("\n")
        pass

    def merge_sort(self, arr):
        if len(arr) > 1:
         # Ищем середину массива.
          mid = len(arr)//2
  
        # Сохраняем отдельно левую часть.
          L = arr[:mid]
  
        # Сохраняем отдельно правую часть.
          R = arr[mid:]
  
        # Сортируем левую часть.
          self.merge_sort(L)
  
        # Сортируем правую часть.
          self.merge_sort(R)
  
          i = j = k = 0
  
        # Переносим данные во временные массивы L и R.
          while i < len(L) and j < len(R):
            if L[i].get_mean() > R[j].get_mean():
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Объединяем массивы в изначальном.
          while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
          while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def read_str_array(self, str_array):
        array_len = len(str_array)
        # Индекс, задающий текущую строку в массиве.
        i = 0
        fig_num = 0
        while i < array_len:
            key = int(str_array[i])
            if key == 1:
                i += 1
                matrix = NormalMatrix()
                # Чтение нормальной матрицы с возвратом позиции.
                i = matrix.read_from_file(str_array, i)
            elif key == 2:
                i += 1
                matrix = DiagonalMatrix()
                # Чтение диагональной матрицы с возвратом позиции.
                i = matrix.read_from_file(str_array, i)
            elif key == 3:
                i += 1
                matrix = LowerTriangularMatrix()
                # Чтение треугольной матрицы с возвратом позиции.
                i = matrix.read_from_file(str_array, i)
            else:
                # Возврат количества прочитанных фигур.
                return fig_num

            fig_num += 1
            self.store.append(matrix)
        return fig_num

    def create_random(self, number):
        for i in range(number):
            self.store.append(random_matrix())
        pass


def random_matrix():
    identifier = random.randint(1, 3)
    matrix = None
    if identifier == 1:
        matrix = NormalMatrix()
    elif identifier == 2:
        matrix = DiagonalMatrix()
    elif identifier == 3:
        matrix = LowerTriangularMatrix()

    matrix.random_input()
    return matrix