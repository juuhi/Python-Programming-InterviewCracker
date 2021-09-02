def MissingNumber(self, array, n):
        total = (n)*(n+1)//2
        suma = sum(array)
        val = total - suma
        return val
     
#  If n is not given in argument of function 

def getMissingNo(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A
