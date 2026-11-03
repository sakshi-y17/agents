from collections import deque

start = (("C", "B", "A"), (), ())
goal = (("A", "B", "C"), (), ())

def get_moves(state):
    moves = []

    for i in range(3):
        if state[i]:
            for j in range(3):
                if i != j:
                    new_state = [list(rod) for rod in state]
                    block = new_state[i].pop()
                    new_state[j].append(block)
                    new_state = tuple(tuple(rod) for rod in new_state)

                    if new_state not in visited:
                        moves.append(new_state)

    return moves

def bfs():
    global visited

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution Found!")
            for step, s in enumerate(path):
                print("Step", step, ":", s)
            return

        for new_state in get_moves(state):
            visited.add(new_state)
            queue.append((new_state, path + [new_state]))

    print("No Solution Found")

bfs()