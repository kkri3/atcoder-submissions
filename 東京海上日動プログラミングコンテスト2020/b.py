a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if v <= w:
  print("NO")
  exit()
print("YNEOS"[abs(a-b)/(v-w) > t::2]) 