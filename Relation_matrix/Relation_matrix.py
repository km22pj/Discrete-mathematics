
# 반사 관계 판별
def is_Reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

# 대칭 관계 판별
def is_Symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:       # i,j 값이 1이면 j,i도 1이어야함
                if matrix[j][i] != 1:
                    return False
            else:
                if matrix[j][i] != 0:   # i,j 값이 0이면 j,i도 0이어야함
                    return False
    return True

# 추이 관계 판별
def is_Transitive(matrix):
    n = len(matrix)
    combined = [row[:] for row in matrix]   # 누적 합집합
    tem = [[0]*n for _ in range(n)]  # 임시 행렬 생성
    # 부울 곱 수행해서 M을 만듦
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tem[i][j] |= matrix[i][k] & matrix[k][j]
    # 만든 행렬 M을 ^n제곱을 수행함
    for _ in range(n):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    combined[i][j] |= tem[i][k] & tem[k][j]
        # 부울곱을 수행한 모든 M^n관계행렬이 matrix의 부분집합인지 확인
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if tem[i][j] == 1 and matrix[i][j] == 0:        # R^n은 1이면서 R은 0인 경우
                    return False                                # R의 부분집합이 아니므로 추이관계 아님
    return True


# 동치 관계 판별
def is_Equivalence(matrix):
    Equivalence_flag = False
    Reflex_flag = False
    Symmetrix_flag = False
    Transitive_flag = False
    # 반사, 대칭, 추이 관계 판별하여 플래그에 반영
    if is_Reflexive(matrix):
        print("입력한 관계행렬은 반사관계이다 ")
        Reflex_flag = True
    else:
        print("입력한 관계행렬은 반사관계가 아니다 ")
    if is_Symmetric(matrix):
        print("입력한 관계행렬은 대칭관계이다 ")
        Symmetrix_flag = True
    else:
        print("입력한 관계행렬은 대칭관계가 아니다 ")
    if is_Transitive(matrix):
        print("입력한 관계행렬은 추이관계이다 ")
        Transitive_flag = True
    else:
        print("입력한 관계행렬은 추이관계가 아니다 ")
    if Reflex_flag and Symmetrix_flag and Transitive_flag:
        print("입력한 관계행렬은 동치관계이다 ")
        print()
        Equivalence_flag = True
    else:
        print("입력한 관계행렬은 동치관계가 아니다 ")
        print()
    return Equivalence_flag, Reflex_flag, Symmetrix_flag, Transitive_flag


# 동치류 판별 후 출력
def print_Equivalence(matrix):
    print("동치류 : ")
    for i in range(len(matrix)):
        print("[%d] = {" %(i+1), end=" ")
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                print("%d," %(j+1), end=" ")
        print("\b\b }")



# 반사 폐포로 변환
def Reflexive_closure(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            matrix[i][i] = 1

# 대칭 폐포로 변환
def Symmetric_closure(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                matrix[j][i] = 1

# 추이 폐포로 변환 Warshall
def Transitive_closure(matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = 1

# 관계 출력
def print_Relation(matrix):
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix)):
            print("%d" %matrix[i][j], end=" ")
        print("|")
    print()


def main():

    # 사용자로부터 5 x 5크기의 정방행렬을 행단위로 입력받음
    # 입력받은 관계행렬 데이터를 2차원 리스트에 저장
    n = 5
    print("1과 0으로 구성된 ", n, "x", n, "인 관계행렬을 입력하시오: ")
    matrix = []
    for i in range(n):
        while True:                                                 # 올바른 입력을 받을 때까지 반복
            try:
                row = list(map(int, input().split()))               # 입력받은 데이터를 문자열에서 정수로 변환
                if len(row) != n:                                   # 입력반은 관계행렬의 길이가 n인지 확인
                    print("Error! 정확히 %d개의 숫자를 입력하시오. " %n)
                    continue
                if row.count(0) + row.count(1) != n:                # 0과 1만 입력받았는지 확인
                    print("Error! 0과 1만 입력하시오.")
                    continue

                matrix.append(row)  # 정확한 개수를 입력했다면 matrix에 추가
                break               # while문 탈출
            except ValueError:      # 숫자가 아닌값을 입력했을때 예외처리
                print("Error! 숫자만 입력하시오. ")

    Equi_flag = False
    Reflex_flag = False
    Symmet_flag = False
    Trans_flag = False
    # 관계의 성질 판별
    Equi_flag,Reflex_flag,Symmet_flag,Trans_flag = is_Equivalence(matrix)

    # 동치관계 flag가 참일 경우 동치류 출력
    if Equi_flag:
        print_Equivalence(matrix)
    # 동치관계 flag가 거짓일 경우
    else:
        matrix_cp = [row[:] for row in matrix]

        if not Reflex_flag:
            print("반사 폐포 변환 전 관계행렬")
            print_Relation(matrix_cp)
            print("반사 폐포 변환 후 관계행렬")
            Reflexive_closure(matrix_cp)
            print_Relation(matrix_cp)
        if not Symmet_flag:
            print("대칭 폐포 변환 전 관계행렬")
            print_Relation(matrix_cp)
            print("대칭 폐포 변환 후 관계행렬")
            Symmetric_closure(matrix_cp)
            print_Relation(matrix_cp)
            Trans_flag = False # 추이관계가 깨질 수 있으므로 flag를 False로 바꿔줌
        if not Trans_flag:
            print("추이 폐포 변환 전 관계행렬")
            print_Relation(matrix_cp)
            print("추이 폐포 변환 후 관계행렬")
            Transitive_closure(matrix_cp)
            print_Relation(matrix_cp)


        # 각각의 폐포로 변환한 후 동치관계 다시 판별
        Equi_flag, Reflex_flag, Symmet_flag, Trans_flag = is_Equivalence(matrix_cp)
        # 동치관계 flag가 참일 경우 동치메시지 출력
        if Equi_flag:
            print("폐포 변환 후 관계행렬은 동치관계가 되었다 ")
            # 동치류 출력
            print_Equivalence(matrix_cp)





if __name__ == '__main__':
    main()

