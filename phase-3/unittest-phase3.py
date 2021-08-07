# -*- coding: utf-8 -*-

import sys
import unittest
from fase3 import Map
from fase3 import HealthCenter


class Test(unittest.TestCase):
    
    def setUp(self):
        self.m=Map()
        
        for c in ['A','B','C','D','E','F']:
            self.m.addHealthCenter(HealthCenter(c))
            
        A=self.m.centers[0]
        B=self.m.centers[1]
        C=self.m.centers[2]
        D=self.m.centers[3]
        E=self.m.centers[4]
        F=self.m.centers[5]
        
        self.m.addConnection(A,B,7)#A,B,7
        self.m.addConnection(A,C,9)#A,C,9
        self.m.addConnection(A,F,14)#A,F,14
        
        self.m.addConnection(B,C,10)#B,C,10
        self.m.addConnection(B,D,15)#B,D,15
        self.m.addConnection(C,D,11)#C,D,11
        self.m.addConnection(C,F,2)#C,F,2
        self.m.addConnection(E,D,6)#E,D,6

        self.m.addConnection(E,F,9)#E,F,9
        
        #print(self.m)
        
        #-------- MAP 2 -------------------
        
        self.m2=Map()
        
        for c in ['A','B','C','D','E']:
            self.m2.addHealthCenter(HealthCenter(c))
            
        A2=self.m2.centers[0]
        B2=self.m2.centers[1]
        C2=self.m2.centers[2]
        D2=self.m2.centers[3]
        E2=self.m2.centers[4]
                      
        self.m2.addConnection(A2,B2,10,True)        #A,B,10
        self.m2.addConnection(A2,D2,5,True)         #A,D,5
        
        self.m2.addConnection(B2,C2,1,True)         #B,C,1
        self.m2.addConnection(B2,D2,2,True)         #B,D,2
        
        self.m2.addConnection(C2,E2,4,True)         #C,E,4
        
        self.m2.addConnection(D2,B2,3,True)           #D,B,3
        self.m2.addConnection(D2,C2,9,True)           #D,C,9
        self.m2.addConnection(D2,E2,2,True)           #D,E,2
        
        self.m2.addConnection(E2,A2,7,True)           #E,A,7
        self.m2.addConnection(E2,C2,6,True)           #E,C,6


        #-------- MAP 3 -------------------         

        self.m3=Map()
        
        for c in ['A','B','C']:
            self.m3.addHealthCenter(HealthCenter(c))
            
        A3=self.m2.centers[0]
        B3=self.m2.centers[1]
        C3=self.m2.centers[2]

    
        self.m3.addConnection(A3,B3,10,True)        #A,B,10
        self.m3.addConnection(A3,C3,4,True)         #A,C,4        
        
        self.m3.addConnection(B3,C3,1,True)         #B,C,1
           

        #-------- MAP 4 -------------------         

        self.m4=Map()
        
        for c in ['A','B','C']:
            self.m4.addHealthCenter(HealthCenter(c))
            
        A4=self.m2.centers[0]
        B4=self.m2.centers[1]
        C4=self.m2.centers[2]     
    
        self.m4.addConnection(A4,B4,10,True)          #A,B,10
        self.m4.addConnection(B4,C4,-15,True)         #B,C,-15        
        self.m4.addConnection(C4,A4,-7,True)          #C,A,-7                 
         
        
        
        
    def test01_areConnected(self):
        print('\n****** test01_areConnected ******************')
        A=self.m.centers[0]
        B=self.m.centers[1]
        C=self.m.centers[2]
        D=self.m.centers[3]
        E=self.m.centers[4]
        F=self.m.centers[5]


        self.assertEqual(self.m.areConnected(A,B),7)
        self.assertEqual(self.m.areConnected(B,A),7)

        self.assertEqual(self.m.areConnected(A,C),9)
        self.assertEqual(self.m.areConnected(A,F),14)
        self.assertEqual(self.m.areConnected(B,C),10)
        self.assertEqual(self.m.areConnected(B,D),15)
        
        self.assertEqual(self.m.areConnected(A,D),0)
        self.assertEqual(self.m.areConnected(A,E),0)
        self.assertEqual(self.m.areConnected(B,F),0)

        print('****** OK test01_areConnected ******************')
    
        
    def test02_removeConnection(self):
        print('\n****** test02_removeConnection ******************')
        A=self.m.centers[0]
        D=self.m.centers[3]

        self.assertEqual(self.m.areConnected(A,D),0)
        self.m.addConnection(A,D,33)                    #A,D,33
        self.assertEqual(self.m.areConnected(A,D),33)
        self.m.removeConnection(A,D)                    #A,D,33
        self.assertEqual(self.m.areConnected(A,D),0)


        print('****** OK test02_removeConnection ******************')
    
           

    def test03_createPath(self):
        print('\n****** test03_createPath ******************')
        result=self.m.createPath()
        A=self.m.centers[0]
        B=self.m.centers[1]
        C=self.m.centers[2]
        D=self.m.centers[3]
        E=self.m.centers[4]
        F=self.m.centers[5]
        dfs=[A,B,C,D,E,F]
        

        self.assertEqual(len(result),len(dfs))
        self.assertEqual(result,dfs)

        
        
        print('****** OK test03_createPath ******************')
    
    def test04_minimumPath(self):
        print('\n******  test04_minimumPath ALGORITMO dijkstra (A,E)******************')

        A=self.m.centers[0]
        E=self.m.centers[4]
        
        result,d=self.m.minimumPath(A,E)
        expepcted=['A', 'C', 'F', 'E']
        d_expected=20
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',E,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()
        
        
        result,d=self.m.minimumPath(E,A)
        expepcted=['E', 'F', 'C', 'A']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',E,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        

       
        print('****** OK test04_minimumPath ******************')

    def test05_minimumPathBF(self):
        print("\n----------------- test05_minimumPathBF ALGORITMO Bellman Ford (A,B) -----------")
        A=self.m.centers[0]
        B=self.m.centers[1]
        result,d=self.m.minimumPathBF(A,B)
        expepcted=['A','B']
        d_expected=7
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        
        
        result,d=self.m.minimumPathBF(B,A)
        expepcted=['B','A']
        d_expected=7
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',B,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()
        
        print('****** OK test05_minimumPathBF ******************')

   
    
    def test06_minimumPathBF(self):
        print("\n----------------- test06_minimumPathBF: ALGORITMO Bellman Ford  (A,E) -----------")
        A=self.m.centers[0]
        E=self.m.centers[4]
        
        result,d=self.m.minimumPathBF(A,E)
        expepcted=['A', 'C', 'F', 'E']
        d_expected=20
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',E,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        
        
        result,d=self.m.minimumPathBF(E,A)
        expepcted=['E', 'F', 'C', 'A']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',E,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()    
        
        print('****** OK test06_minimumPathBF ******************')

                
    def test07_minimumPathBF(self):
        print("\n----------------- test07_minimumPathBF: ALGORITMO Bellman Ford  (A,F) -----------")
        A=self.m.centers[0]
        F=self.m.centers[5]
        
        result,d=self.m.minimumPathBF(A,F)
        
        expepcted=['A', 'C', 'F']
        d_expected=11
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',F,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()            
        
        result,d=self.m.minimumPathBF(F,A)
        expepcted=['F', 'C', 'A']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',F,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()    
        
        print('****** OK test07_minimumPathBF ******************')

        
    def test08_minimumPathBF(self):
        print("\n----------------- test08_minimumPathBF: ALGORITMO Bellman Ford  (B,E) -----------")
        B=self.m.centers[1]
        E=self.m.centers[4]
        
        result,d=self.m.minimumPathBF(B,E)
        
        expepcted1=['B', 'D', 'E']
        expepcted2=['B', 'C', 'F', 'E']

        d_expected=21
        
        self.assertEqual(d,d_expected)
        try:
            self.assertEqual(result,expepcted1)
        except:
            self.assertEqual(result,expepcted2)
            
        print('Ruta mínima de:',B,'->',E,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()                

        
        result,d=self.m.minimumPathBF(E,B)

        expepcted1=['E', 'D', 'B']
        expepcted2=['E', 'F', 'C', 'B']

        self.assertEqual(d,d_expected)
        try:
            self.assertEqual(result,expepcted1)
        except:
            self.assertEqual(result,expepcted2)
            
        print('Ruta mínima de:',E,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()  
            
        print('****** OK test08_minimumPathBF ******************')

    def test09_minimumPathBF(self):
        print("\n----------------- test09_minimumPathBF: ALGORITMO Bellman Ford  (D,F) -----------")
        D=self.m.centers[3]
        F=self.m.centers[5]
        
        result,d=self.m.minimumPathBF(D,F)
        
        expepcted=['D', 'C', 'F']
        d_expected=13
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',D,'->',F,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()          
        
        result,d=self.m.minimumPathBF(F,D)

        expepcted=['F', 'C', 'D']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',F,'->',D,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()  
        
        print('****** OK test09_minimumPathBF ******************')

    def test10_minimumPathFW(self):
        print("\n----------------- test10_minimumPathFW ALGORITMO Floyd-Warshall (A,B) -----------")
        A=self.m.centers[0]
        B=self.m.centers[1]
        result,d=self.m.minimumPathFW(A,B)
        expepcted=['A','B']
        d_expected=7
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        
        
        result,d=self.m.minimumPathFW(B,A)
        expepcted=['B','A']
        d_expected=7
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',B,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()
        
        print('****** OK test10_minimumPathFW ******************')
    
    def test11_minimumPathFW(self):
        print("\n----------------- test11_minimumPathFW: ALGORITMO Floyd-Warshall  (A,E) -----------")
        A=self.m.centers[0]
        E=self.m.centers[4]
        
        result,d=self.m.minimumPathFW(A,E)
        expepcted=['A', 'C', 'F', 'E']
        d_expected=20
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',E,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        
        
        result,d=self.m.minimumPathFW(E,A)
        expepcted=['E', 'F', 'C', 'A']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',E,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()    
        
        print('****** OK test11_minimumPathFW ******************')
      
    def test12_minimumPathFW(self):
        print("\n----------------- test12_minimumPathFW: ALGORITMO Floyd-Warshall  (A,F) -----------")
        A=self.m.centers[0]
        F=self.m.centers[5]
        
        result,d=self.m.minimumPathFW(A,F)
        
        expepcted=['A', 'C', 'F']
        d_expected=11
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',A,'->',F,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()            
        
        result,d=self.m.minimumPathFW(F,A)
        expepcted=['F', 'C', 'A']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',F,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()    
        
        print('****** OK test12_minimumPathFW ******************')

    def test13_minimumPathFW(self):
        print("\n----------------- test13_minimumPathFW: ALGORITMO Floyd-Warshall  (B,E) -----------")
        B=self.m.centers[1]
        E=self.m.centers[4]
        
        result,d=self.m.minimumPathFW(B,E)
        
        expepcted1=['B', 'D', 'E']
        expepcted2=['B', 'C', 'F', 'E']

        d_expected=21
        
        self.assertEqual(d,d_expected)
        try:
            self.assertEqual(result,expepcted1)
        except:
            self.assertEqual(result,expepcted2)
            
        print('Ruta mínima de:',B,'->',E,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()                

        
        result,d=self.m.minimumPathFW(E,B)

        expepcted1=['E', 'D', 'B']
        expepcted2=['E', 'F', 'C', 'B']

        self.assertEqual(d,d_expected)
        try:
            self.assertEqual(result,expepcted1)
        except:
            self.assertEqual(result,expepcted2)
            
        print('Ruta mínima de:',E,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()  
            
        print('****** OK test13_minimumPathFW ******************')

    def test14_minimumPathFW(self):
        print("\n----------------- test14_minimumPathFW: ALGORITMO Floyd-Warshall  (D,F) -----------")
        D=self.m.centers[3]
        F=self.m.centers[5]
        
        result,d=self.m.minimumPathFW(D,F)
        
        expepcted=['D', 'C', 'F']
        d_expected=13
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',D,'->',F,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()          
        
        result,d=self.m.minimumPathFW(F,D)

        expepcted=['F', 'C', 'D']
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',F,'->',D,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()  
        
        print('****** OK test14_minimumPathFW ******************')

    def test15_minimumPath(self):
        print('\n******  test15_minimumPath ALGORITMO dijkstra GRAFO DIRIGIDO (C,B) y (B,A) ******************')

        C=self.m2.centers[2]
        B=self.m2.centers[1]
        A=self.m2.centers[0]        
        
        result,d=self.m2.minimumPath(C,B)
        expepcted=['C', 'E', 'A', 'D', 'B']
        d_expected=19
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',C,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()
        
        
        result,d=self.m2.minimumPath(B,A)
        expepcted=['B', 'D', 'E', 'A']
        d_expected=11
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',B,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        

       
        print('****** OK test15_minimumPath ******************')
        
    def test16_minimumPathBF(self):
        print('\n*  test16_minimumPathBF ALGORITMO Bellman-Ford GRAFO DIRIGIDO (C,B) y (B,A)')

        C=self.m2.centers[2]
        B=self.m2.centers[1]
        A=self.m2.centers[0]        
         
        result,d=self.m2.minimumPathBF(C,B)
        expepcted=['C', 'E', 'A', 'D', 'B']
        d_expected=19
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',C,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()
        
        
        result,d=self.m2.minimumPathBF(B,A)
        expepcted=['B', 'D', 'E', 'A']
        d_expected=11
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',B,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        

        print('****** OK test16_minimumPathBF ******************')

    def test17_minimumPathFW(self):
        print('\n* test17_minimumPathFW ALGORITMO Floyd-Warshall GRAFO DIRIGIDO (C,B) y (B,A)')

        C=self.m2.centers[2]
        B=self.m2.centers[1]
        A=self.m2.centers[0]        
        
        result,d=self.m2.minimumPathFW(C,B)
        expepcted=['C', 'E', 'A', 'D', 'B']
        d_expected=19
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',C,'->',B,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()

        result,d=self.m2.minimumPathFW(B,A)
        expepcted=['B', 'D', 'E', 'A']
        d_expected=11
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
        
        print('Ruta mínima de:',B,'->',A,", distancia: ", d, ', ruta: ',end=' ')
        for p in result:
            print(p,end=' ')
        print()        
       
        print('****** OK test17_minimumPathFW ******************')

    def test18_minimumPath(self):
        print('\n***** test18_minimumPath ALGORITMO dijkstra sin camino mínimo (C,A)')

        C=self.m3.centers[2]
        A=self.m3.centers[0]        
     
        result,d=self.m3.minimumPath(C,A)
        expepcted=['A']
        d_expected=sys.maxsize
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test18_minimumPath ******************')

    def test19_minimumPathBF(self):
        print('\n*****  test19_minimumPathBF ALGORITMO Bellman-Ford sin camino mínimo (C,A)')

        C=self.m3.centers[2]
        A=self.m3.centers[0]        
     
        result,d=self.m3.minimumPathBF(C,A)
        expepcted=['A']
        d_expected=sys.maxsize
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test19_minimumPathBF ******************')

    def test20_minimumPathFW(self):
        print('\n******  test20_minimumPathFW ALGORITMO Floyd-Warshall sin camino mínimo (C,A)')

        C=self.m3.centers[2]
        A=self.m3.centers[0]        
       
        result,d=self.m3.minimumPathBF(C,A)
        expepcted=['A']
        d_expected=sys.maxsize
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test20_minimumPathFW ******************')

    def test21_minimumPath(self):
        print('\n******  test21_minimumPath ALGORITMO dijkstra Ciclos negativos (C,A)')

        C=self.m4.centers[2]
        A=self.m4.centers[0]        
      
        result,d=self.m4.minimumPath(A,C)
        expepcted=['A','B','C']
        d_expected=-5
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test21_minimumPath ******************')
        
    def test22_minimumPathBF(self):
        print('\n******  test22_minimumPathBF ALGORITMO Bellman-Ford Ciclos negativos (C,A)')

        C=self.m4.centers[2]
        A=self.m4.centers[0]        
   
        result,d=self.m4.minimumPathBF(A,C)
        expepcted=['C']
        d_expected=sys.maxsize
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test22_minimumPathBF ******************')

    def test23_minimumPathFW(self):
        print('\n******  test23_minimumPathFW ALGORITMO Floyd-Warshall Ciclos negativos (C,A)')

        C=self.m4.centers[2]
        A=self.m4.centers[0]        
   
        result,d=self.m4.minimumPathFW(A,C)
        expepcted=['A','B','C']
        d_expected=-17
        
        self.assertEqual(d,d_expected)
        self.assertEqual(result,expepcted)
                
        if d==sys.maxsize:
            print("No hay camino desde ",C,' hasta ',A)
        else:
            print('Ruta mínima de:',C,'->',A,", distancia: ", d, ', ruta: ',end=' ')
            for p in result:
                print(p,end=' ')
            print()

        print('****** OK test22_minimumPathBF ******************')

if __name__ == '__main__':
    unittest.main()