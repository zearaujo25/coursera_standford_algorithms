def multiply_recursively(integer1,integer2):
    integer1, integer2, size = paddle_inputs(integer1, integer2)

    is_single_digit1 = len(integer1) <= 1
    is_single_digit2 = len(integer2) <= 1
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

    return int((10**size) * ac + (10**(size//2))*(ad + bc) + bd)

def paddle_inputs(integer1, integer2):
    paddled_size = max(len(integer1),len(integer2))
    if (paddled_size & (paddled_size-1) != 0):
        while (paddled_size & (paddled_size-1) != 0):
            paddled_size+=1

    while len(integer1) < paddled_size:
        integer1 = "0"+integer1
    while len(integer2) < paddled_size:
        integer2 = "0"+integer2

    return integer1, integer2, paddled_size
        
def main():
    integer1 = '341'
    integer2 = '456'
    result = multiply_recursively(integer1,integer2)
    assert result == 155496 ,"Wrong result: {}".format(result)
    print(result)

if __name__ == '__main__':
    main()