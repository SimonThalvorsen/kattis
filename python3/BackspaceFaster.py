inp = input()
out = []

for char in inp:
    out.pop() if char=="<" else out.append(char)
print("".join(out))

