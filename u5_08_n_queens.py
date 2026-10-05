def solve_queens(n):
    solutions = []
    cols = []

    # cols[r] = column of the queen in row r
    def safe(row, col):
        for r in range(row):
            c = cols[r]

            if c == col or abs(c - col) == abs(r - row):
                return False

        return True

    def place(row):
        if row == n:
            solutions.append(cols[:])
            return

        for col in range(n):
            if safe(row, col):
                cols.append(col)
                place(row + 1)
                cols.pop()

    # Backtracking
    place(0)

    return solutions


# Solve 4-Queens
sols = solve_queens(4)

print("4-Queens solutions:", len(sols))

for s in sols:
    print(s)

    for r in range(4):
        print(" ".join("Q" if c == s[r] else "." for c in range(4)))

    print()


# Solve 6-Queens
print("6-Queens solutions:", len(solve_queens(6)))

# Solve 8-Queens
print("8-Queens solutions:", len(solve_queens(8)))
def solve_queens(n):
    solutions = []
    cols = []

    # cols[r] = column of the queen in row r
    def safe(row, col):
        for r in range(row):
            c = cols[r]

            if c == col or abs(c - col) == abs(r - row):
                return False

        return True

    def place(row):
        if row == n:
            solutions.append(cols[:])
            return

        for col in range(n):
            if safe(row, col):
                cols.append(col)
                place(row + 1)
                cols.pop()

    place(0)
    return solutions


# 4-Queens
sols = solve_queens(4)

print("4-Queens solutions:", len(sols))

for s in sols:
    print(s)

    for r in range(4):
        print(" ".join("Q" if c == s[r] else "." for c in range(4)))

    print()


# Changed from 6 and 8 to 5 and 7
print("5-Queens solutions:", len(solve_queens(5)))
print("7-Queens solutions:", len(solve_queens(7)))
