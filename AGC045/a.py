def list_difference(list1, list2):
    result = list1.copy()
    for value in list2:
        if value in result:
            result.remove(value)
    return result

T = int(input())
for t in range(T):
    n = input()
    t = input()
    s = input()
    a0 = [0]
    a1 = [0]
    s = s.rstrip("1")
    for i in range(len(s)):
        if s[i] == "0":
            for j in range(len(a0)):
                a0.append(int(a0[j]) ^ int(t[i*2]))
        elif s[i] == "1":
            for j in range(len(a1)):
                a1.append(int(a1[j]) ^ int(t[i*2]))
    if not list_difference(a1,a0):
        print("0")
    else:
        print("1")