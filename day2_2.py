

def assert_increasing(report, allow_error=False):
    for (i, current_level), next_level in zip(enumerate(report[:-1]), report[1:]):
        if -3 <= current_level - next_level <= -1:
            continue
        else:
            if allow_error:
                remove_next_valid = do_report(report[:i+1] + report[i+2:], allow_error=False)
                remove_current_valid = do_report(report[:i] + report[i+1:], allow_error=False)
                return remove_next_valid or remove_current_valid
            return False
    return True

def assert_decreasing(report, allow_error=False):
    for (i, current_level), next_level in zip(enumerate(report[:-1]), report[1:]):
        if 1 <= current_level - next_level <= 3:
            continue
        else:
            if allow_error:
                remove_next_valid = do_report(report[:i+1] + report[i+2:], allow_error=False)
                remove_current_valid = do_report(report[:i] + report[i+1:], allow_error=False)
                return remove_next_valid or remove_current_valid
            return False
    return True


def do_report(report, allow_error=False):
    if report[0] > report[1]:
        return assert_decreasing(report, allow_error)
    return assert_increasing(report, allow_error)


def main():
    filename = "data/day2_1.txt"

    with open(filename, "r") as f:
        reports = f.readlines()

    total = 0
    for i, report in enumerate(reports):
        report_levels = list(map(int, report.strip().split(" ")))
        valid = do_report(report_levels, allow_error=True)
        if not valid:
            valid = do_report(report_levels[1:], allow_error=False)
        total += valid
    print(total)


if __name__ == "__main__":
    main()
