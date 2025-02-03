from heapq import heappush, heappop

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = 9
        rowSet = [set() for _ in range(N)]
        colSet = [set() for _ in range(N)]
        subSqr = [set() for _ in range(N)]
        empty_cells = []

        # Initialize sets and track empty cells
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    rowSet[i].add(board[i][j])
                    colSet[j].add(board[i][j])
                    subIdx = 3 * (i // 3) + j // 3
                    subSqr[subIdx].add(board[i][j])
                else:
                    # Add empty cell to priority queue (track with fewer options first)
                    empty_cells.append((i, j))

        # Sort cells based on possible options (ascending order)
        def cell_options(cell):
            r, c = cell
            subIdx = 3 * (r // 3) + c // 3
            return [
                num for num in map(str, range(1, 10))
                if num not in rowSet[r] and num not in colSet[c] and num not in subSqr[subIdx]
            ]

        # Sort empty cells by the number of possible options
        empty_cells = sorted(empty_cells, key=lambda cell: len(cell_options(cell)))

        def solve(idx):
            if idx == len(empty_cells):
                return True  # All cells filled successfully

            r, c = empty_cells[idx]
            subIdx = 3 * (r // 3) + c // 3

            for num in cell_options((r, c)):
                # Place number
                board[r][c] = num
                rowSet[r].add(num)
                colSet[c].add(num)
                subSqr[subIdx].add(num)

                if solve(idx + 1):
                    return True

                # Backtrack
                board[r][c] = "."
                rowSet[r].remove(num)
                colSet[c].remove(num)
                subSqr[subIdx].remove(num)

            return False

        solve(0)
