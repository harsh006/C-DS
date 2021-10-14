import sys


#Graph as a class
class Graph:
	def __init__(self, edges, N):

		#Initialising a Adjacency list.
		self.adjList = [[] for _ in range(N)]
		for edge in edges:
			self.adjList[edge[0]].append([edge[1],edge[2]]) #appending the destination node and its weigth as a list


#Using bellman Ford algorithm to find longest path from single source
def longDist(graph, source, N):
	cost = [-1e9] * N  #Initializing cost as a very small number.(as we have to find longest path)
	cost[source] = 1

	for i in range(N):
		# relax the cost of its adjacent vertices
		v = i

		for e in graph.adjList[v]:
			u = e[0] # Destination node
			w = e[1] # weight of the path

			#checking if the cost from v-> u is more than the previous cost
			if cost[v] != -1e9 and cost[v]*w > cost[u]: 
				cost[u] = cost[v]*w  #updating cost for u Node

	su =0
	for i in range(N):
		su += cost[i]
		print("dist", (source, i), "=", (cost[i]))
	print("Sum of quality scores is: ", su)


# Directed Acyclic Graph - 
edges = [
			[0, 1, 9], #s->a, with weight 9
			[6, 7, 1], #f->g, with weight 1
			[1, 2, 1], #a->b, with weight 1
			[0, 3, 1], #s->c, with weight 1
			[1, 4, 1], #a->d, with weight 1
			[2, 5, 1], #b->e, with weight 1
			[3, 4, 1], #c->d, with weight 1
			[3, 6, 9], #c->f, with weight 9
			[4, 5, 9], #d->e, with weight 9
			[4, 7, 9], #d->g, with weight 9
			[5, 8, 9], #e->t, with weight 9
			[7, 8, 1] #g->t, with weight 1
		]
graph = Graph(edges, 9) # Graph with edges as "edges" and 9 nodes

#Below function gets us longest distance from source "s", i.e--> 0 to other nodes in graph
longDist(graph, 0, 9)






