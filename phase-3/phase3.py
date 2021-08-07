# -*- coding: utf-8 -*-
"""
third phase
"""
import sys

class HealthCenter():
    def __init__(self, name = None):
        self.name=name
        
        
    def __eq__(self,other):
        return  other!=None and self.name == other.name
    
    def __str__(self):
        return self.name

class AdjacentVertex():
  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight
  
  def __str__(self):
    return '('+str(self.vertex)+','+str(self.weight)+')'
 
class Map():
    def __init__(self):
        self.centers = {}
        self.vertices = {}
    
    def addHealthCenter(self, center):
        i = len(self.centers)
        self.centers[i] = center
        self.vertices[i] = []
        
    def _getIndice(self,center):
        for index in self.centers.keys():
            if self.centers[index] == center:
                return index
        return -1
        
    def __str__(self):
        result=''
        for i in self.vertices.keys():
            result+=str(self.centers[i])+':\n'
            for adj in self.vertices[i]:
                result+='\t'+str(self.centers[adj.vertex])+', distance:'+str(adj.weight)+'\n'
        return result
       
    def addConnection(self,center1,center2,distance, directed=False):
        #print('new conexion:',pto1,pto2)
        index1=self._getIndice(center1)
        index2=self._getIndice(center2)
        if index1==-1:
            print(center1,' not found!')
            return
        if index2==-1:
            print(center2,' not found!!')
            return 
        self.vertices[index1].append(AdjacentVertex(index2,distance))
        #print('adding:',index2,index1,distancia)
        if (directed == False):
            self.vertices[index2].append(AdjacentVertex(index1,distance))

        
    def areConnected(self,center1,center2):
        index1=self._getIndice(center1)
        index2=self._getIndice(center2)
        if index1==-1:
            print(center1,' not found!')
            return
        if index2==-1:
            print(center2,' not found!!')
            return 
        
        for adj in self.vertices[index1]:
            if adj.vertex==index2:
                return adj.weight
        #print(pto1,pto2," no están conectados")
        return 0
            
    def removeConnection(self,center1,center2):
        index1=self._getIndice(center1)
        index2=self._getIndice(center2)
        if index1==-1:
            print(center1,' not found!')
            return
        if index2==-1:
            print(center2,' not found!!')
            return 
        
        for adj in self.vertices[index1]:
            if adj.vertex==index2:
                self.vertices[index1].remove(adj)
                break
                
        for adj in self.vertices[index2]:
            if adj.vertex==index1:
                self.vertices[index2].remove(adj)
                break

    def createPath(self): 
        """This function prints the vertices by dfs algorithm"""
        #print('dfs traversal:')
        # Mark all the vertices as not visited 
        visited = [False] * len(self.vertices)

        paths=[]
        for v in  self.vertices:
            if visited[v]==False:
                self._dfs(v, visited,paths)
        
        print()
        return paths
        
    def _dfs(self, v, visited,paths): 
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(self.centers[v], end = ' ') 
        paths.append(self.centers[v])
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self.vertices[v]: 
          i=adj.vertex
          if visited[i] == False: 
            self._dfs(i, visited,paths) 
            
    def printSolution(self,distances,previous,v): 
        """imprime los caminos mínimos desde v"""
        for i in range(len(self.vertices)):
          if distances[i]==sys.maxsize:
            print("There is not path from ",v,' to ',i)
          else: 
            minimum_path=[]
            prev=previous[i]
            while prev!=-1:
              minimum_path.insert(0,self.centers[prev])
              prev=previous[prev]
            
            minimum_path.append(self.centers[i])  
    
            print('Ruta mínima de:',self.centers[v],'->',self.centers[i],
                  ", distance", distances[i], ', ruta: ',  end= ' ')
            for x in minimum_path:
                print(x,end= ' ')
            print()
    
    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) with the mininum 
        distance. To do this, we see in the list distances. We only consider 
        the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
    
        #returns the vertex with minimum distance from the non-visited vertices
        for i in range(len(self.vertices)): 
          if distances[i] <= min and visited[i] == False: 
            min = distances[i] 
            min_index = i 
      
        return min_index 
    
    def dijkstra(self, v=0): 
        """"This function takes the index of a delivery point pto and 
        calculates its mininum path to the rest of vertices by using the 
        Dijkstra algoritm.""" 
        
        """ Complexity (Time): O(|E|+|V|⋅log(|V|))
            Complexity (Space): O(|A|)"""
         
        visited = [False] * len(self.vertices) 
        previous=[-1]*len(self.vertices) 
        distances = [sys.maxsize]*len(self.vertices) 
        distances[v] = 0
    
        for i in range(len(self.vertices)): 
          u = self.minDistance(distances, visited) 
          # Put the minimum distance vertex in the shortest path tree
          visited[u] = True
          
          # Update distance value of the u's adjacent vertices only if the 
          #current distance is greater than new distance and the vertex in 
          #not in the shortest path tree 
          for adj in self.vertices[u]:
            i=adj.vertex
            w=adj.weight
            if visited[i]==False and distances[i]>distances[u]+w:
              distances[i]=distances[u]+w   
              previous[i]=u       
              
        #we print the minimum path from v to the other vertices
        #self.printSolution(distances,previous,v)
        return previous,distances
 
    def minimumPath(self, start, end):
        indexStart=self._getIndice(start)
        if indexStart==-1:
            print(str(start) + " does not exist")
            return None
        indexEnd=self._getIndice(end)
        if indexEnd==-1:
            print(str(end)  + " does not exist")
            return None
        
        previous,distances=self.dijkstra(indexStart)
        
        print("Previous: " + str(previous) + " Distances: " + str(distances))    
        
        #Making the path
        minimum_path=[]
        prev=previous[indexEnd]
        while prev!=-1:
            minimum_path.insert(0,str(self.centers[prev]))
            prev=previous[prev]
            
        minimum_path.append(str(self.centers[indexEnd]))
        return minimum_path, distances[indexEnd]
    
    def bellmanFord(self, start=0): 
        
        """ Complexity (Time): O(|E|⋅|V|)
            Complexity (Space): O(|A|)"""
               
        previous = [-1]*len(self.vertices) 
        distances = [sys.maxsize]*len(self.vertices) 
        distances[start]=0
        
        for i in range(len(self.vertices)):         
            for u in range(len(self.vertices)):              
                for adj in self.vertices[u]:
                    v=adj.vertex
                    w=adj.weight
                    if distances[v]>distances[u]+w:
                        distances[v]=distances[u]+w
                        previous[v]=u  

        for u in range(len(self.vertices)):
            for adj in self.vertices[u]:             
                v=adj.vertex
                w=adj.weight
                if distances[v]>distances[u]+w:                
                    print("Ciclo negativo en v: " + str(v) + " u: " + str(u) + " w: " + str(w)+ "  distances[v]:" + str(distances[v]) + " distances[u]: " + str(distances[u]) + " w: " + str(w))
                    previous = [-1]*len(self.vertices)
                    distances = [sys.maxsize]*len(self.vertices)                    
                    return previous,distances
                      
        return previous,distances
    
    def minimumPathBF(self,start,end):
        """"Return the minimum path using the Bellman-Ford algorithm"""
        
        minimum_path=[]
        minimumDistance=0

        indexStart=self._getIndice(start)
        if indexStart==-1:
            print(str(start) + " does not exist")
            return None
        indexEnd=self._getIndice(end)
        if indexEnd==-1:
            print(str(end)  + " does not exist")
            return None
        
        previous,distances=self.bellmanFord(indexStart)
        
        print("Previous: " + str(previous) + " Distances: " + str(distances)) 
        
        if (previous[indexEnd]) != -1:
            prev=previous[indexEnd]
            while prev!=-1:
                minimum_path.insert(0,str(self.centers[prev]))                
                prev=previous[prev]
        minimum_path.append(str(self.centers[indexEnd]))
        
        minimumDistance = distances[indexEnd]
        
        return minimum_path, minimumDistance

    def minimumPathFW(self,start,end):
        """"Return the minimum path using the Floyd-Warshall algorithm"""
        
        """ Complexity (Time): O(n^3). 
            Complexity (Space): O(n^2)."""
        
        minimumDistance=0
        minimum_path=[]
        
        indexStart=self._getIndice(start)
        if indexStart==-1:
            print(str(start) + " does not exist")
            return None     
        indexEnd=self._getIndice(end)      
        if indexEnd==-1:
            print(str(end)  + " does not exist")
            return None
        
        Distances=[]
        Path=[]
        
        for i in range (0, len(self.vertices)):
            Distances.append([sys.maxsize]*len(self.vertices))
            Path.append([0]*len(self.vertices))
        
        for i in range (0, len(self.vertices)):            
            for j in range (0, len(self.vertices)):
                if (i==j):
                    Distances[i][j] = 0            
        
        for i in range(len(self.vertices)):          
            for adj in self.vertices[i]:
                j=adj.vertex
                w=adj.weight
                Distances[i][j]=w
    
        for i in range (0, len(self.vertices)):            
            for j in range (0, len(self.vertices)):
                if (i==j) or (Distances[i][j]==sys.maxsize):
                    Path[i][j]="-"
                else:
                    Path[i][j]=i 
        
        for k in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    if Distances[i][j] > (Distances[i][k]+ Distances[k][j]):
                        Distances[i][j] = Distances[i][k]+ Distances[k][j]
                        if (Path[k][j] != '-'):
                            Path[i][j] = Path[k][j]
                        
        print("____________________Matriz de Distancias (final):")
        for i in Distances:
            print(i)
            
        print("____________________Matriz de Caminos Mínimos (final):")                   
        for i in Path:
            print(i)
        
        minimumDistance = Distances[indexStart][indexEnd]
        i = indexStart
        j = indexEnd
        minimum_path.append(str(self.centers[indexEnd]))
        while (Path[i][j] != indexStart and Path[i][j] != '-'):
            minimum_path.append(str(self.centers[Path[i][j]]))
            j = Path[i][j]
        if Path[i][j] != '-':
            minimum_path.append(str(self.centers[indexStart]))
        minimum_path.reverse()
                        
        return minimum_path, minimumDistance


def test():
    m=Map()
    for c in ['A','B','C','D','E','F']:
        m.addHealthCenter(HealthCenter(c))
    

    m.addConnection(m.centers[0],m.centers[1],7)#A,B,7
    m.addConnection(m.centers[0],m.centers[2],9)#A,C,9
    m.addConnection(m.centers[0],m.centers[5],14)#A,F,14
    
    m.addConnection(m.centers[1],m.centers[2],10)#B,C,10
    m.addConnection(m.centers[1],m.centers[3],15)#B,D,15
    
    m.addConnection(m.centers[2],m.centers[3],11)#C,D,11
    m.addConnection(m.centers[2],m.centers[5],2)#C,F,2
    
    m.addConnection(m.centers[3],m.centers[4],6)#D,E,6
    
    m.addConnection(m.centers[4],m.centers[5],9)#E,F,9
       
    print()
    print("___________________________________________________________")
    print("_                         MAPA 1                          _")
    print("___________________________________________________________")  
    print()
    
    print("El grafo inicial es:")
    print(m)
    
    c1=m.centers[0]
    c2=m.centers[3]
    print(c1,c2,' are connected?:',m.areConnected(c1,c2))
    
    c2=m.centers[1]
    print(c1,c2,' are connected?:',m.areConnected(c1,c2))
    print()
    
    m.removeConnection(c1,c2)
    print("Se borra conexión entre ",c1," y ",c2)
    print()
    
    print("El nuevo grafo queda así:")
    print(m)
    print()
    
    print("Recorrido del grafo con algoritmo DFS:")
    print('createPath:',end=' ')
    ruta=m.createPath()
    #print('Ruta:',ruta)
    for r in ruta:
        print(r, end=' ')
    print()
    print()    
   
    c1=m.centers[1]
    c2=m.centers[4]    
    
    print("------------------------------------- Mapa 1")
    print("Camino mínimo desde "+str(c1)+" a " + str(c2))
    print()

    print("----------------- ALGORITMO Dijkstra -----------")
    minimum_path,d=m.minimumPath(c1,c2)   
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
    
    print("----------------- ALGORITMO Bellman-Ford -----------")
    minimum_path,d=m.minimumPathBF(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
            
    print("----------------- ALGORITMO Floyd-Warshall -----------")
    minimum_path,d=m.minimumPathFW(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
    
    c1=m.centers[0]
    c2=m.centers[4]    
    
    print("------------------------------------- Mapa 1")
    print("Camino mínimo desde "+str(c1)+" a " + str(c2))
    print()

    print("----------------- ALGORITMO Dijkstra -----------")
    minimum_path,d=m.minimumPath(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
    
    

    print("----------------- ALGORITMO Bellman-Ford -----------")
    minimum_path,d=m.minimumPathBF(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
        
    
    print("----------------- ALGORITMO Floyd-Warshall -----------")
    minimum_path,d=m.minimumPathFW(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()

    m2=Map()
    for c in ['0','1','2','3','4']:
        m2.addHealthCenter(HealthCenter(c))
    
    m2.addConnection(m2.centers[0],m2.centers[1],10,True)
    m2.addConnection(m2.centers[0],m2.centers[3],5,True)
    m2.addConnection(m2.centers[1],m2.centers[2],1,True)
    m2.addConnection(m2.centers[1],m2.centers[3],2,True)
    m2.addConnection(m2.centers[2],m2.centers[4],4,True)
    m2.addConnection(m2.centers[3],m2.centers[1],3,True)
    m2.addConnection(m2.centers[3],m2.centers[2],9,True)
    m2.addConnection(m2.centers[3],m2.centers[4],2,True)
    m2.addConnection(m2.centers[4],m2.centers[0],7,True)
    m2.addConnection(m2.centers[4],m2.centers[2],6,True)
    
    print()
    print("___________________________________________________________")
    print("_                         MAPA 2                          _")
    print("___________________________________________________________")  
    print()
    print()
    print(m2)
    
    c1=m2.centers[2]
    c2=m2.centers[1]
    
    print("------------------------------------- Mapa 2")
    print("Camino mínimo desde "+str(c1)+" a " + str(c2))
    print()

    print("----------------- ALGORITMO Dijkstra -----------")
    minimum_path,d=m2.minimumPath(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
        
    
    print("----------------- ALGORITMO Bellman-Ford -----------")
    minimum_path,d=m2.minimumPathBF(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
        
    
    print("----------------- ALGORITMO Floyd-Warshall -----------")
    minimum_path,d=m2.minimumPathFW(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
        
    
    c1=m2.centers[4]
    c2=m2.centers[1]
    
    print("------------------------------------- Mapa 2")
    print("Camino mínimo desde "+str(c1)+" a " + str(c2))
    print()

    print("----------------- ALGORITMO Dijkstra -----------")
    minimum_path,d=m2.minimumPath(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')  
    print()
    print()
    
    
    print("----------------- ALGORITMO Bellman-Ford -----------")
    minimum_path,d=m2.minimumPathBF(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()
    print()
    
    
    print("----------------- ALGORITMO Floyd-Warshall -----------")
    minimum_path,d=m2.minimumPathFW(c1,c2)
    print('Ruta mínima de:',c1,'->',c2,", distancia: ", d, ', ruta: ',end=' ')
    for p in minimum_path:
        print(p,end=' ')
    print()

if __name__ == '__main__':
    test()