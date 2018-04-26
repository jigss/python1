startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))
result = map(fib, range(startNumber, endNumber))#print fibonaci series
sum1 = result[-1] + result[-2] + result[-3] # last 3 number add.
print (sum1)
