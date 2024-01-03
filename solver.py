"""Math 018"""


def solver(n):
    """returns maximum total from top to bottom
    of the triangle of variable height"""
    n = n.split("\n")

    intn = [[int(j) for j in i.split(" ")] for i in n]

    for i in reversed(range(len(intn) - 1)):
        for j in range(len(intn[i])):
            intn[i][j] += max(intn[i + 1][j], intn[i + 1][j + 1])
    return intn[0][0]
