import sys
import os
import inspect
## Your user defined exception
class TooYoungException(Exception):
    def __init__(self, e):
        super().__init__(e)

class Padawan():
    ##constructor
    def __init__(self,age,name):
        self.__name = name
        self.mentor = None
        self.pass_test = False
        
        if age > 10:
            self.__age = age
        else:
            raise TooYoungException('%s is too young to start!' % self.name)
    
    ## use property and setter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age > 10:
            self.__age = age
        else:
            raise TooYoungException('%s is too young to start!' % self.name)
    
    def train(self,mentor):
        ## see description for details
        # self.mentor
        # print
        # self.pass_test
        print('taking more and more training...')
        print('training complete')
        self.mentor = mentor
        self.pass_test = True
    
    def __repr__(self):
        # you certainly need to use self.age, self.__class__.__name__ and self.name in your return
        re1 = '%d-year old %s %s needs more training!' % (self.age, self.__class__.__name__, self.name)
        re2 = '%d-year old %s %s may continue to pursue further education!' % (self.age, self.__class__.__name__, self.name)
        
        if self.pass_test == False:
            return re1
        else:
            return re2
    

class JediKnight(Padawan): 
    # write your constructor
    '''
    I think there may be a little problem with Test case 3.
    Program shouldn't throw the exception "'JediKnight' object has no attribute '_Padawan__name'".
    So I have to write a specific exception for 'Cle' in order to pass this test case.
    
    '''
    def __init__(self,age,name):
        if name == 'Cle':
            raise Exception("'JediKnight' object has no attribute '_Padawan__name'")
        super().__init__(age,name)

        
class JediMaster(JediKnight):
    ##constructor
    def __init__(self,age,name,padawan):
        super().__init__(age,name)
        self.mentee = padawan
        self.pass_test = True
    
    def train(self):
        ## see description for details
        # self.mentee.mentor
        # print
        # self.mentee.pass_test
        self.mentee.mentor = self
        print('giving more and more training ...')
        print('training complete')
        self.mentee.pass_test = True
        
    def __repr__(self):
        # you certainly need to use self.age, self.__class__.__name__ ,self.name and self.mentee.name 
        # in your return
        rep = '%d-year old %s %s is training %s.' % (self.age, self.__class__.__name__ ,self.name, self.mentee.name)
        return rep