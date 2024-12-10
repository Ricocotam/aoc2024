from collections import Counter


def main():
    filename = "data/day1_1.txt"

    with open(filename, "r") as f:
        lines = f.readlines()

    list_a, list_b = zip(*[line.strip().split("  ") for line in lines])
    list_a = map(int, list_a)
    list_b = map(int, list_b)

    counted_b = Counter(list_b)

    total = 0
    for a in list_a:
        occ = counted_b.get(a, 0)
        total += a * occ
    print(total)


if __name__ == "__main__":
    main()

