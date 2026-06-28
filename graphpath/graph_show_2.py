import math

from matplotlib.lines import Line2D


vertex = (
    (0, 1),
    (1, 1),
    (0.5, 0.8),
    (0.1, 0.5),
    (0.8, 0.2),
    (0.4, 0)
)

vx = [v[0] for v in vertex]
vy = [v[1] for v in vertex]

def show_graph2(connectivity_matrix, ax, best):
    connections = getConnections(connectivity_matrix)
    for index, connection in enumerate(connections):
        x_1 = vertex[connection[0]][0]
        y_1 = vertex[connection[0]][1]
        x_2 = vertex[connection[1]][0]
        y_2 = vertex[connection[1]][1]
        ax.add_line(Line2D((x_1, x_2), (y_1, y_2), color='#aaa'))

        ax.annotate(
            text=connection[0],
            xy=(x_1, y_1),  # Pulls index 0 from your input data arrays
            xytext=(0, 12),  # Pushes the text 12 pixel points straight up
            textcoords="offset points",  # Guarantees the offset stays fixed during zoom
            ha="center",  # Centers text box over the start point
            va="bottom",  # Keeps text baseline sitting on top of offset
            color="purple",
            fontsize=11,
            weight="bold"
        )
    if last iteration

    #how can I get last item in connections
    startV = 0
    for i, v in enumerate(best):
        if i == 0:
            continue

        prev = startV
        v = v[:v.index(i)+1]
        for j in v:
            ax.add_line(Line2D((vertex[prev][0], vertex[j][0]), (vertex[prev][1], vertex[j][1]), color='r'))
            prev = j

    ax.plot(vx, vy, ' ob', markersize=15)


def getConnections(connection_matrix):
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
