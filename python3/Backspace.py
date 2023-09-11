inp = list(input())

def rm():
    while "<" in inp:
        for i in range(len(inp)):
            if inp[i] == "<":
                inp.pop(i)
                inp.pop(i-1)
                break
rm()
print("".join(inp))




