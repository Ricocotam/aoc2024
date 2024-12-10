

def assert_increasing(report):
    for current_level, next_level in zip(report[:-1], report[1:]):
        if -3 <= current_level - next_level <= -1:
            continue
        else:
            return False
    return True

def assert_decreasing(report):
    for current_level, next_level in zip(report[:-1], report[1:]):
        if 1 <= current_level - next_level <= 3:
            continue
        else:
            return False
    return True



def main():
    filename = "data/day2_1.txt"

    with open(filename, "r") as f:
        reports = f.readlines()

    total = 0
    for report in reports:
        report_levels = list(map(int, report.split(" ")))

        if report_levels[0] > report_levels[1]:
            valid = assert_decreasing(report_levels)
        else:
            valid = assert_increasing(report_levels)

        total += valid

    print(total)


if __name__ == "__main__":
    main()
