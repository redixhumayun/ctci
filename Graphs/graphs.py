import pdb

class Graph():
    def __init__(self, graph_dict=None):
        if graph_dict:
            self.__graph_dict = graph_dict

    def getAdjNodes(self, node):
        return self.__graph_dict[node]

    def buildProjects(self, projects, dependencies):
        projectOrder = []
        while projects:
            for project in projects:
                if project in projectOrder:
                    return False
                current = self.__graph_dict[project]
                if not current['incoming']:
                    children = current['outgoing']
                    self.removeDependencies(project, children)
                    projectOrder.append(project)
                    projects.remove(project)
        print(projectOrder)

    def removeDependencies(self, project, children):
        for child in children:
            self.__graph_dict[child]['incoming'].remove(project)



if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    nodes = {}
    for project in projects:
        nodes[project] = {
                'outgoing': [], 'incoming': []
            }
        for dep in dependencies:
            if project == dep[0]:
                nodes[project]['outgoing'].append(dep[1])
            if project == dep[1]:
                nodes[project]['incoming'].append(dep[0])

    graph = Graph(nodes)
    graph.buildProjects(projects, dependencies)
