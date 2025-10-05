def main():
    binary = input("2진수 입력: ")
    binary = binary[::-1]
    answer = "0"
    multiplier = "1"

    for b in binary:
        if b == "1":
            answer = addStrings(answer, multiplier)
        multiplier = multiply(multiplier, "2")
    print("10진수: ", answer)


def addStrings(num1, num2):
    res = []
    carry = 0
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1>=0 or p2>=0:
        x1 = ord(num1[p1]) - ord('0') if p1>=0 else 0
        x2 = ord(num2[p2]) - ord('0') if p2>=0 else 0
        value = (x1+x2+carry) % 10
        carry = (x1+x2+carry) // 10
        res.append(value)
        p1 -= 1
        p2 -= 1
    if carry:
        res.append(carry)
    return ''.join(str(x) for x in res[::-1])


def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    N = len(num1) + len(num2)
    answer = [0] * N
    first_number = num1[::-1]
    second_number = num2[::-1]

    for place2, digit2 in enumerate(second_number):
        for place1, digit1 in enumerate(first_number):
            num_zeros = place1 + place2
            carry = answer[num_zeros]
            multiplication = int(digit1)*int(digit2)+carry
            answer[num_zeros] = multiplication%10
            answer[num_zeros+1] += multiplication//10
    if answer[-1] == 0:
        answer.pop()
    return ''.join(str(digit) for digit in reversed(answer))


if __name__ == '__main__':
    main()