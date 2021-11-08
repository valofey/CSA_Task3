import sys
import time

from container import *

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("incorrect command line!\n"
              "  Waited:\n"
              "     main -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     main -n number outfile01 outfile02\n")
        exit(1)

    start = time.perf_counter()

    # Cоздание контейнера.
    print('==> Start')
    container = Container()

    if sys.argv[1] == "-f":
        # Чтение из тестового файла.
        inputFileName = sys.argv[2]
        outputFileName = sys.argv[3]
        outputFileName_2 = sys.argv[4]

        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки.
        input_file_name = open(inputFileName)
        input_string = input_file_name.read()
        input_file_name.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        str_array = input_string.replace("\n", " ").split(" ")
        while str_array.__contains__(''):
            str_array.remove('')

        container.read_str_array(str_array)
        # Можно сделать container.print_container().

    elif sys.argv[1] == "-n":
        random_number = int(sys.argv[2])
        outputFileName = sys.argv[3]
        outputFileName_2 = sys.argv[4]

        container.create_random(random_number)
        # Можно сделать container.print_container().
    else:
        print("Incorrect command line!")
        exit()
        pass

    # Вывод до выполнения функции.
    output_file = open(outputFileName, 'w')
    container.write_container(output_file)
    output_file.close()

    container.merge_sort(container.store)

    # Вывод после выполнения функции.
    output_file = open(outputFileName_2, 'w')
    container.write_container(output_file)
    output_file.close()

    end = time.perf_counter()
    print(f"Time spent: {end - start:0.4f} seconds")
    print('==> Finish')
pass