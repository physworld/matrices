def input_matrix(rows, columns):  # Считывает матрицу заданой размерности
    matrix = []
    for i in range(int(rows)):
        row = input()
        row = row.split()
        while len(row) != int(columns):
            print('Write correct number of data!')
            row = input()
            row = row.split(' ')
        matrix.append(row)
    return matrix


def input_matrix_with_dimension():  # Считывает матрицу одновременно с размерностью
    dimension = input('Enter size of matrix: ')
    dimension = dimension.split(' ')
    print('Enter matrix: ')
    matrix = input_matrix(dimension[0], dimension[1])
    return dimension, matrix


def input_square_matrix():
    dimension = input('Enter size of matrix: ')
    dimension = dimension.split(' ')
    while dimension[0] != dimension[1]:
        print('You must write square matrix!')
        dimension = input('Enter size of matrix: ')
        dimension = dimension.split(' ')
    print('Enter matrix:')
    matrix = input_matrix(dimension[0], dimension[1])
    return dimension, matrix


def calculate_determinant(matrix):  # Алгоритм считает детерминант через рекурсию
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
    else:
        det = 0
        for i in range(len(matrix)):
            minor = []
            for j in range(1, len(matrix)):
                line_of_minor = []
                for k in range(len(matrix)):
                    if k != i:
                        line_of_minor.append(matrix[j][k])
                minor.append(line_of_minor)
            det += float(matrix[0][i]) * ((-1) ** (2 + i)) * calculate_determinant(minor)
    return det


def calculate_cofactors(matrix):
    if len(matrix) == 1:
        return 1 / matrix[0][0]
    elif len(matrix) == 2:
        return [[float(matrix[1][1]), -1 * float(matrix[1][0])], [-1 * float(matrix[0][1]), float(matrix[0][0])]]
    else:
        result = []
        for a in range(len(matrix)):  # За каждый проход цикла создаем 1 линию в матрице кофакторов
            line_of_result = []
            for i in range(len(matrix)):  # За каждый проход создаем 1 элемент для строчки матрицы кофакторов
                minor = []
                for j in range(len(matrix)):  # За каждый проход создаем строчку для минора кофактора
                    line_of_minor = []
                    for k in range(len(matrix)):  # За каждый проход создаем элемент строчки минора кофактора
                        if k != i and j != a:
                            line_of_minor.append(matrix[j][k])
                    if line_of_minor: minor.append(line_of_minor)
                cofactor = ((-1) ** (2 + i + a)) * calculate_determinant(minor)
                line_of_result.append(cofactor)
            result.append(line_of_result)
    return result


def formatting_of_input(matrix):
    maximum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len('{:.2f}'.format(matrix[i][j])) > maximum:
                maximum = len('{:.2f}'.format(matrix[i][j]))  # НАХОДИМ САМУЮ ДЛИННУЮ СТРОКУ
    for i in range(len(matrix)):
        string = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == -0.0 or matrix[i][j] == 0.0:  # ЕСЛИ СТРОЧКА БЫЛА НУЛЕМ, ОТОДВИГАЕМ ЕЕ НА ДЛИНУ
                matrix[i][j] = '{:>{number}}'.format('0', number=maximum)  # САМОЙ ДЛИННОЙ СТРОКИ
            else:
                matrix[i][j] = '{: .2f}'.format(matrix[i][j])  # ФОРМАТИРУЕМ ОТВЕТ ДО ДВУХ ЦИФР ПОСЛЕ ТОЧКИ
            string.append(matrix[i][j])
        print(' '.join(string))


print("HI! IT'S A PROGRAM FOR WORKING WITH MATRICES!")
while True:
    print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    choice = input('Your choice: ')
    while choice not in '1234560':
        print('Chose 1, 2, 3, 4, 5, 6 or 0!')
        choice = input('Your choice: ')
    else:
        if choice == '1':  # ПРИБАВЛЕНИЕ ДВУХ МАТРИЦ
            first_matrix_dimension = input('Enter size of first matrix: ')
            first_matrix_dimension = first_matrix_dimension.split(' ')
            print('Enter first matrix: ')
            first_matrix = input_matrix(first_matrix_dimension[0], first_matrix_dimension[1])
            second_matrix_dimension = input('Enter size of second matrix: ')
            second_matrix_dimension = second_matrix_dimension.split(' ')
            # Если размерности матриц не совпадают - выводим ошибку
            while (first_matrix_dimension[0] != second_matrix_dimension[0]) or (
                    first_matrix_dimension[1] != second_matrix_dimension[1]):
                print('Both matrices must have the same dimension!')
                second_matrix_dimension = input('Enter size of second matrix: ')
                second_matrix_dimension = second_matrix_dimension.split(' ')
            print('Enter second matrix: ')
            second_matrix = input_matrix(second_matrix_dimension[0], second_matrix_dimension[1])
            print('The result is:')
            for i in range(int(first_matrix_dimension[0])):
                answer = []
                for j in range(int(first_matrix_dimension[1])):
                    answer.append(str(float(first_matrix[i][j]) + float(second_matrix[i][j])))
                answer = ' '.join(answer)
                print(answer)
        elif choice == '2':  # УМНОЖЕНИЕ МАТРИЦЫ НА ЧИСЛО
            dimension, matrix = input_matrix_with_dimension()
            multiplier = float(input('Enter constant: '))
            print('The result is:')
            for i in range(len(matrix)):
                for j in range(len((matrix[i]))):
                    matrix[i][j] = str(round(float(matrix[i][j]) * multiplier, 2))
                print(' '.join(matrix[i]))
        elif choice == '3':  # ПЕРЕМНОЖЕНИЕ МАТРИЦ
            first_matrix_dimension = input('Enter size of first matrix: ')
            first_matrix_dimension = first_matrix_dimension.split(' ')
            print('Enter first matrix: ')
            first_matrix = input_matrix(first_matrix_dimension[0], first_matrix_dimension[1])
            second_matrix_dimension = input('Enter size of second matrix: ')
            second_matrix_dimension = second_matrix_dimension.split(' ')
            while first_matrix_dimension[1] != second_matrix_dimension[0]:
                print('Incorrect dimensions!')
                second_matrix_dimension = input('Enter size of second matrix: ')
                second_matrix_dimension = second_matrix_dimension.split(' ')
            print('Enter second matrix: ')
            second_matrix = input_matrix(second_matrix_dimension[0], second_matrix_dimension[1])
            print('The result is:')
            for i in range(int(first_matrix_dimension[0])):
                row = []
                for j in range(int(second_matrix_dimension[1])):
                    dot_product = 0
                    for k in range(int(first_matrix_dimension[1])):
                        dot_product += float(first_matrix[i][k]) * float(second_matrix[k][j])
                    row.append(str(dot_product))
                print(' '.join(row))
        elif choice == '4':  # ТРАНСПОНИРОВАНИЕ МАТРИЦ
            print('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
            choice_two = input('Your choice: ')
            while choice_two not in '1234':
                print('Chose 1, 2, 3, or 4!')
                choice_two = input('Your choice: ')
            else:
                if choice_two == '1':  # ОТНОСИТЕЛЬНО ГЛАВНОЙ ДИАГОНАЛИ
                    dimension, matrix = input_matrix_with_dimension()
                    print('The result is:')
                    for i in range(int(dimension[1])):
                        row = []
                        for j in range(int(dimension[0])):
                            row.append(matrix[j][i])
                        print(' '.join(row))
                elif choice_two == '2':  # ОТНОСИТЕЛЬНО ПОБОЧНОЙ ДИГОНАЛИ
                    dimension, matrix = input_matrix_with_dimension()
                    print('The result is:')
                    for i in range(int(dimension[1]) - 1,  -1, -1):
                        row = []
                        for j in range(int(dimension[0]) - 1,  -1, -1):
                            row.append(matrix[j][i])
                        print(' '.join(row))
                elif choice_two == '3':  # ОТНОСИТЕЛЬНО ВЕРТИКАЛИ
                    dimension, matrix = input_matrix_with_dimension()
                    print('The result is:')
                    for i in range(int(dimension[1])):
                        row = []
                        for j in range(int(dimension[0]) - 1, -1, -1):
                            row.append(matrix[i][j])
                        print(' '.join(row))
                elif choice_two == '4':  # ОТНОСИТЕЛЬНО ГОРИЗОНТАЛИ
                    dimension, matrix = input_matrix_with_dimension()
                    print('The result is:')
                    for i in range(int(dimension[1]) - 1,  -1, -1):
                        print(' '.join(matrix[i]))
        elif choice == '5':  # ПОДСЧЕТ ДЕТЕРМИНАНТА
            dimension, matrix = input_square_matrix()
            print('The result is:')
            print(calculate_determinant(matrix))
        elif choice == '6':  # ОБРАТНАЯ МАТРИЦА
            dimension, matrix = input_square_matrix()
            if calculate_determinant(matrix) == 0:
                print("This matrix doesn't have an inverse.")
            else:
                print('The result is:')
                matrix_of_cofactors = calculate_cofactors(matrix)  # ПОЛУЧАЕМ МАТРИЦУ КОФАКТОРОВ
                transpose_matrix = []
                for i in range(int(dimension[1])):
                    row = []
                    for j in range(int(dimension[0])):
                        row.append(matrix_of_cofactors[j][i])
                    transpose_matrix.append(row)  # ТРАНСПОНИРУЕМ МАТРИЦУ КОФАКТОРОВ
                for i in range(len(transpose_matrix)):
                    for j in range(len((transpose_matrix[i]))):
                        transpose_matrix[i][j] = float(transpose_matrix[i][j]) / calculate_determinant(matrix)
                formatting_of_input(transpose_matrix)
        else:  # ВЫХОД
            break
