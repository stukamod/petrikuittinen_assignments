with open("testi.txt") as f:
    n = 1
    for line in f:
        print(n, line.strip())
        n += 1

