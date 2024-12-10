

def main():
    filename = "data/day1_1.txt"

    with open(filename, "r") as f:
        lines = f.readlines()

    list_a, list_b = zip(*[line.strip().split("  ") for line in lines])

    list_a = sorted(map(int, list_a))
    list_b = sorted(map(int, list_b))

    total = 0
    for a, b in zip(list_a, list_b):
        diff = abs(a - b)
        total += diff
    print(total)


if __name__ == "__main__":
    main()

