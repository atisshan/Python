import sys
from heapq import heapify, heappush, heappop

def dijkstra(graph, src, dest):
    infi=sys.maxsize
    node={'A':{'cost': infi,'pred':[]},
          'B':{'cost': infi,'pred':[]},
          'C':{'cost': infi,'pred':[]},
          'D':{'cost': infi,'pred':[]},
          'E':{'cost': infi,'pred':[]},
          'F':{'cost': infi,'pred':[]},
          }
    node[src]['cost'] = 0
    visited=[]
    temp=src
    for i in range(5):
        if temp not in visited:
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    cost=node[temp]['cost'] + graph[temp][j]
                    if cost < node[j]['cost']:
                        node[j]['cost']=cost
                        node[j]['pred']=node[temp]['pred'] + list(temp)
                    heappush(min_heap,(node[j]['cost'], j))
        heapify(min_heap)
        temp=min_heap[0][1]

        
        print('Shortest distance: ' + str(node[dest]['cost']))
        print('Shortest path: ' + str(node[dest]['pred'] + list(dest)))

    if __name__ =="__main__":
        graph = {
            'A':{'B':2, 'C':4},
            'B':{'A':2, 'C':3, 'D':8},
            'C':{'A':4, 'B':3, 'E':5, 'D':2},
            'D':{'B':8, 'C':2, 'E':11},
            'E':{'C':5, 'D':11, 'F':1},
            'F':{'D':22, 'E':1}
        }

        source='A'
        destination='F'
        dijkstra(graph,source,destination)
