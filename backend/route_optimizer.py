import networkx as nx

# ==================================
# BUS STOP GRAPH
# ==================================

G = nx.Graph()

bus_stops = [
    "Majestic",
    "KR Market",
    "Lalbagh",
    "Jayanagar",
    "BTM",
    "Silk Board",
    "Electronic City"
]

# distance(km), traffic_score, occupancy_score

edges = [

    ("Majestic", "KR Market", 2, 1, 2),

    ("KR Market", "Lalbagh", 3, 2, 1),

    ("Lalbagh", "Jayanagar", 4, 1, 2),

    ("Jayanagar", "BTM", 3, 2, 2),

    ("BTM", "Silk Board", 4, 3, 3),

    ("Silk Board", "Electronic City", 6, 2, 2),

    ("Majestic", "Lalbagh", 5, 3, 2),

    ("KR Market", "Jayanagar", 6, 2, 3),

    ("BTM", "Electronic City", 8, 1, 1)
]

# ==================================
# COST FORMULA
# ==================================

for u, v, distance, traffic, occupancy in edges:

    cost = (
        distance * 0.4 +
        traffic * 0.3 +
        occupancy * 0.3
    )

    G.add_edge(
        u,
        v,
        weight=cost,
        distance=distance,
        traffic=traffic,
        occupancy=occupancy
    )

# ==================================
# DIJKSTRA
# ==================================

def dijkstra_route(source, destination):

    path = nx.dijkstra_path(
        G,
        source,
        destination,
        weight="weight"
    )

    cost = nx.dijkstra_path_length(
        G,
        source,
        destination,
        weight="weight"
    )

    return path, round(cost, 2)

# ==================================
# ASTAR
# ==================================

def heuristic(a, b):
    return 1

def astar_route(source, destination):

    path = nx.astar_path(
        G,
        source,
        destination,
        heuristic=heuristic,
        weight="weight"
    )

    cost = nx.astar_path_length(
        G,
        source,
        destination,
        heuristic=heuristic,
        weight="weight"
    )

    return path, round(cost, 2)

# ==================================
# TRAVEL TIME
# ==================================

def estimate_time(path):

    total_distance = 0

    for i in range(len(path)-1):

        total_distance += G[
            path[i]
        ][
            path[i+1]
        ]["distance"]

    speed = 25

    time = (total_distance / speed) * 60

    return round(time)

# ==================================
# OCCUPANCY STATUS
# ==================================

def route_occupancy(path):

    values = []

    for i in range(len(path)-1):

        values.append(
            G[path[i]][path[i+1]]
            ["occupancy"]
        )

    avg = sum(values)/len(values)

    if avg < 1.5:
        return "Low"

    elif avg < 2.5:
        return "Moderate"

    return "High"