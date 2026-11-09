# https://www.hackerearth.com/problem/algorithm/decimal-to-binary-2-192eda4d/



# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

def binary_val(N):
    if N==0:
        return "0"
    
    binary=""
    while N>0:
        binary=str(N%2)+binary
        N=N//2
    return binary

N=int(input("Enter the number: "))
result=binary_val(N)
print(result)



# Trace for b = "1010"

# ch	decimal * 2 + int(ch)	result
# start		0
# 1	0*2 + 1	1
# 0	1*2 + 0	2
# 1	2*2 + 1	5
# 0	5*2 + 0	10

# The answer is 10, which matches the expected output.

# Why it works

# Expanding it out gives:

# ((((0*2 + 1)*2 + 0)*2 + 1)*2 + 0) = 1*2³ + 0*2² + 1*2¹ + 0*2⁰ = 8 + 0 + 2 + 0 = 10

# Each bit ends up multiplied by the correct power of 2 without you ever computing the powers yourself. That is why it is simpler than the 2**power approach.

# Complexity: O(n) time for n bits, and O(1) extra space.