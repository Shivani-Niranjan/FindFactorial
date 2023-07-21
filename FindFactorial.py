'''
factorial
Input 1:
A = 4

Input 2:
A = 1


Output 1:
24

Output 2:
1
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (factorial(n-1) * n)


number = int(input())
print(factorial(number))