import random

def print_matrix(NxM, rows, columns, title): #Выведение матрицы на экран
    print(title)
    for i in range(0, rows):
        row = ''
        for j in range(0, columns):
            cell = NxM[i][j]
            cell_formated = f'{cell:>5}, '
            row = row + cell_formated
        print(row)

def generation_matrix(rows, columns): #Создали матрицу
    NxM=[[random.randint(-10,10) for i in range(1,rows+1)] for j in range(0,columns)]
    return NxM

def null_rows_or_columns(NxM, null_coordinates): #Зануляем матрицу по координатам
    for i in null_coordinates:
    	NxM[i[0]][i[1]] = 0

def main():
    rows, columns = 10, 10
    NxM=generation_matrix(rows, columns)
    print_matrix(NxM, rows, columns, "Исходная матрица")
    null_el = [[0, 1], [1, 2]]
    null_rows_or_columns(NxM, null_el)
    print_matrix(NxM, rows, columns, "Матрица после зануления")

main()