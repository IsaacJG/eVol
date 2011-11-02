#!/usr/bin/python

from random import *

class generate_base_pop(object):
    def __init__(self):
        self.populate()
        for i in self.base_pop:
            self.generate_gcode(i)
        for i in range(2):
            for i in self.base_pop:
                self.check_gcode(i, self.base_pop[i])
    def populate(self):
        self.base_pop = {}
        for i in range(101):
            if i != 0:
                self.base_pop[i] = 0
    def generate_gcode(self, key):
        for i in range(key):
            base_number = str(randint(0, key*2)/random())
            base_number = base_number[base_number.find('.')+1:]
            rint = randint(0, len(base_number))
            if len(base_number)/2 < rint:
                gcode = base_number[rint-5:rint]
            else:
                gcode = base_number[rint:rint+5]
            self.base_pop[key] = gcode
    def check_gcode(self, key, gcode):
        if gcode == '0':
            base_number = str(randint(0, key*2)/random())
            base_number = base_number[base_number.find('.')+1:]
            rint = randint(0, len(base_number))
            if len(base_number)/2 < rint:
                gcode = base_number[rint-5:rint]
            else:
                gcode = base_number[rint:rint+5]
            self.base_pop[key] = gcode
class key_life():
    def __init__(self):
        self.population = generate_base_pop().base_pop
    def new(self, gcode1, gcode2):
        gcode1 = list(str(gcode1))
        gcode2 = list(str(gcode2))
        new_gcode = ''
        for i in range(5):
            decision = random()
            if decision > .5:
                new_gcode += str(gcode1[i])
            else:
                new_gcode += str(gcode2[i])
        key = (len(self.population)+1, new_gcode)
        self.population[key[0]] = key[1]
    def kill(self, key):
        stc.add_to_archive(key, self.population[key])
        self.population.pop(key)
    def mutate(self, key, mutations=1):
        for i in range(mutations):
            rint = random()
            if rint < .3:
                left = key[randint(0, 3)]
                right = key[randint(0, 3)]
                if left != right:
                    key = ustr(key).replace(left, right)
                    key = ustr(key).replace(right, left)
                print key, 'SW'
            elif .3 < rint < .5:
                left = key[randint(0, 3)]
                right = str(randint(0, 9))
                key = ustr(key).replace(left, right)
                print key, 'S'
            elif .5 < rint < .7:
                for i in range(3):
                    right = str(randint(0, 9))
                    key = ustr(key).replace(key[i], right)
                print key, 'R'
            else:
                pass
        return key
class stimec():
    def __init__(self):
        self.archive = {}
        self.time = {}
    def add_to_archive(self, key, gcode):
        self.archive[key] = gcode
    def matrix(self, key):
        rint = random()
        if str(key) in str(rint):
            if key != 0 and key != '':
                self.time[key] = rint
                kl.mutate(key)
        else:
            if not self.time.has_key(key):
                self.time[key] = 'CALL'
    def alt_matrix(self, n, key):
        rint = random()
        if self.time.has_key(key):
            if key != 0 and key != '':
                self.time[key] = rint
                kl.population[n] = kl.mutate(key)
        else:
            self.time[key] = 'CALL'
def life(time=365):
    for i in range(time):
        for key in kl.population.values():
            stc.matrix(key)
def alt_life():
    while True:
        n = 0
        while n < 100:
            n+=1
            for key in kl.population.values():
                stc.alt_matrix(n, key)
##        for key in kl.population.values():
##            stc.alt_matrix(key)
kl = key_life()
stc = stimec()
