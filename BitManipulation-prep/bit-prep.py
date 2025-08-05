#multiply by 2^k/ left shift
'''
x << k = x * 2^k
'''
num = 10 << 2
num = 1 << 5
#print(num)

#divide by 2^k/ right shift
'''
x >> k = x / 2^k
'''
num = 10 >> 2
num = 1 >> 5
#print(num)

#Test if kth bit is set
'''
x & (1<<k) != 0
'''
if 4 & (1 << 2) != 0:
    print("yes bit set at 2")
else:
    print("no bit set at 2")

#Set kth bit if it isn't set
'''
x |= (1<<k)
'''
num = 4 | (1<<2)
#print(num)

#Turn off kth bit
'''
x &= ~(1<<k)
'''
num = 4 & ~(1<<2)
#print(num)

#check if a number is a power of 2
'''
n > 0 and (n & (n - 1)) == 0
'''
n = 4
if n > 0 and (n&(n-1)) == 0:
    print("yes power of 2")
else:
    print("no not power of 2")

#swapping 2 variables
num1 = 2
num2 = 4
num1^=num2
num2^=num1
num1^=num2
print(num1, num2)
