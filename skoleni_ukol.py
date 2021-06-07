import sys
'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
jmeno = input('Zadejte sve jmeno: ')
heslo = input('Zadejte sve heslo: ')
users = {'user': ['bob','ann','mike','liz'], 'password': ['123','pass123','password123','pass123']}
if not((jmeno in users['user']) and (users['password'][users['user'].index(jmeno)] == heslo)):
    print('Zadali jste špatné jméno nebo heslo. Program bude ukončen.')
    sys.exit()
print(30*'-')
print('Vítejte v aplikace', jmeno)
print('Máte na výběr z', len(TEXTS), 'textů k analýze.')
print(30*'-')
cislo_textu = input('Zadejte číslo v rozsahu 1 až 3 k výběru odpovídajícího textu: ')

if not ((cislo_textu.isdigit()) and (int(cislo_textu) - 1) in range(len(TEXTS))):
    print('Zadali jste špatné číslo, nebo jste nezadali číslo. Program bude ukončen.')
    sys.exit()
seznam_slov = TEXTS[int(cislo_textu) - 1].lstrip('\n').split()

pocet_slov = len(seznam_slov)
title_case = 0
upper_case = 0
lower_case = 0
nume = 0
suma = 0

delka = dict()
for slovo in seznam_slov:
## Řešení počtu slov malým písmem atd... 
    if slovo.isdigit():
        nume += 1
        suma+=int(slovo)
    elif slovo.isupper():

       upper_case+=1
       title_case+=1
    elif slovo.islower():
        lower_case+=1
    else:
        title_case+=1
    if len(slovo) in delka.keys():

        delka[len(slovo)] = int(delka[len(slovo)]) + 1

    else:
        delka.setdefault(len(slovo), 1)
delky = sorted(list(delka.keys()))

## Délka slov 
print(30*'-')  
print('Ve vybraném textu je', pocet_slov, 'slov')
print('Text obsahuje', title_case, 'slov začínajících velkým písmenem.')
print('Text obsahuje', upper_case, 'slov psaných velkými písmeny.')
print('Text obsahuje', lower_case, 'slov psaných malými písmeny.')
print('Text obsahuje', nume, 'čísel.')
print('Suma čísel v textu je', suma)
print(30*'-')  
print('LEN | OCCURENCES   |  NR.')
print(30*'-')  
for cislo in delky:
#    print('{:>3}|{:<4}{:<30} '.format(cislo,'*'*delka[cislo],'|' + str(delka[cislo])))
    print((2 - (len(str(cislo)))) * ' ', cislo, '|', '*'*delka[cislo], (max(list(delka.values())) - delka[cislo]) * ' ' , '|', (2 - (len(str(delka[cislo])))) * ' ', delka[cislo])



