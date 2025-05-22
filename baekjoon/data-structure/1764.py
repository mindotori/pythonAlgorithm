n, m = map(int, input().split())

set_n = set(input().strip() for _ in range(n))
set_m = set(input().strip() for _ in range(m))

result = set_n & set_m

print(len(result))
for name in sorted(result):
    print(name)