from collections import deque

start = ((3, 2, 1), (), ())
goal = ((), (), (3, 2, 1))

def get_moves(state):
    moves = []

    for i in range(3):
        if state[i]:
            disk = state[i][-1]

            for j in range(3):
                if i != j:
                    if not state[j] or state[j][-1] > disk:
                        new_state = [list(rod) for rod in state]
                        new_state[i].pop()
                        new_state[j].append(disk)

                        moves.append(tuple(tuple(rod) for rod in new_state))

    return moves

def bfs():
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution Found!")

            for step, s in enumerate(path):
                print("Step", step, ":", s)

            print("Total Moves:", len(path) - 1)
            return

        for new_state in get_moves(state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No Solution Found")

bfs()