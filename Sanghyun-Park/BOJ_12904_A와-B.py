import sys


words = [list(sys.stdin.readline().rstrip()) for _ in range(2)]

while len(words[1]) >= len(words[0]):
    if words[1] == words[0]:
        print(1)
        break

    if words[1][-1] == 'A':
        words[1].pop()
    elif words[1][-1] == 'B':
        words[1].pop()
        words[1].reverse()
else:
    print(0)
