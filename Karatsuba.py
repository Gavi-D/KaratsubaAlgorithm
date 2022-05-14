import math

global counts
counts = 0

def karatsuba(n1, n2):
    global counts #counter to keep track of number of recursive calls
    length1 = len(str(n1)) #number of digits in n1
    length2 = len(str(n2)) #number of digits in n2
    length = max(length1, length2)
    m = (length//2) #just in case n1 and n2 have different number of digits, we will split the numbers up by the largest number of digits (divided by 2 (floor))
    
    if n1<10 or n2<10:
        return (n1*n2) #if we recieve single digits (just return the multiplication of those digits)
    
    else:
        #split of n1 into a and b
        a = n1//(10**m)
        b = n1%(10**m)

        #split of n2 into a and b
        c = n2//(10**m)
        d = n2%(10**m)

        ac = karatsuba(a, c) #multiplying a and c using Karatsuba
        counts += 1 #Karatsuba called! increase counter by 1
        #print(ac)
 
        bd = karatsuba(b, d) #multiplying b and d using Karatsuba
        counts += 1 #Karatsuba called! increase counter by 1
        #print(bd)
    
        ad_bc = karatsuba(a+b, c+d) #using Karatsuba to find (a+b) + (c+d)
        counts += 1 #Karatsuba called! increase counter by 1
        #print(ad_bc)
        ad_bc_final = ad_bc - ac - bd  #ad*bc = (a+b)*(c+d) - ac - bc
        #print(ad_bc_final)
    
    #return((ac*(10**(2*m))) + ((ad_bc_final)*(10**(m))) + bd) #final return statement (formula for Karatsuba) for answer to n1*n2
    return counts

print(karatsuba(9999999999999999999999999999999999999999999999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999))