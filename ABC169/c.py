import math
a,b = input().split()

# int*floatは誤差が出る
# bは今回小数第2位までなので100倍(b[0]+b[2:])
# した値でint同士の計算を行い、100で割る
print((int(a)*int(b[0]+b[2:]))//100)