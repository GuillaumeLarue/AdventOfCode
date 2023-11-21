def part1(str):
    l = str.split('\n')
    res = 0

    # X, 1
    # Y, 2
    # Z, 3

    # Draw = 3
    # loss = 0
    # Win = 6

    # X, Y, Z moi
    # A, B, C adversaire

    # A, X : pierre
    # B, Y : feuille
    # C, Z : ciseaux
    for e in l:
        if e[0] == 'A':
            if e[2] == 'X':
                res += 1 + 3  # pierre pierre
            elif e[2] == 'Y':
                res += 2 + 6  # pierre feuille
            elif e[2] == 'Z':
                res += 3 + 0  # pierre ciseau
        elif e[0] == 'B':
            if e[2] == 'X':
                res += 1 + 0  # feuille pierre
            elif e[2] == 'Y':
                res += 2 + 3  # feuille feuille
            elif e[2] == 'Z':
                res += 3 + 6  # feuille ciseaux
        elif e[0] == 'C':
            if e[2] == 'X':
                res += 1 + 6  # ciseaux pierre
            elif e[2] == 'Y':
                res += 2 + 0  # ciseaux feuille
            elif e[2] == 'Z':
                res += 3 + 3  # ciseaux ciseaux
    return res


def part2(str):
    l = str.split('\n')
    res = 0

    # Draw = 3
    # loss = 0
    # Win = 6

    # X, Y, Z ce que je dois réussir
    # A, B, C adversaire

    # A : pierre
    # B : feuille
    # C : ciseaux

    # X : loose
    # Y : draw
    # Z : win
    for e in l:
        if e[0] == 'A':
            if e[2] == 'X':
                res += 0 + 3  # pierre perdre = ciseaux
            elif e[2] == 'Y':
                res += 3 + 1  # pierre égalité = pierre
            elif e[2] == 'Z':
                res += 6 + 2  # pierre gagner = feuille
        elif e[0] == 'B':
            if e[2] == 'X':
                res += 0 + 1  # feuille perdre = pierre
            elif e[2] == 'Y':
                res += 3 + 2  # feuille égalité = feuille
            elif e[2] == 'Z':
                res += 6 + 3  # feuille gagner = ciseaux
        elif e[0] == 'C':
            if e[2] == 'X':
                res += 0 + 2  # ciseaux perdre = feuille
            elif e[2] == 'Y':
                res += 3 + 3  # ciseaux égalité = ciseaux
            elif e[2] == 'Z':
                res += 6 + 1  # ciseaux gagner = pierre
    return res


if __name__ == '__main__':
    with open("pfc.txt", "r") as f:
        read_content = f.read()
        print(f"Part1 : {part1(read_content)}")
        print(f"Part2 : {part2(read_content)}")

