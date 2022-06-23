import sys


def change_to_arab(num_roma):
    idx, result = 0, 0
    while idx < len(num_roma) - 1:
        if roma_to_arab[num_roma[idx]] >= roma_to_arab[num_roma[idx+1]]:
            result += roma_to_arab[num_roma[idx]]
            idx += 1
        else:
            result += roma_to_arab[num_roma[idx]+num_roma[idx+1]]
            idx += 2

    if idx < len(num_roma):
        return result + roma_to_arab[num_roma[-1]]
    return result


def change_to_roma(agg):
    idx, result = len(str(agg)) - 1, ''
    while idx >= 0:
        digit = int(str(agg)[len(str(agg)) - 1 - idx])
        if digit == 9:
            result += arab_to_roma[digit*10**idx]
        elif digit > 5:
            result += (arab_to_roma[5*10**idx] + arab_to_roma[10**idx] * (digit % 5))
        elif digit == 5:
            result += arab_to_roma[5*10**idx]
        elif digit == 4:
            result += (arab_to_roma[10**idx] + arab_to_roma[5*10**idx])
        elif digit < 4:
            result += arab_to_roma[10**idx] * (digit % 5)
        idx -= 1

    return result


arab_nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roma_nums = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
arab_to_roma = {a: r for a, r in zip(arab_nums, roma_nums)}
roma_to_arab = {r: a for a, r in zip(arab_nums, roma_nums)}

agg = sum([change_to_arab(sys.stdin.readline().rstrip()) for _ in range(2)])
print(agg)
print(change_to_roma(agg))
