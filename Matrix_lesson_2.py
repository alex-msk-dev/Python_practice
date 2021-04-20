import random


def print_matrix(NxM, rows, columns, title): #Выведение матрицы на экран
    print(title)
    for i in range(rows):
        row = ''
        for j in range(columns):
            cell = NxM[i][j]
            cell_formated = f'{cell:>5}, '
            row = row + cell_formated
        print(row)


def generation_matrix(rows, columns): #Создали матрицу
    NxM = [[random.randint(-10, 10) for i in range(columns)] for j in range(rows)]
    return NxM


def null_rows_and_columns(NxM, rows, columns): #Зануляем матрицу
    rows_to_be_null = set()
    columns_to_be_null = set()
    for i in range(rows):
        for j in range(columns):
            if NxM[i][j] == 0:
                rows_to_be_null.add(i)
                columns_to_be_null.add(j)

    for i in rows_to_be_null:
        for j in range(columns):
            NxM[i][j] = 0

    for j in columns_to_be_null:
        for i in range(rows):
            NxM[i][j] = 0


def main():
    rows, columns = 5, 7
    NxM = generation_matrix(rows, columns)
    print_matrix(NxM, rows, columns, "Исходная матрица")

    null_rows_and_columns(NxM, rows, columns)
    print_matrix(NxM, rows, columns, "Матрица после зануления")


main()
