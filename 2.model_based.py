from collections import deque

grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

visited = set()

def model_based_agent(start, goal, grid):
    queue = deque([start])
    parent = {start: None}
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            new_position = (nx, ny)

            if 0 <= nx < 4 and 0 <= ny < 4:
                if grid[nx][ny] == 0 and new_position not in visited:
                    visited.add(new_position)
                    parent[new_position] = (x, y)
                    queue.append(new_position)

    return None

path = model_based_agent(start, goal, grid)

if path:
    print("Goal Reached!")
    for position in path:
        print(position)
    print("Total Moves:", len(path) - 1)
else:
    print("Goal Cannot Be Reached")