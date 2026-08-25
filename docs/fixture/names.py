# -*- coding: utf-8 -*-
"""Given-name pools.  Every generated (given, family) pair is checked against the
   21,677 real pairs in the Ramallah GEDCOM and resampled on collision, so no
   synthetic person carries the name of a real one."""
import json, io, os

_HERE = os.path.dirname(os.path.abspath(__file__))
REAL_PAIRS = set(json.load(io.open(os.path.join(_HERE,'namecollide.json'))))

# Three generations of naming practice in the diaspora.
ELDER_M = ['Nadeem','Fuad','Jiries','Wadie','Shukri','Tawfiq','Naim','Raja','Habib','Munir',
           'Zaki','Fareed','Nabil','Adib','Salim','Butros','Emile','Iskandar','Rafiq','Jamil']
ELDER_F = ['Widad','Najla','Therese','Mathilde','Adele','Suad','Nuha','Wadad','Salwa','Rima',
           'Yusra','Ilham','Nawal','Alice','Odette','Victoria','Julia','Wafa','Hind','Samira']
MID_M   = ['Ramzi','Sami','Basel','Tarek','Ziad','Rami','Hani','Marwan','Nader','Fadi',
           'Amjad','Issa','Karim','Jad','Elias','Bishara','Nicola','Anton','Gabriel','Michel']
MID_F   = ['Rana','Dima','Reem','Lina','Maha','Sawsan','Hala','Rula','Nisreen','Randa',
           'Carmen','Nadia','Christine','Vera','Leila','Mona','Rania','Yara','Diana','Hanan']
YOUNG_M = ['Zayd','Amir','Jude','Sami','Lucas','Adam','Noah','Kareem','Malik','Tariq',
           'Gabriel','Alexander','Sebastian','Ryan','Julian','Omar','Yousef','Daniel','Leo','Milo']
YOUNG_F = ['Layla','Maya','Zeina','Nora','Sophia','Amara','Talia','Jana','Celine','Isabel',
           'Salma','Naya','Emilia','Aya','Mira','Lara','Juliette','Nina','Dalia','Rose']
# married-in spouses: not of Ramallah descent, so a wider pool and a non-roster surname
OUTSIDE_M = ['Peter','Marcus','Daniel','Andre','Stefan','Thomas','Vincent','Gregory','Colin','Ravi',
             'Hassan','Andrés','Mateo','Ezra','Owen','Devon','Kwame','Ilya','Nikos','Tomás']
OUTSIDE_F = ['Margaret','Beth','Alison','Priya','Grace','Nicole','Erin','Sofia','Hannah','Imani',
             'Katarzyna','Mei','Ana','Rebecca','Josephine','Fiona','Claudia','Noor','Ingrid','Chloe']
OUTSIDE_SURNAMES = ['Whitfield','Okonkwo','Nakamura','Alvarez','Brennan','Kowalski','Petrov','Adeyemi',
                    'Lindqvist','Delacroix','Moreau','Silva','Rossi','Fitzgerald','Kaplan','Ferreira',
                    'Bhattacharya','Novak','Halvorsen','Castellanos','Nguyen','Duarte','Osei','Vasquez']

def pool(sex, birth_year, outside=False):
    if outside:
        return OUTSIDE_M if sex=='M' else OUTSIDE_F
    if birth_year < 1960: return ELDER_M if sex=='M' else ELDER_F
    if birth_year < 1996: return MID_M   if sex=='M' else MID_F
    return YOUNG_M if sex=='M' else YOUNG_F

def collides(given, family):
    return f'{given.lower()}|{family.lower()}' in REAL_PAIRS
