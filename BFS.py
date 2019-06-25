from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def graph_search(graph):
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        print('Get name ' + person)
        if person_is_seller(person):
            print(person + ' is a seller')
            return True
        else:
            search_queue += graph[person]
    return False


graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}

graph_search(graph)
