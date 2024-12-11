import re

mul_regex = re.compile(r"mul\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)")

def main():
    file = "data/day3_1.txt"

    with open(file, "r") as f:
        text = f.read()

    total = 0
    for match in mul_regex.finditer(text):
        left = match.group("left")
        right = match.group("right")
        total += int(left) * int(right)

    print(total)


if __name__ == "__main__":
    main()
