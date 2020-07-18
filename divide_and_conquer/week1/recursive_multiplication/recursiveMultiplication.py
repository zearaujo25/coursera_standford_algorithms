def multiply_recursively(integer1,integer2):
    size = len(integer1)
    is_single_digit1 = len(integer1) == 1
    is_single_digit2 = len(integer2) == 1
    if(is_single_digit1 and is_single_digit2):
        return int(integer1)*int(integer2)

    a = integer1[:len(integer1)//2]
    b = integer1[len(integer1)//2:]

    c = integer2[:len(integer2)//2]
    d = integer2[len(integer2)//2:]

    
    ac = multiply_recursively(a,c)
    ad = multiply_recursively(a,d)
    bc = multiply_recursively(b,c)
    bd = multiply_recursively(b,d)
    
    # print("INTEGERS: {}".format((integer1,integer2)))
    # print("ac: {}, ad: {}, bc: {}, d: {}".format(ac,ad,bc,bd))
    # print(int((10**size) * ac + (10**(size/2))*(ad + bc) + bd))

    return int((10**size) * ac + (10**(size//2))*(ad + bc) + bd)
        
def main():
    integer1 = '1234'
    integer2 = '5678'
    result = multiply_recursively(integer1,integer2)
    print(result)

if __name__ == '__main__':
    main()