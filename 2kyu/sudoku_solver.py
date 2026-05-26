# There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on how many cells are given of the 81 cells of the game.
# Easy sudoku generally have over 32 givens
# Medium sudoku have around 30–32 givens
# Hard sudoku have around 28–30 givens
# Very Hard sudoku have less than 28 givens
# Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.
# A hard sudoku game means that at start no cell will have a single candidates and thus require guessing and trial and error. A very hard will have several layers of multiple candidates for any empty cell.
# Task:
# Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid and it should return a 9x9 array with the proper answer for the puzzle.
# Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9); multiple solutions for the same puzzle or the puzzle is unsolvable

def sudoku_solver(grid):
	if not _is_valid_shape(grid):
		raise ValueError("Invalid grid")

	board = [row[:] for row in grid]
	if not _is_valid_values(board):
		raise ValueError("Invalid grid")

	state = _build_state(board)
	if state is None:
		raise ValueError("Invalid grid")

	solutions = []
	_solve(board, state, solutions, limit=2)

	if not solutions:
		raise ValueError("Unsolvable puzzle")
	if len(solutions) > 1:
		raise ValueError("Multiple solutions")
	return solutions[0]


def _is_valid_shape(grid):
	if not isinstance(grid, list) or len(grid) != 9:
		return False
	for row in grid:
		if not isinstance(row, list) or len(row) != 9:
			return False
	return True


def _is_valid_values(board):
	for row in board:
		for val in row:
			if not isinstance(val, int):
				return False
			if val < 0 or val > 9:
				return False
	return True


def _build_state(board):
	rows = [set() for _ in range(9)]
	cols = [set() for _ in range(9)]
	boxes = [set() for _ in range(9)]
	for r in range(9):
		for c in range(9):
			val = board[r][c]
			if val == 0:
				continue
			b = (r // 3) * 3 + (c // 3)
			if val in rows[r] or val in cols[c] or val in boxes[b]:
				return None
			rows[r].add(val)
			cols[c].add(val)
			boxes[b].add(val)
	return (rows, cols, boxes)


def _solve(board, state, solutions, limit):
	if len(solutions) >= limit:
		return

	target = _find_best_cell(board, state)
	if target is None:
		solutions.append([row[:] for row in board])
		return

	r, c, candidates = target
	if not candidates:
		return

	rows, cols, boxes = state
	box = (r // 3) * 3 + (c // 3)
	for val in candidates:
		board[r][c] = val
		rows[r].add(val)
		cols[c].add(val)
		boxes[box].add(val)

		_solve(board, state, solutions, limit)
		if len(solutions) >= limit:
			board[r][c] = 0
			rows[r].remove(val)
			cols[c].remove(val)
			boxes[box].remove(val)
			return

		board[r][c] = 0
		rows[r].remove(val)
		cols[c].remove(val)
		boxes[box].remove(val)


def _find_best_cell(board, state):
	rows, cols, boxes = state
	best = None
	best_candidates = None
	for r in range(9):
		for c in range(9):
			if board[r][c] != 0:
				continue
			b = (r // 3) * 3 + (c // 3)
			candidates = _candidates_for(rows, cols, boxes, r, c, b)
			if best is None or len(candidates) < len(best_candidates):
				best = (r, c)
				best_candidates = candidates
				if len(best_candidates) <= 1:
					return (r, c, best_candidates)
	if best is None:
		return None
	return (best[0], best[1], best_candidates)


def _candidates_for(rows, cols, boxes, r, c, b):
	used = rows[r] | cols[c] | boxes[b]
	return [v for v in range(1, 10) if v not in used]

