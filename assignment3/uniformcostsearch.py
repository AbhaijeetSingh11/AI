import heapq
class graph:
    def __init__(self):
        self.graph={}

    def addEdge(self,start,end,cost):
        if start not in self.graph:
            self.graph[start]=[]
        self.graph[start].append((end,cost))
 
def usc(graph,start,goal):
    prior_q=[(0,start)]
    visited=set()

    while prior_q:
        cost,node=heapq.heappop(prior_q)
        if node in visited:
            continue
        print("visited node",node,"cost",cost)
        visited.add(node)

        if node==goal:
            print("found")
            return
        if node in graph.graph:
            for neighbour,edge_cost in graph.graph[node]:
                if neighbour not in visited:
                    heapq.heappush(prior_q,(cost+edge_cost,neighbour))

g=graph()
g.addEdge("S","A",1)
g.addEdge("S","B",5)
g.addEdge("A","G",15)
g.addEdge("B","G",10)
g.addEdge("C","G",5)
usc(g,"S","G") 