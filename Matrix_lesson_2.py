import random

def print_matrix(NxM, title="Исходная матрица"): #Выведение матрицы на экран
    print(title)
    for i in range(0, 5):
        row = ''
        for j in range(0, 5):
            cell = NxM[i][j]
            cell_formated = f'{cell:>5}, '
            row = row + cell_formated
        print(row)

def generation_matrix(rows, columns): #Создали матрицу
    NxM=[[random.randint(-10,10) for i in range(1,rows)] for j in range(1,columns)]
    return NxM

def null_rows_null_columns(NxM, columns, rows, null_rows=None, null_columns=None):
    null_rows = null_rows or []
    null_columns = null_columns or []
    for i in range(rows):
           for j in range(columns):
            if i in null_rows or j in null_columns:
                NxM[i][j] = 0

def main():
    rows, columns, n = 10, 10, 5
    NxM=generation_matrix(rows, columns)
    print_matrix(NxM)
    print("Матрица после зануления")
    null_rows_null_columns(NxM, rows, columns, null_rows=(0), null_columns=(0))
    print_matrix(NxM)
main()