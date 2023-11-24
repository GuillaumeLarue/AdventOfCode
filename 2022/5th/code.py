import re


def part1(s: str) -> str:
    # game = [['Z', 'N'], ['M','C', 'D'], ['P']]
    game = [['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
            ['L', 'D', 'Z', 'Q', 'W', 'V'],
            ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
            ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
            ['Z', 'W', 'L', 'C'],
            ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
            ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
            ['D', 'P', 'J'],
            ['D', 'C', 'N', 'W', 'V']]
    l = s.split('\n')
    for e in l:
        nb2move, frm, to = re.search(r'move (\d+) from (\d+) to (\d+)', e).groups()
        tmp_l = []
        for i in range(int(nb2move)):
            a = game[int(frm) - 1].pop()
            tmp_l.insert(0, a)
        for e in tmp_l:
            game[int(to) - 1].append(e)
    res = ""
    for e in game:
        res += e[-1]
    return res


def part2(s: str) -> int:
    return 1


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        read_content = f.read()
        print(f"Part1: {part1(read_content)}")
        print(f"Part2: {part2(read_content)}")
