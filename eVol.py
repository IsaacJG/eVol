#!/usr/bin/python
from random import *

class GenerateBasePop(object):
        def __init__(self):
                self.Populate()
                for i in self.BasePop:
                        self.GenerateGCode(i)
                for i in self.BasePop:
                        self.CheckGCode(i, self.BasePop[i])
        def Populate(self):
                self.BasePop = {}
                Keys = []
                for i in range(101):
                        if i != 0:
                                Keys += [i]
                                self.BasePop[i] = 0
        def GenerateGCode(self, Key):
                for i in range(Key):
                        BaseNumber = str(randint(0,Key*2)/random())
                        BaseNumber = BaseNumber[BaseNumber.find('.')+1:]
                        RandInt = randint(0,len(BaseNumber))
                        if len(BaseNumber)/2 < RandInt:
                                GCode = BaseNumber[RandInt-5:RandInt]
                        else:
                                GCode = BaseNumber[RandInt:RandInt+5]
                        self.BasePop[Key] = GCode
        def CheckGCode(self, Key, GCode):
                if GCode == '0':
                        BaseNumber = str(randint(0,Key*2)/random())
                        BaseNumber = BaseNumber[BaseNumber.find('.')+1:]
                        RandInt = randint(0,len(BaseNumber))
                        if len(BaseNumber)/2 < RandInt:
                                GCode = BaseNumber[RandInt-5:RandInt]
                        else:
                                GCode = BaseNumber[RandInt:RandInt+5]
                        self.BasePop[Key] = GCode

                        
class KeyLife():
        def __init__(self):
                self.Population = GenerateBasePop().BasePop
        def New(self, GCode1, GCode2):
                GCode1 = list(str(GCode1))
                GCode2 = list(str(GCode2))
                NewGCode = ''
                for i in range(5):
                        Decision = random()
                        if Decision > .5:
                                NewGCode += str(GCode1[i])
                        else:
                                NewGCode += str(GCode2[i])
                Key = (len(self.Population)+1, NewGCode)
                self.Population[Key[0]] = Key[1]
        def Kill(self, Key):
                STC.AddToArchive(Key, self.Population[Key])
                self.Population.pop(Key)
        def Mutate(self, Key, Mutations=1):
                for i in range(Mutations):
                        if int(Key[0]) + int(Key[1]) + int(Key[2]) < 10:
                                if Key[0] == '9':
                                        Key = Key.replace(Key[0], '0')
                                else:
                                        Key = Key.replace(Key[0], str(int(Key[0]) + 1))
                        elif 20 > int(Key[0]) + int(Key[1]) + int(Key[2]) > 10:
                                if Key[0] == '0':
                                        Key = Key.replace(Key[0], '9')
                                else:
                                        Key = Key.replace(Key[0], str(int(Key[0]) - 1))
                        elif 20 >= int(Key[0]) + int(Key[1]) + int(Key[2]):
                                if random() > 0.5:
                                        if Key[1] == '0':
                                                Key = Key.replace(Key[1], '9')
                                        else:
                                                Key = Key.replace(Key[1], str(int(Key[1]) - 1))
                                else:
                                        if Key[1] == '9':
                                                Key = Key.replace(Key[1], '0')
                                        else:
                                                Key = Key.replace(Key[1], str(int(Key[1]) + 1))
                        print Key


class STC():
        def __init__(self):
                self.Archive = {}
                self.Time = {}
        def AddToArchive(self, Key, GCode):
                self.Archive[Key] = GCode
        def Matrix(self, Key):
                RandInt = random()
                if str(Key) in str(RandInt):
                        if Key != 0 and Key != '':
                                self.Time[Key] = RandInt
                else:
                        if not self.Time.has_key(Key):
                                self.Time[Key] = 'CALL'
kl = KeyLife()
stc = STC()
def x():
        for i in range(1000):
                for key in kl.Population.values():
                        stc.Matrix(key)
                
