t = int(input())
freq = [0] * 200005

for _ in range(t):
    n = int(input())

    a = []

    for _ in range(n):
        temp = list(map(int, input().split()))
        k = temp[0]
        bits = temp[1:]

        a.append(bits)

        for bit in bits:
            freq[bit] += 1

    found = False

    for bits in a:
        can_remove = True

        for bit in bits:
            if freq[bit] == 1:
                can_remove = False
                break

        if can_remove:
            found = True
            break

    print("YES" if found else "NO")

    # cleanup
    for bits in a:
        for bit in bits:
            freq[bit] = 0