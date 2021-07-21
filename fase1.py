# -*- coding: utf-8 -*-
from dlist import DList

import csv
import os.path

""" 
Main file of the first phase
"""

class Patient:
    
    def __init__(self,name,year,covid,vaccine):
        self.name=name
        self.year=year
        self.covid=covid
        self.vaccine=vaccine
        
    def __str__(self):
        return (self.name+'\t'+str(self.year)+'\t'+
                str(self.covid)+'\t'+str(self.vaccine))


class HealthCenter(DList):
    
    def __init__(self,filetsv=None):
        super(HealthCenter, self).__init__()

        if filetsv is None or not os.path.isfile(filetsv):
            self.name=''

        else: 
            print('loading the data for the health center from the file ',
                  filetsv)
    
            self.name=filetsv.replace('.tsv','')
            tsv_file = open(filetsv)
            read_tsv = csv.reader(tsv_file, delimiter="\t")
    
            for row in read_tsv:
                name=row[0]
                year=int(row[1])
                covid=False
                
                if int(row[2])==1:
                    covid=True

                vaccine=int(row[3])
                self.addLast(Patient(name,year,covid,vaccine))
                
    def addPatient(self,patient):
        
        index = 0
        lastName = None
        nodeIt=self._head
        while nodeIt and nodeIt.elem.name<=patient.name:

            lastName = nodeIt.elem.name
            nodeIt=nodeIt.next
            index+=1    
        if (lastName!=patient.name):
            self.insertAt(index,patient)
        
    def searchPatients(self,year,covid=None,vaccine=None):
        
        nuevo_centro = HealthCenter()
        nodeIt=self._head
        while nodeIt:
            if ((nodeIt.elem.year in range(0,year+1)) and 
            (nodeIt.elem.covid==covid or covid==None) and 
            (nodeIt.elem.vaccine==vaccine or vaccine==None)):
                nuevo_centro.addLast(Patient(nodeIt.elem.name,nodeIt.elem.year,nodeIt.elem.covid,nodeIt.elem.vaccine))
            nodeIt = nodeIt.next
        return nuevo_centro
                
    
    def statistics(self):

        nodeIt= self._head
        p1,p2,p3,p4,p5,p6=0,0,0,0,0,0
        p_1950 = 0 
        pacientes = 0
        while nodeIt:
            #We don't use elif because a patient can fit in several conditions.
            if nodeIt.elem.year <= 1950:
                p_1950 += 1
                if nodeIt.elem.covid == True:
                    p2 += 1
                if nodeIt.elem.vaccine == 0:
                    p4 += 1
            if nodeIt.elem.covid == True:
                p1 += 1
            if nodeIt.elem.vaccine == 0:
                p3 += 1
            if nodeIt.elem.vaccine == 1:
                p5 += 1
            if nodeIt.elem.vaccine == 2:
                p6 += 1
            nodeIt = nodeIt.next
            pacientes += 1
        p1 = round((p1/pacientes),2)
        p2 = round((p2/p_1950),2)
        p3 = round((p3/pacientes),2)
        p4 = round((p4/p_1950),2)
        p5 = round((p5/pacientes),2)
        p6 = round((p6/pacientes),2)
        
        return p1,p2,p3,p4,p5,p6

    def merge(self,other):
 
        nuevo_centro=HealthCenter()
        nodeIt=self._head
        nodeIt2=other._head        

        while nodeIt or nodeIt2:
            
            if nodeIt != None and nodeIt2 == None:
                nuevo_centro.addLast(nodeIt.elem)
                nodeIt=nodeIt.next
                
                            
            elif nodeIt == None and nodeIt2 != None:
                nuevo_centro.addLast(nodeIt2.elem)              
                nodeIt2=nodeIt2.next
                
                                      
            elif nodeIt.elem.name <= nodeIt2.elem.name:             
                nuevo_centro.addLast(nodeIt.elem)
                if (nodeIt.elem.name == nodeIt2.elem.name):
                    nodeIt2=nodeIt2.next
                nodeIt=nodeIt.next                    
            else:
                nuevo_centro.addLast(nodeIt2.elem)                   
                nodeIt2=nodeIt2.next
                
        return nuevo_centro
        
    
    def minus(self,other):
        
        nuevo_centro=HealthCenter()
        nodeIt=self._head
        nodeIt2=other._head        

        while nodeIt or nodeIt2:
            if nodeIt != None and nodeIt2 == None:
                nuevo_centro.addLast(nodeIt.elem)
                nodeIt=nodeIt.next
                  
            elif nodeIt.elem.name != nodeIt2.elem.name:             
                nuevo_centro.addLast(nodeIt.elem)
                nodeIt=nodeIt.next       
            else:  
                nodeIt = nodeIt.next                 
                nodeIt2=nodeIt2.next
                
        return nuevo_centro
    
    def inter(self,other):

        nuevo_centro=HealthCenter()
        nodeIt=self._head
        nodeIt2=other._head        
        while nodeIt and nodeIt2:
            if nodeIt.elem.name < nodeIt2.elem.name:             
                nodeIt = nodeIt.next
            elif nodeIt2.elem.name < nodeIt.elem.name:   
                nodeIt2 = nodeIt2.next
            else:
                nuevo_centro.addLast(nodeIt.elem)
                nodeIt = nodeIt.next                   
                nodeIt2=nodeIt2.next
                
        return nuevo_centro     
    
####Main    

if __name__ == '__main__':
    gst=HealthCenter('data/LosFrailes.tsv')
    print(gst)

    