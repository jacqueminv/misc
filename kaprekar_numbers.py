'''

Wolfram’s MathWorld describes Kaprekar numbers like this:

Consider an n-digit number k. Square it and add the right n digits to
the left n or n-1 digits. If the resultant sum is k, then k is called
a Kaprekar number. For example, 9 is a Kaprekar number since 92 = 81
and 8 + 1 = 9 and 297 is a Kaprekar number since 2972 = 88209 and 88 +
209 = 297.

'''

def is_kaprekar(number):
    squared = str(number ** 2)
    n = len(str(squared))
    return int(squared[n/2:]) + int(squared[:n/2]) == number

for i in range(4, 1000):
    if is_kaprekar(i):
        print i, 'is a kaprekar'
