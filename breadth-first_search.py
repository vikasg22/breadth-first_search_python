class Node(object):
  def __init__(self, name):
    self.name = name
    self.adjacencyList = [] # перечисляем соседей
    self.visited = False
    self.predecessor = None # предыдущая вершина

class BreadthFirstSearch(object):

  def bfs(self, startNode):

    queue = []
    queue.append(startNode)

    startNode.visited = True

    # BFS --> queue
    # DFS --> stack BUT usually we implement it with recursion!!!
    while queue:
      actualNode = queue.pop(0)

      print('%s ' % actualNode.name)

      for n in actualNode.adjacencyList:
        if n.visited == False:
          n.visited = True # отмечаем, что вершина уже добавлена была
          queue.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node1.adjacencyList.append(node5)

node2.adjacencyList.append(node5)
node2.adjacencyList.append(node2)
node2.adjacencyList.append(node4)

bfs = BreadthFirstSearch()
bfs.bfs(node1)

