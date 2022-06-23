#SmithHW7.py

import networkx

def loadEdges(nt):
    infile = open("SmithHW7.csv","r")
    text = infile.readline()
    while text!="":
        a,b = text.strip().split(',')
        nt.add_edge(a,b)
        text = infile.readline()
    infile.close()

def findBestConnected(nt):
    
    for i in nt.nodes():
        if i!="node 1" and i!="node 2":
            bestConn = i
            maxConn = nt.degree(i)
            print(bestConn,"has a degree of",maxConn)

def main():
    nt = networkx.Graph()
    loadEdges(nt)
    print("number of nodes is:", len(nt.nodes()))
    print()
    nt.degree()
    sp = networkx.shortest_path(nt, "Kendrick Smith","John Hancock")
    print("Shortest path between Kendrick Smith and John Hancock is",sp)
    sp = networkx.shortest_path(nt, "Brian Kokensparger","Paul Revere")
    print("Shortest path between Kendrick Smith and John Hancock is",sp)
    sp = networkx.shortest_path(nt, "Nathaniel Mulliken","John Coney")
    print("Shortest path between Nathaniel Mulliken and John Coney is",sp)
    print()
    bc = networkx.betweenness_centrality(nt)
    print("Betweenness for Kendrick Smith is "+str(bc['Kendrick Smith']))
    print("Betweenness for Paul Revere is "+str(bc['Paul Revere']))
    print("Betweenness for John Coney is "+str(bc['John Coney']))
    print()
    findBestConnected(nt)
    
main()
