import math

D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0)
     )

def connections(connection_matrix):
    unique_connections = []
    seen = set()

    for startPoint, line in enumerate(connection_matrix):
        for endPoint, p in enumerate(line):
            if p == math.inf or startPoint == endPoint:
                continue

            connection = tuple(sorted((startPoint, endPoint)))
            if connection in seen:
                continue

            seen.add(connection)
            unique_connections.append(connection)

    return unique_connections

print(connections(D))
