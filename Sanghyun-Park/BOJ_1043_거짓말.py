import sys

N, M = map(int, sys.stdin.readline().split())
people = set(list(map(int, sys.stdin.readline().split()))[1:])
PARTIES = [set(list(map(int, sys.stdin.readline().split()))[1:]) for _ in range(M)]  # INPUT

people_before = set()  # 거짓말을 알아차릴 수 있는 사람들이 확정되었는지를 판단하기 위한 변수
while people != people_before:  # 아직 확정되지 않았다면
    people_before = people

    for PARTY in PARTIES:
        if PARTY.intersection(people):  # 거짓말을 알아차릴 수 있는 사람이 있다면
            people = people.union(PARTY)  # 합집합 연산 수행

ans = 0
for PARTY in PARTIES:
    if not PARTY.intersection(people):  # 거짓말을 알아차릴 수 있는 사람이 없다면
        ans += 1
print(ans)  # OUTPUT
