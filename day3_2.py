import re

mul_regex = re.compile(r"mul\((?P<left>\d{1,3}),(?P<right>\d{1,3})\)")
do_regex = re.compile(r"do\(\)")
dont_regex = re.compile(r"don't\(\)")

def main():
    file = "data/day3_1.txt"

    with open(file, "r") as f:
        text = f.read()

    dos = do_regex.finditer(text)
    donts = dont_regex.finditer(text)

    dos_n_donts = sorted([*dos, *donts], key=lambda x: x.span()[0])
    next_do_dont = 0
    do = True
    theresnext = True

    total = 0
    for match in mul_regex.finditer(text):
        if theresnext and match.span()[0] > dos_n_donts[next_do_dont].span()[0]:
            do_dont_match = dos_n_donts[next_do_dont]
            do = do_dont_match.re.pattern == do_regex.pattern

            next_do_dont += 1

            if next_do_dont >= len(dos_n_donts):
                theresnext = False

        if do:
            left = match.group("left")
            right = match.group("right")
            total += int(left) * int(right)

    print(total)


if __name__ == "__main__":
    main()
