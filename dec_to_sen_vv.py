def dec_to_sen(n):
    x = n//6
    y = n-(x*6)
    return (x*10)+y
    
def sen_to_dec(n):
    x = n//10
    y = n-(x*10)
    return (x*6)+y
