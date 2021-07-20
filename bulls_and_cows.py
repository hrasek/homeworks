# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:55:46 2021

@author: Hosek
"""
import random
import time

## Vyhodnocuje počet správných tipů
def kolo_hry(tip):
    bulls = 0
    cows = 0
    for index,cislo in enumerate(tip):
        if int(cislo) == cislo_hadane[index]:
            bulls+=1
        elif int(cislo) in cislo_hadane:
            cows+=1
        else:
            pass
    return [bulls, cows]

## Vyhodnocuje korektnost tipu
def pravidla(tip):
    for cislo in tip:
        if not(cislo.isnumeric()):
            return False
    if len(tip) != 4:
        return False
    if len(set(tip)) != 4:
        return False
    return True


start = time.time() # zacatek mereni casu
# Úvod
print('Hi there!')
print(54*'-')
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
# Generování tipovaného čísla
cislo_hadane = []
seznam_cisel = list(range(1,10))  
for _ in range(4):
    vyber = random.randint(0,len(seznam_cisel)-1)
    cislo_hadane.append(seznam_cisel.pop(vyber))
# Samotná hra
pocet_tipu = 0
while True:
    # Tip uživatele
    pocet_tipu += 1
    tip = list(input('Enter a number: '))
    print(54*'-')
    # Vyhodnocení, zda tip odpovídá pravidlům.
    if not pravidla(tip):
        print('Your tip is against the rules.')
        print('Try again.')
        continue
    # Vyhodnocení počtu bulls and cows
    bulls, cows = kolo_hry(tip)
    # Vyhodnocení, zda došlo k výhře
    if bulls == 4:
        print("Correct, you've guessed the right number in {} guesses!".format(pocet_tipu))
        print(54*'-')
        break
    # Výpis počtu bulls and cows 
    else:
        if bulls == 1 and cows == 1:
            print('{} bull, {} cow.'.format(bulls,cows))
        elif bulls == 1:
            print('{} bull, {} cows.'.format(bulls,cows))
        elif cows == 1:
            print('{} bulls, {} cow.'.format(bulls,cows))
        else:
            print('{} bulls, {} cows.'.format(bulls,cows))
            
end = time.time() # Konec měření času
print('You finished the game in {0:.5} seconds'.format(end-start))
        