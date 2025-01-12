def main():
    inp = input()
    x = {"b":0, "k":0}
    for char in inp:
        if char in x:
            x[char] += 1
    if x["b"] > x["k"]:
        print("boba")
    elif x["b"] < x["k"]:
        print("kiki")
    else:
        print("boki") if x["k"] else print("none")


if __name__ == "__main__":
    main()
