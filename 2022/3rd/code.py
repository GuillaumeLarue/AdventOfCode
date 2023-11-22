
def char2int(ch):
    if ch.isupper():
        return ord(ch) - ord('A') + 1 + 26
    else:
        return ord(ch) - ord('a') + 1



def part1(str):
    res = 0
    l = str.split('\n')
    for e in l:
        l_tmp_1 = []
        l_tmp_2 = []
        for i in range(0, len(e)//2):
            l_tmp_1.append(e[i])
        for j in range((len(e)//2), len(e)):
            l_tmp_2.append(e[j])
        l_inter = list(set(l_tmp_1) & set(l_tmp_2))
        res += char2int(l_inter[0])
    return res


def part2(str):
    res = 0
    l = str.split('\n')
    for i in range(0, len(l), 3):
        l_tmp = []
        for j in range(i, i+3):
            l_tmp_2 = []
            for k in range(0, len(l[j])):
                l_tmp_2.append(l[j][k])
            l_tmp.append(l_tmp_2)
        l_inter = list(set(l_tmp[0]) & set(l_tmp[1]) & set(l_tmp[2]))
        res += char2int(l_inter[0])
    return res


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        read_content = f.read()
        print(f"Part1 : {part1(read_content)}")
        print(f"Part2 : {part2(read_content)}")

