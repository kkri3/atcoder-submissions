def main():
    input() #n
    a = list(map(int, input().split()))
    prod = 1

    if 0 in a:
        print(0)
        return
    for i in a:
        prod *= i
        if prod > 1e+18:
            print(-1)
            break
    else:
        print(prod)

if __name__ == "__main__":
    main()