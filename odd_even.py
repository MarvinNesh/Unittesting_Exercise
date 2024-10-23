def even(n):
   
    even_n=[]
    for i in n:
        if i %2==0:
            i=str(i)
            even_n.append(i)
    return(",".join(even_n))


def odd(n):
    odd_n=[]
    for i in n:
        if i%2!=0:
            i=str(i)
            odd_n.append(i)
    return(",".join(odd_n))

