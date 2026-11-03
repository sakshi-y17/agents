import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_moves(state):
    moves = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    directions = [-3, 3, -1, 1]

    for move in directions:
        new = zero + move

        if 0 <= new < 9:
            if abs(new // 3 - row) + abs(new % 3 - col) == 1:
                temp = list(state)
                temp[zero], temp[new] = temp[new], temp[zero]
                moves.append(tuple(temp))

    return moves

def a_star():
    open_list = [(heuristic(start), 0, start, [start])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            print("Solution Found!")
            for step in path:
                print(step)
            print("Total Steps:", g)
            return

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_moves(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state)
                heapq.heappush(open_list, (new_f, new_g, next_state, path + [next_state]))

    print("No Solution Found")

a_star()