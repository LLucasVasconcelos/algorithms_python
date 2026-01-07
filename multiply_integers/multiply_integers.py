def multiply(a:str,b:str):
    
    n = max(len(a),len(b))
    
    if n == 1:
        return int(a)*int(b)
    n = n//2
    
    print(n)
    
    high_a =  int(a[:-n]) if len(a)>n else 0
    high_b =  int(b[:-n]) if len(b)>n else 0
    low_a = int(a[-n:])
    low_b = int(b[-n:])
    
    
    p1 = high_a*high_b
    print(high_a,"+",high_b,"=",p1)
    p2 = high_a*low_b
    print(high_a,"*",low_b,"=",p2)
    p3 = low_a*high_b
    print(low_a,"*",high_b,"=",p3)
    p4 = low_a*low_b
    print(low_a,"*",low_b,"=",p4)
    
    return 10**(2*n)*(p1)+10**n*(p2+p3)+p4
    
print(multiply("34","398"))
    
    
