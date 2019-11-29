from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree as mst

from scipy.sparse.csgraph import shortest_path as sp

grafo = csr_matrix([
    [0,6,6,6,0,0,0,0,0,0,0,0],
    [6,0,1,0,2,0,0,0,0,0,0,0],
    [6,1,0,2,7,0,2,0,0,0,0,0],
    [6,0,2,0,0,0,0,0,0,18,0,0],
    [0,2,7,0,0,4,0,0,0,0,0,0],
    [0,0,0,0,4,0,11,10,0,0,0,0],
    [0,0,2,0,0,11,0,22,2,0,0,0],
    [0,0,0,0,0,10,22,0,12,0,25,0],
    [0,0,0,0,0,0,2,12,0,1,16,0],
    [0,0,0,18,0,0,0,0,1,0,0,8],
    [0,0,0,0,0,0,0,25,16,0,0,3],
    [0,0,0,0,0,0,0,0,0,8,3,0]
])

arbol = mst(grafo)
print(arbol)
print(arbol.toarray().astype(int))
