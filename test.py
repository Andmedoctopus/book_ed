import BFS


def test_graph_search():
    graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"],
             "anuj": [], "peggy": [], "thom": [], "jonny": []}
    assert (BFS.graph_search(graph)) == 'thom', "Should return thom"


if __name__ == "__main__":
    test_graph_search()
    print("All test passed")
