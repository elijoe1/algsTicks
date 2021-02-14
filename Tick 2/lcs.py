def table(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return []

    tbl = [[0 for j in range(len(s2))] for i in range(len(s1))]
    tbl[0][0] = 1 if s1[0] == s2[0] else 0
    for i in range(1, len(s1)):
        tbl[i][0] = 1 if s1[i] == s2[0] else tbl[i-1][0]
    for j in range(1, len(s2)):
        tbl[0][j] = 1 if s1[0] == s2[j] else tbl[0][j-1]

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if not (i == 0 and j == 0):
                tbl[i][j] = tbl[i-1][j-1] + 1 if s1[i] == s2[j] else max(tbl[i-1][j], tbl[i][j-1])

    return tbl


def match_length(tbl):
    if len(tbl) == 0:
        return 0
    return tbl[len(tbl) - 1][len(tbl[0]) - 1]


def match_string(s1, s2, tbl):
    if match_length(tbl) == 0:
        return ""
    letters = ""
    i = len(tbl) - 1
    j = len(tbl[0]) - 1
    while i > 0 and j > 0:
        if s1[i] == s2[j]:
            letters = s1[i] + letters
            i -= 1
            j -= 1
        else:
            if tbl[i-1][j] > tbl[i][j-1]:
                i -= 1
            elif tbl[i-1][j] == tbl[i][j-1]:
                i -= 1
            else:
                j -= 1

    if tbl[i][j] == 1:
        if i == 0:
            letters = s1[0] + letters
        else:
            letters = s2[0] + letters

    return letters
