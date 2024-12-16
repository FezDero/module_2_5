def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(3,3,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,4,13)

    # 1 вариант решения, с указанием как заявлено в задаче - весь вывод в строку
print (*result1)
print (*result2)
print (*result3)

    # 2 вариант решения, с указанием как в задаче, но через цикл, и через * чтобы убрать квадратные
    #скобки [] у списка matrix
# for matrix in (result1, result2, result3):
#     print(*matrix)

    # 3 вариант решения, выводит каждую матрицу result1, result2, result3, с распаковкой

# for matrix in result1:
#     print (*matrix,  sep=' ')
# for matrix in result2:
#     print (*matrix, sep=' ')
# for matrix in result3:
#     print (*matrix, sep=' ')


