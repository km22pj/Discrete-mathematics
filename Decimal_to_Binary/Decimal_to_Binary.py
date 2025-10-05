def main():
    decimal_input = input("10진수 입력: ")
    if decimal_input == "0":
        print("2진수: 0")
    else:
        binary_output = decimal_to_binary(decimal_input)
        print("2진수: ", binary_output)


def decimal_to_binary(decimal_str):
    binary = ""
    remainder = ""
    decimal = int(decimal_str)

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary

if __name__=='__main__':
    main()