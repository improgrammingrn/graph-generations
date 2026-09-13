#hyperclass

for i in range(10):
    gh.nodes.add(str(i))

petersen_edges = {
    # op
    "e0": {"0", "1"}, "e1": {"1", "2"}, "e2": {"2", "3"}, "e3": {"3", "4"}, "e4": {"4", "0"},
    # is
    "e5": {"5", "7"}, "e6": {"7", "9"}, "e7": {"9", "6"}, "e8": {"6", "8"}, "e9": {"8", "5"},
    # spokes
    "e10": {"0", "5"}, "e11": {"1", "6"}, "e12": {"2", "7"}, "e13": {"3", "8"}, "e14": {"4", "9"}
}

for edge_id, nodes in petersen_edges.items():
    gh.hyperedges[edge_id] = nodes
    gh.weights[edge_id] = [1.0]
