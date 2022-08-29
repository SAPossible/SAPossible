import sys

# V, L, D : 1회 / I, X, C, M : 3회
# exception : 1회 / IV - IX , XL - XC, CD - CM 같이 X

numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
exception = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

def Arabia(words):
    ret = 0
    idx = 0

    while idx < len(words):
        if len(words) > idx + 1 and words[idx:idx + 2] in exception:
            ret += exception[words[idx:idx + 2]]
            idx += 2

        else:
            ret += numbers[words[idx]]
            idx += 1

    return ret


def Roman(number):
    ret = ""

    for k in range(len(number), 0, -1):
        n = int(number[-k])

        if k == 4:
            ret += 'M' * n

        elif k == 3:
            if n == 9:
                ret += 'CM'
            elif n == 4:
                ret += 'CD'
            else:
                if n >= 5:
                    ret += 'D'
                ret += 'C' * (n % 5)

        elif k == 2:
            if n == 9:
                ret += 'XC'
            elif n == 4:
                ret += 'XL'
            else:
                if n >= 5:
                    ret += 'L'
                ret += 'X' * (n % 5)

        else:
            if n == 9:
                ret += 'IX'
            elif n == 4:
                ret += 'IV'
            else:
                if n >= 5:
                    ret += 'V'
                ret += 'I' * (n % 5)

    return ret


A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
print(Arabia(A) + Arabia(B))
print(Roman(str(Arabia(A) + Arabia(B))))