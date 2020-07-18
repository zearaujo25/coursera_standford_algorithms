def multiply(integer1,integer2):
    integer1_size = len(integer1)
    integer2_size = len(integer2)
    sum_stack = []
    for digit1_position in range(integer1_size-1,-1,-1):
        digit1 = int(integer1[digit1_position])
        sum_factor = int(0)
        string_line_result = ''
        digit1_order =  10**(integer1_size-1 - digit1_position)
        for digit2_position in range(integer2_size-1,-1,-1):
            digit2 = int(integer2[digit2_position])
            digit_multiplication =  str(digit1*digit2 + sum_factor)
            sum_factor = int(digit_multiplication[0] if len(digit_multiplication) >1 else 0)
            digit_result = int(digit_multiplication[1] if len(digit_multiplication) >1 else digit_multiplication[0])
            string_line_result = str(digit_result) + string_line_result
        
        string_line_result = string_line_result if sum_factor == 0 else str(sum_factor) + string_line_result
        line_result = int(string_line_result)*digit1_order
        sum_stack.append(int(line_result))
    return sum(sum_stack)
        
def main():
    integer1 = '3141592653589793238462643383279502884197169399375105820974944592'
    integer2 = '2718281828459045235360287471352662497757247093699959574966967627'
    result = multiply(integer1,integer2)
    print(result)

if __name__ == '__main__':
    main()