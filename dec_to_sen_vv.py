def b10_to_b6(n):
    x = n//6
    y = n-(x*6)
    return (x*10)+y
    
def b6_to_b10(n):
    x = n//10
    y = n-(x*10)
    return (x*6)+y
