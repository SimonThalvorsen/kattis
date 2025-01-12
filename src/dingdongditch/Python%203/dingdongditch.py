def main():
    _ = input()
    h = sorted(int(x) for x in input().split())
    b = (int(x) for x in input().split())

    cum_sum = [0] * (len(h) + 1)
    for i in range(1, len(h) + 1):
        cum_sum[i] = cum_sum[i - 1] + h[i - 1]

    for e in b:
        print(cum_sum[e])

if __name__ == "__main__":
    main()
