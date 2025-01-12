def main():
    c = 0
    i = input()
    l = 0
    r = i.count("<")
    for e in i:
        if e == "<":
            c += r * l
            r -= 1
            l = 0
        if e == ">":
            l += 1
    print(c)

if __name__ == "__main__":
    main()
