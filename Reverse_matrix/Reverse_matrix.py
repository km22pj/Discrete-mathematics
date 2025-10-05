# 행렬 출력
def printmatrix(matrix):
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix)):
            print("%6.3f" %matrix[i][j], end=" ")
        print("|")

# 전치행렬
def transposematrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

# 소행렬
def matrixminor(matrix, i ,j):
    return [(row[0:j] + row[j+1:]) for row in (matrix[0:i] + matrix[i+1:])]

# 행렬식 계산
def matrixdeterminant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    determinant = 0
    for i in range(len(matrix)):
        determinant += ((-1)**i) * matrix[0][i] * matrixdeterminant(matrixminor(matrix, 0, i))
    return determinant



# 행렬식을 이용한 역행렬 계산
def inverse_matrix(matrix):
    determinant = matrixdeterminant(matrix)

    # 행렬식이 0이면 역행렬이 존재하지 않음
    if determinant == 0:
        print("Error! determinant is 0")
        return None

    if len(matrix) == 1:
         return [[1/matrix[0][0]]]

    if len(matrix) == 2:
        return [[matrix[1][1]/determinant, -1 * matrix[0][1]/determinant],
                [-1 * matrix[1][0]/determinant, matrix[0][0]/determinant]]

    n = len(matrix)
    cofactors = []      # 여인수 행렬
    for row in range(n):
        cofactor_row = []
        for col in range(n):
            minior = matrixminor(matrix, row, col)
            cofactor_row.append(((-1)**(row+col)) * matrixdeterminant(minior))
        cofactors.append(cofactor_row)

    trans = transposematrix(cofactors)
    for row in range(len(trans)):
        for col in range(len(trans)):
            trans[row][col] = trans[row][col] / determinant
    return trans



# 가우스-조던 소거법을 이용한 역행렬
def GaussJordan(matrix):
    n = len(matrix)
    # 단위행렬 생성
    unit_matrix = [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    for i in range(n):   # 주대각 성분이 0이라면 행을 서로 교환
        if matrix[i][i] == 0:
            flag = 0
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    unit_matrix[i], unit_matrix[j] = unit_matrix[j], unit_matrix[i]
                    flag = 1
                    break
            # 하나의 열이 전부 0일 경우 역행렬이 존재하지 않음
            if flag == 0:
                print("Error! Can't find a non-zero pivot")
                return 0
        # 주대각 성분을 1로 만듦
        scala = 1/matrix[i][i]
        for j in range(n):
            matrix[i][j] *= scala
            unit_matrix[i][j] *= scala
        # 주대각을 성분 외 나머지 부분을 전부 0으로 만듦
        for j in range(n):
            if i == j:
                continue
            scala = -1 * matrix[j][i]
            for k in range(n):
                matrix[j][k] += scala * matrix[i][k]
                unit_matrix[j][k] += scala * unit_matrix[i][k]
    return unit_matrix



def main():
    matrix = []
    while True:     # 올바른 차수의 값이 입력될 때까지 반복함
        try:
            n = int(input("정방행렬의 차수를 입력하시오 : "))
            if n <= 0:
                print("양의 정수를 입력하시오")
                continue
            break
        except ValueError:
            print("정수를 입력하시오")
        except Exception as e:
            print("예상치 못한 오류 발생 : ", e)

    while True:
        try:        # 한 행에 정확히 n개의 숫자를 입력할 수 있도록 함
            i = 0
            while i < n:
                row = list(map(float, input("%d 행 입력 : " %(i+1)).strip().split()))
                if len(row) != n:
                    print("정확히 %d개를 입력하시오" %n)
                    continue
                matrix.append(row)
                i += 1
            break
        except ValueError:
            print("정수를 입력하시오")
        except Exception as e:
            print("예상치 못한 오류 발생 : ", e)


    # 행렬식을 이용한 역행렬
    matrix_copy1 = [row[:] for row in matrix]
    matrix_a = inverse_matrix(matrix_copy1)
    if matrix_a:
        print("행렬식을 이용한 역행렬 : ")
        printmatrix(matrix_a)
    print()
    # 가우스 조던 소거법을 이용한 역행렬
    matrix_copy2 = [row[:] for row in matrix]
    matrix_b = GaussJordan(matrix_copy2)
    if matrix_b:
        print("가우스 조던 소거법을 이용한 역행렬 : ")
        printmatrix(matrix_b)
    print()

    # 두 방법으로 구한 결과가 동일한지 비교
    same = True
    if matrix_a and matrix_b:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if abs(matrix_a[row][col] - matrix_b[row][col]) > 1e-10:
                    same = False
                    break
            if not same:
                break

    if matrix_a and matrix_b:   # 역행렬이 존재할때만 비교
        if same:
            print("두 방법으로 계산한 역행렬이 동일하다.")
        else:
            print("두 방법으로 계산한 역행렬이 동일하지 않다.")


if __name__ == '__main__':
    main()