from itertools import repeat


def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Первый (внешний) цикл для создания строк
    for i in range(n):
        # Добавляем пустой список (строку) в матрицу
        row = []
        matrix.append(row)

        # Второй (внутренний) цикл для заполнения строки значениями
        for j in range(m):
            row.append(value)

    # Возвращаем матрицу
    return matrix

print(get_matrix(2, 3, 10))







        
