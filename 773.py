class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            zero = state.index('0')
            for n in neighbors[zero]:
                new_state = list(state)
                new_state[zero], new_state[n] = new_state[n], new_state[zero]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        return -1