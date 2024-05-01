import networkx as nx

# defining the full_wpts for my graph
wpts = [
            ("MOD", "PTW", 30),
            ("PTW", "BRIG", 50),
            ("BRIG", "DUP", 45),
            ("DUP", "CTR", 25),
            ("CTR", "MOD", 35),
            ("MOD", "OPK", 75),
            ("ACL", "MOD", 27),
            ("KBR", "BRIG", 40),
            ("MOD", "YIT", 12),
            ("OPK", "PTW", 33)]

hold_entry_points = [
    ("KBR", "HOLD_ENTER", 10),
    ("OPK", "HOLD_ENTER", 10),
    ("HOLD_ENTER", "HOLD_EXIT", 15)
]

# aircraft must pass through these points to go to their desired runway
runway_entry_points = [
    ("BRIG", "RWY-27L", 10),
    #("YIT", "27L", 12),
    #("DUP", "RWY-09R", 8),
    ("BRIG", "RWY-35", 5),
    ("PTW", "RWY-17", 12),

    # entering runway through hold point
    ("HOLD_EXIT", "RWY-27L", -10),
    ("HOLD_EXIT", "RWY-09R", -10),
    ("HOLD_EXIT", "RWY-35", -10),
    ("HOLD_EXIT", "RWY-17", -10)
]

full_wpts = wpts.copy()
full_wpts.extend(runway_entry_points)

kphl_graph = nx.Graph()

for start, end, cost in full_wpts:
    kphl_graph.add_edge(start, end, weight=cost)













