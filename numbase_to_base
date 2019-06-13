"""Converts decimal to any base"""
def dec_to_base(n,b):
    if n < b:
        #fringe case of unary conversion
        if b == 1:
            return [n]
        else:
            return [n]
    else:
        #print(n//b, ":" ,n%b)
        if b == 1:
            return dec_to_base(n-1,b) + [1]
        else:
            return dec_to_base(n//b, b) + [n%b]
            
"""Converts any number to unary base. *Not implemented in solution"""
def num_to_unary(n,b):
    if n <= 1:
        if n == 0:
            return [0]
        else:
            return [1]
    else:
        return num_to_unary(n-1) + [1]

"""main function"""
def numbase_to_base(n1,b1,b2):
    num_dec = base_to_dec(n1,b1)  
    return int(''.join(map(str, dec_to_base(num_dec,b2))))
        
"""Converts base number to base list"""
def base_to_dec(digits_int,base):
    digits_list = [int(x) for x in str(digits_int)]
    return base_to_dec_conversion(digits_list, base)

"""Takes a base list and converts it to another base"""
#requires list of digits and base
def base_to_dec_conversion(digits, base):
    #base case
    if len(digits) == 1:
        return digits[0]
    #recursive case
    else:
        return digits[-1] + base * base_to_dec_conversion(digits[:-1], base)


