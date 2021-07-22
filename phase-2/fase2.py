# -*- coding: utf-8 -*-

from binarysearchtree import BinarySearchTree

import csv      
import os.path  
import queue  
import re 

def checkFormatHour(time):
    """checks if appointments follow the right format: hh:dd"""
        
    pattern = re.compile(r'\d{2}:\d{2}')
    
    if pattern.match(time):
        data=time.split(':')
        hour=int(data[0])
        minute=int(data[1])
        if hour in range(8,20) and minute in range(0,60,5):
            return True
    
    return False

def newHour(time, diferencia, despues):
    """
Calculate a new hour within these statements: 'diferencia' 
indicates the number of minutes forward or backward. if 'despues' is True, calculate 
an hour forward, in other case backward
    """
    pattern = re.compile(r'\d{2}:\d{2}')
    
    if pattern.match(time):
        data=time.split(':')
        hour=int(data[0])
        minute=int(data[1])
        hourDif = diferencia // 60
        minDif = diferencia - ((diferencia // 60) * 60)
        if despues == True:
            if minute+minDif <= 55:
                minute += minDif
                if hour <= 19:
                    hour += hourDif                
            else:
                minute += minDif-60
                if hour <= 19:
                    hour += hourDif + 1              
        else:
            if minute-minDif >= 0:
                minute -= minDif
                if hour >= 8:
                    hour -= hourDif                
            else:
                minute = 60 - (minDif - minute)                
                if hour >= 8:
                    hour -= (hourDif + 1)
        timeNew = str(hour).zfill(2)+":"+str(minute).zfill(2)
        if hour in range(8,20) and minute in range(0,60,5):
            return timeNew
        else:
            return time       
NUM_APPOINTMENTS=144

class Patient:
    def __init__(self,name,year,covid,vaccine,appointment=None):
        self.name=name
        self.year=year
        self.covid=covid
        self.vaccine=vaccine
        self.appointment=appointment     

    def setAppointment(self,time):
        """gets a string with format hour:minute"""
        self.appointment=time
        
    def __str__(self):
        return (self.name+'\t'+str(self.year)+'\t'+str(self.covid)+'\t'+
                str(self.vaccine)+'\t appointment:'+str(self.appointment))

    def __eq__(self,other):
        return  other!=None and self.name == other.name 

class HealthCenter2(BinarySearchTree):
    """this class is a subclass of a binary search tree to 
    achive a better temporal complexity of its algorithms for 
    searching, inserting o removing a patient (or an appointment)"""

    def __init__(self, filetsv=None, orderByName=True):
        """ This constructor allows to create an object instance of HealthCenter2. 
        It takes two parameters:
        - filetsv: a file csv with the information about the patients whe belong to this health center
        - orderByName: if it is True, it means that the patients should be sorted by their name in the binary search tree,
        however, if is is False, it means that the patients should be sorted according their appointments
        """
        super(HealthCenter2, self).__init__()
        if filetsv is None or not os.path.isfile(filetsv):
            self.name=''
        else: 
            order='by appointment'
            if orderByName:
                order='by name'
            self.name=filetsv[filetsv.rindex('/')+1:].replace('.tsv','')
            fichero = open(filetsv)
            lines = csv.reader(fichero, delimiter="\t")
            for row in lines:
                #print(row)
                name=row[0] #nombre
                year=int(row[1]) #año nacimiento
                covid=False
                if int(row[2])==1:          #covid:0 o 1
                    covid=True
                vaccine=int(row[3])         #número de dosis
                try:
                    appointment=row[4]
                    if checkFormatHour(appointment)==False:
                        #print(appointment, ' is not a right time (hh:minute)')
                        appointment=None       
                except:
                    appointment=None    
                objPatient=Patient(name,year,covid,vaccine,appointment)
                #name is the key, and objPatient the eleme
                if orderByName:
                    self.insert(name,objPatient)
                else:
                    if appointment:
                        self.insert(appointment,objPatient)
                    else:
                        print(objPatient," was not added because appointment was not valid!!!")
            fichero.close()

    def searchPatients(self,year=2021,covid=None,vaccine=None):    
        """
        Search for patients and includes them into a new Health Center.
        In the best case, complexity is n.
        In the worst case, complexity is n^2 if not balanced and O(n · log(n)) if balanced 
        """
        result=HealthCenter2() 
        if self._root==None:
            print('Árbol vacío')
        else:     
            q=queue.Queue()
            q.put(self._root)     
            while q.empty()==False:
                current=q.get()
                if (current.elem.year<=year and 
                    (covid == None or current.elem.covid == covid) and
                    (vaccine == None or current.elem.vaccine == vaccine)):         
                    result.insert(current.elem.name,
                                    Patient(current.elem.name,
                                            current.elem.year,
                                            current.elem.covid,
                                            current.elem.vaccine))
                if current.left!=None:
                    q.put(current.left)
                if current.right!=None:
                    q.put(current.right)       
        return result        
      
    def vaccine(self,name,vaccinated):
        """
        Simulates the vaccination of the patients whose name is provided. 
        True if the patient doesnt has any of the doses 
        False if the patient has all the doses
        If the tree is balanced, complexity is log(n)
        If not balanced, complexity is n 
        """
        paciente = self.find(name)
        if paciente == None:
            print("Paciente no existe")
            return False
        else:
            if (paciente.elem.vaccine == 0):
                print("Paciente existe y nunca ha sido vacunado")                   
                paciente.elem.vaccine = 1
                return True          
            elif (paciente.elem.vaccine == 1):
                print("Paciente existe y ya ha sido vacunado 1 vez")                
                paciente.elem.vaccine = 2
                self.remove(name)
                vaccinated.insert(name,
                                  Patient(paciente.elem.name,
                                          paciente.elem.year,
                                          paciente.elem.covid,
                                          paciente.elem.vaccine))
                return True          
            elif (paciente.elem.vaccine == 2):
                print("Paciente existe y ya ha sido vacunado 2 veces")
                self.remove(name)
                vaccinated.insert(name,
                                  Patient(paciente.elem.name,
                                          paciente.elem.year,
                                          paciente.elem.covid,
                                          paciente.elem.vaccine))
                return False            
        return None

    def makeAppointment(self,name,time,schedule):
        """
        True if the appointment is created, False if not. 
        Best case if patient doesnt exist, complexity is log(n) if balanced
        Worst case if patient does exist, O(n · log(n))
        """
        paciente = self.find(name)
        if paciente == None:
            print("Paciente no existe")
            return False
        else:
            if (paciente.elem.vaccine == 2):
                print("Paciente existe y ya ha sido vacunado 2 veces")                   
                return False
            if schedule.size() == NUM_APPOINTMENTS:
                print("No hay citas disponibles")
                return False
            if checkFormatHour(time)==False:
                print("Cita no tiene formato correcto")
                return False
            appointment = schedule.find(time)
            if appointment == None:
                print("Cita libre, se asigna a paciente")
                paciente.elem.appointment = time   
                paciente.elem.vaccine += 1                   
                schedule.insert(time,
                                Patient(paciente.elem.name,
                                        paciente.elem.year,
                                        paciente.elem.covid,
                                        paciente.elem.vaccine,
                                        paciente.elem.appointment))
                return True
            encontrado = False
            diferencia = 5
            while (encontrado == False):
                prevTime = newHour(time, diferencia, False)
                postTime = newHour(time, diferencia, True)
                prev = True
                appointment = schedule.find(prevTime)
                if appointment != None:
                    prev = False
                    appointment = schedule.find(postTime)
                if appointment == None:
                    print("Nueva cita encontrada, se asigna a paciente")
                    print("Cita original: ", time)
                    if prev == True:
                        time = prevTime
                    else:
                        time = postTime                      
                    print("Cita asignada: ", time)
                    paciente.elem.appointment = time   
                    paciente.elem.vaccine += 1                   
                    schedule.insert(time,
                                    Patient(paciente.elem.name,
                                            paciente.elem.year,
                                            paciente.elem.covid,
                                            paciente.elem.vaccine,
                                            paciente.elem.appointment))
                    encontrado = True
                    return True
                diferencia += 5
           
if __name__ == '__main__':
   
    ###Testing the constructor. Creating a health center where patients are sorted by name
    o=HealthCenter2('data/LosFrailes2.tsv')
    o.draw()
    print()

    print('Patients who were born in or before than 1990, had covid and did not get any vaccine')
    result=o.searchPatients(1990, True,0)
    result.draw()
    print()

    print('Patients who were born in or before than 1990, did not have covid and did not get any vaccine')
    result=o.searchPatients(1990, False,0)
    result.draw()
    print()

    print('Patients who were born in or before than 1990 and got one dosage')
    result=o.searchPatients(1990, None,1)
    result.draw()
    print()

    print('Patients who were born in or before than 1990 and had covid')
    result=o.searchPatients(1990, True)
    result.draw()
    print()

    ###Testing the constructor. Creating a health center where patients are sorted by name
    schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
    schedule.draw(False)
    print()

    o.makeAppointment("Perez","08:00",schedule)
    o.makeAppointment("Losada","19:55",schedule)
    o.makeAppointment("Jaen","16:00",schedule)
    o.makeAppointment("Perez","16:00",schedule)
    o.makeAppointment("Jaen","16:00",schedule)

    o.makeAppointment("Losada","15:45",schedule)
    o.makeAppointment("Jaen","08:00",schedule)

    o.makeAppointment("Abad","08:00",schedule)
    o.makeAppointment("Omar","15:45",schedule)
    
    schedule.draw(False)

    vaccinated=HealthCenter2('data/vaccinated.tsv')
    vaccinated.draw(False)

    name='Ainoza'  #doest no exist
    result=o.vaccine(name,vaccinated)
    print("was patient vaccined?:", name,result)
    print('center:')
    o.draw(False)
    print('vaccinated:')
    vaccinated.draw(False)

    name='Abad'   #0 dosages
    result=o.vaccine(name,vaccinated)
    print("was patient vaccined?:", name,result)
    print('center:')
    o.draw(False)
    print('vaccinated:')
    vaccinated.draw(False)
    
    name='Font' #with one dosage
    result=o.vaccine(name,vaccinated)
    print("was patient vaccined?:", name,result)
    print('center:')
    o.draw(False)
    print('vaccinated:')
    vaccinated.draw(False)
    
    name='Omar' #with two dosage
    result=o.vaccine(name,vaccinated)
    print("was patient vaccined?:", name,result)
    print('center:')
    o.draw(False)
    print('vaccinated:')
    vaccinated.draw(False)

