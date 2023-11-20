def part2(str):
    l = str.split('\n')
    res = []
    tmp = 0
    for e in l:
        if e == '':
            res.append(tmp)
            tmp = 0
        else:
            tmp += int(e)

    res = sorted(res)

    return res[-1] + res[-2] + res[-3]


if __name__ == '__main__':
    with open("elf.txt", "r") as f:
        read_content = f.read()
        print(f"Part 2 : {part2(read_content)}")
