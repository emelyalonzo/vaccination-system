# -*- coding: utf-8 -*-
"""Unittest for the second phase
"""


from fase2 import HealthCenter2
import unittest

class Test(unittest.TestCase):

    mark=0

    def setUp(self):
        pass
    
    def test1_searchPatients(self):
        print('\n\ttest1_searchPatients: all patients')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        result=expected.searchPatients(2021)
        self.assertEqual(result.size(),expected.size(),'FAIL: lenghts are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest1_searchPatients: was OK!!!')

    def test2_searchPatients(self):
        print('\n\ttest2_searchPatients: patients with covid')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailesCovid.tsv')
        result=oInput.searchPatients(2021,True)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest2_searchPatients: was OK!!!\n')


    def test3_searchPatients(self):
        print('\n\ttest3_searchPatients: patients with covid and year <=1950')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailesCovid1950.tsv')
        result=oInput.searchPatients(1950,True)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest3_searchPatients: was OK!!!')

        
    def test4_searchPatients(self):
        print('\n\ttest4_searchPatients: no covid, year <=1950 and 1 dosage')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailesNoCovid1950-1.tsv')
        result=oInput.searchPatients(1950,False,1)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')          
        print()
        Test.mark+=0.25
        print('\ttest4_searchPatients: was OK!!!\n')


    def test5_searchPatients(self):
        print('\n\ttest5_searchPatients: covid, year <=1950 and 0 dosage')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailesCovid1950-0.tsv')
        result=oInput.searchPatients(1950,True,0)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest5_searchPatients: was OK!!!\n')
            

    def test6_searchPatients(self):
        print('\n\ttest6_searchPatients: patients with 2 dosages')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2-2.tsv')
        result=oInput.searchPatients(2021,None,2)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest6_searchPatients: was OK!!!\n')
            

     
    def test7_searchPatients(self):
        print('\n\ttest7_searchPatients: no covid')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailesNoCovid.tsv')
        result=oInput.searchPatients(2021,False)
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest7_searchPatients: was OK!!!\n')
        
        
    def test8_searchPatients(self):
        print('\n\ttest8_searchPatients: 0 dosages')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2-0.tsv')
        result=oInput.searchPatients(2021,None,0) 
        self.assertEqual(result.size(),expected.size(),'FAIL: sizes are different')
        self.assertEqual(result,expected,'Fail: trees are not equal')            
        print()
        Test.mark+=0.25
        print('\ttest8_searchPatients: was OK!!!')
            
    def test9_vaccine(self):
        print('\n\ttest9_vaccine: patient does not exist')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        oInput_v=HealthCenter2('data/LosFrailes2.tsv')
        vaccinated=HealthCenter2('data/vaccinated.tsv')
        before_v=HealthCenter2('data/vaccinated.tsv')
        name='Ainoza'
        result=oInput.vaccine(name,vaccinated)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        node=oInput.find(name)
        self.assertIsNone(node)
        self.assertEqual(oInput,oInput_v)            
        self.assertEqual(vaccinated,before_v)            
        print()
        Test.mark+=0.25
        print('\ttest9_vaccine: was OK!!!')

    def test_10_vaccine(self):
        print('\n\ttest10_vaccine: patient with 0 dosage')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        oInput_v=HealthCenter2('data/LosFrailes2.tsv')
        vaccinated=HealthCenter2('data/vaccinated.tsv')
        vaccinated_exp=HealthCenter2('data/vaccinated.tsv')
        name='Abad'
        result=oInput.vaccine(name,vaccinated)
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.vaccine,1)            
        self.assertEqual(oInput,oInput_v)            
        self.assertEqual(vaccinated,vaccinated_exp)            
        print()
        Test.mark+=0.50
        print('\ttest10_vaccine: was OK!!!')
        
    
    def test_11_vaccine(self):
        print('\n\ttest11_vaccine: patient with 1 dosage ')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2NoFont.tsv')
        vaccinated=HealthCenter2('data/vaccinated.tsv')
        vaccinnated_exp=HealthCenter2('data/vaccinatedFont.tsv')
        name='Font'
        result=oInput.vaccine(name,vaccinated)
        self.assertTrue(result)
        node=oInput.find(name)
        self.assertIsNone(node)            
        self.assertEqual(oInput,expected)            
        node=vaccinated.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.vaccine,2)            
        self.assertEqual(vaccinated,vaccinnated_exp)           
        print()
        Test.mark+=0.75
        print('\ttest11_vaccine: was OK!!!')

    def test_12_vaccine(self):
        print('\n\ttest12_vaccine: patient with 2 dosage ')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2NoOmar.tsv')
        vaccinated=HealthCenter2('data/vaccinated.tsv')
        vaccinnated_exp=HealthCenter2('data/vaccinatedOmar.tsv')
        name='Omar'
        result=oInput.vaccine(name,vaccinated)
        self.assertIsNotNone(result)
        self.assertFalse(result)
        node=oInput.find(name)
        self.assertIsNone(node)           
        self.assertEqual(oInput,expected)            
        node=vaccinated.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.vaccine,2)            
        self.assertEqual(vaccinated,vaccinnated_exp)            
        print('\n\ttest12_vaccine: patient with 2 dosage ')
        print()
        Test.mark+=0.75
        print('\ttest12_makeAppointment: was OK!!!')
        

    def test_13_makeAppointment(self):
        print('\n\ttest13_makeAppointment: patient not exist')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFrailesCitas.tsv',False)
        name='Ainoza'
        time='15:00'
        result=oInput.makeAppointment(name,time,schedule)   
        self.assertIsNotNone(result)
        self.assertFalse(result)
        node=oInput.find(name)
        self.assertIsNone(node)
        self.assertEqual(oInput,expected)            
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.25
        print('\ttest13_makeAppointment: was OK!!!')
        

    def test_14_makeAppointment(self):
        print('\n\ttest14_makeAppointment: patient is already vaccinated')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFrailesCitas.tsv',False)
        name='Mayo'
        time='15:00'
        result=oInput.makeAppointment(name,time,schedule)   
        self.assertIsNotNone(result)
        self.assertFalse(result)
        node=oInput.find(name)
        self.assertEqual(node.elem.vaccine,2)
        self.assertEqual(oInput,expected)            
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.25
        print('\ttest14_makeAppointment: was OK!!!')

    def test_15_makeAppointment(self):
        print('\n\ttest15_makeAppointment: no free appointments')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitasFull.tsv',False)
        schedule_exp=HealthCenter2('data/LosFrailesCitasFull.tsv',False)
        name='Losada'
        time='15:00'
        result=oInput.makeAppointment(name,time,schedule)   
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(oInput,expected)            
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.50
        print('\ttest15_makeAppointment: was OK!!!')
    
    def test_16_makeAppointment(self):
        print('\n\ttest16_makeAppointment: time no right')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFrailesCitas.tsv',False)
        name='Losada'
        time='20:00'
        result=oInput.makeAppointment(name,time,schedule)   
        self.assertIsNotNone(result)
        self.assertFalse(result)
        self.assertEqual(oInput,expected)  
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.25
        print('\ttest16_makeAppointment: was OK!!!')
    
    def test_17_makeAppointment(self):
        print('\n\ttest17_makeAppointment: time is free')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada13.tsv',False)
        name='Losada'
        time='13:00'
        result=oInput.makeAppointment(name,time,schedule)    
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,time)
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.50
        print('\ttest17_makeAppointment: was OK!!!')
        
    
    def test_18_makeAppointment(self):
        print('\n\ttest18_makeAppointment: time is not free; last hour, free 5 minutes before')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada19-50.tsv',False)
        name='Losada'
        time='19:55'
        result=oInput.makeAppointment(name,time,schedule)  
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,"19:50")
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.75
        print('\ttest18_makeAppointment: was OK!!!')
        
    def test_19_makeAppointment(self):
        print('\n\ttest19_makeAppointment: time is not free; first hour, 15 minutes later')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada8-15.tsv',False)
        name='Losada'
        time='08:00'
        result=oInput.makeAppointment(name,time,schedule)   
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,"08:15")
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.75
        print('\ttest19_makeAppointment: was OK!!!')
        
     
    def test_20_makeAppointment(self):
        print('\n\ttest20_makeAppointment: time is not free; 5 before free, 5 later no free ')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada14-50.tsv',False)
        name='Losada'
        time='14:55'
        result=oInput.makeAppointment(name,time,schedule)  
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,"14:50") 
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.75
        print('\ttest21_makeAppointment: was OK!!!')

        
    def test_21_makeAppointment(self):
        print('\n\ttest_21_makeAppointment: time is not free; 5 before and 5 later are free')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada15-55.tsv',False)
        name='Losada'
        time='16:00'
        result=oInput.makeAppointment(name,time,schedule) 
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,"15:55")
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=1
        print('\ttest21_makeAppointment: was OK!!!')

    def test_22_makeAppointment(self):
        print('\n\ttest22_makeAppointment: time is not free; 5 before no free, 5 later free')
        oInput=HealthCenter2('data/LosFrailes2.tsv')
        expected=HealthCenter2('data/LosFrailes2.tsv')
        schedule=HealthCenter2('data/LosFrailesCitas.tsv',False)
        schedule_exp=HealthCenter2('data/LosFracilesCitasLosada15-10.tsv',False)
        name='Losada'
        time='15:05'
        result=oInput.makeAppointment(name,time,schedule)    
        self.assertIsNotNone(result)
        self.assertTrue(result)
        node=oInput.find(name)
        oPatient=node.elem
        self.assertEqual(oPatient.appointment,"15:10")
        self.assertEqual(oInput,expected)     
        self.assertEqual(schedule,schedule_exp)            
        print()
        Test.mark+=0.75
        print('\ttest22_makeAppointment: was OK!!!')


        
    def test_showmark(self):
        print('Total mark is ', Test.mark)

if __name__ == '__main__':
    unittest.main()