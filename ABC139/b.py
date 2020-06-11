a, b = map(int, input().split())
unused = 1
tap_num = 0
while not unused >= b:
  unused += a-1
  tap_num += 1
print(tap_num)