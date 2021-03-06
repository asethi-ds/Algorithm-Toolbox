"""
need to check both direction, because the blocks can try to trap source or destination
max block area is (1 + 199) * 199 / 2 = 19900
0 <= blocked.length <= 200

1   OOO...OX
2   OOO...X
.   ...
199 OX
200 X

199 rows
first row contains 199 O
Row 199 contains 1 O

Enclosed O: (199 + 1) * 199 / 2
"""

def isEscapePossible(self, blocked, source, target):
    blocked = set(map(tuple, blocked))

    def dfs(x, y, target, seen):
        if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
        seen.add((x, y))
        if len(seen) > 20000 or [x, y] == target: return True
        return dfs(x + 1, y, target, seen) or \
            dfs(x - 1, y, target, seen) or \
            dfs(x, y + 1, target, seen) or \
            dfs(x, y - 1, target, seen)
    return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())


def isEscapePossible(self, blocked, source, target):
    blocked = {tuple(p) for p in blocked}

    def bfs(source, target):
        bfs, seen = [source], {tuple(source)}
        for x0, y0 in bfs:
            for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = x0 + i, y0 + j
                if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                    if [x, y] == target: return True
                    bfs.append([x, y])
                    seen.add((x, y))
            if len(bfs) == 20000: return True
        return False
    return bfs(source, target) and bfs(target, source)
