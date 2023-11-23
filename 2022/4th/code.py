import re


def part1(s: str) -> int:
    l = s.split("\n")
    res = 0
    for e in l:
        e1, e2, e3, e4 = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', e).groups()
        if int(e1) <= int(e3) and int(e2) >= int(e4) or int(e3) <= int(e1) and int(e4) >= int(e2):
            res += 1
    return res


def part2(s: str) -> int:
    l = s.split("\n")
    res = 0
    for e in l:
        tmp_l_1 = []
        tmp_l_2 = []
        e1, e2, e3, e4 = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', e).groups()
        for i in range(int(e1), int(e2) + 1):
            tmp_l_1.append(i)
        for i in range(int(e3), int(e4) + 1):
            tmp_l_2.append(i)
        if len(list(set(tmp_l_1) & set(tmp_l_2))) != 0:
            res += 1
    return res


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        read_content = f.read()
        print(f"Part1: {part1(read_content)}")
        print(f"Part2: {part2(read_content)}")