import csv

Antigens = []
Cell1Panel = []
Cell2Panel = []
Cell3Panel = []
Cell4Panel = []
Cell5Panel = []
Cell6Panel = []
Cell7Panel = []
Cell8Panel = []
Cell9Panel = []
Cell10Panel = []
Cell11Panel = []

with open('RB347.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    print(readCSV)

    for row in readCSV:

        if 'D' in row or 'C' in row:
            Antigens = row

        elif '1' in row:
            Cell1Panel = row
        elif '2' in row:
            Cell2Panel = row
        elif '3' in row:
            Cell3Panel = row
        elif '4' in row:
            Cell4Panel = row
        elif '5' in row:
            Cell5Panel = row
        elif '6' in row:
            Cell6Panel = row
        elif '7' in row:
            Cell7Panel = row
        elif '8' in row:
            Cell8Panel = row
        elif '9' in row:
            Cell9Panel = row
        elif '10' in row:
            Cell10Panel = row
        elif '11' in row:
            Cell11Panel = row

Cell1Data = {}
Cell2Data = {}
Cell3Data = {}
Cell4Data = {}
Cell5Data = {}
Cell6Data = {}
Cell7Data = {}
Cell8Data = {}
Cell9Data = {}
Cell10Data = {}
Cell11Data = {}
Cell1Data = dict(zip(Antigens, Cell1Panel))
Cell1Data.pop('Cell', None)
Cell1Data.pop('RT', None)
# print( Cell1Data )
Cell2Data = dict(zip(Antigens, Cell2Panel))
Cell2Data.pop('Cell', None)
Cell2Data.pop('RT', None)
# print( Cell2Data )
Cell3Data = dict(zip(Antigens, Cell3Panel))
Cell3Data.pop('Cell', None)
Cell3Data.pop('RT', None)
# print( Cell3Data )
Cell4Data = dict(zip(Antigens, Cell4Panel))
Cell4Data.pop('Cell', None)
Cell4Data.pop('RT', None)
# print( Cell4Data )
Cell5Data = dict(zip(Antigens, Cell5Panel))
Cell5Data.pop('Cell', None)
Cell5Data.pop('RT', None)
# print( Cell5Data )
Cell6Data = dict(zip(Antigens, Cell6Panel))
Cell6Data.pop('Cell', None)
Cell6Data.pop('RT', None)
# print( Cell6Data )
Cell7Data = dict(zip(Antigens, Cell7Panel))
Cell7Data.pop('Cell', None)
Cell7Data.pop('RT', None)
# print( Cell7Data )
Cell8Data = dict(zip(Antigens, Cell8Panel))
Cell8Data.pop('Cell', None)
Cell8Data.pop('RT', None)
# print( Cell8Data )
Cell9Data = dict(zip(Antigens, Cell9Panel))
Cell9Data.pop('Cell', None)
Cell9Data.pop('RT', None)
# print( Cell9Data )
Cell10Data = dict(zip(Antigens, Cell10Panel))
Cell10Data.pop('Cell', None)
Cell10Data.pop('RT', None)
# print( Cell10Data )
Cell11Data = dict(zip(Antigens, Cell11Panel))
Cell11Data.pop('Cell', None)
Cell11Data.pop('RT', None)
# print( Cell11Data )

TMQ_1 = Cell1Data
TMQ_2 = Cell2Data
TMQ_3 = Cell3Data
TMQ_4 = Cell4Data
TMQ_5 = Cell5Data
TMQ_6 = Cell6Data
TMQ_7 = Cell7Data
TMQ_8 = Cell8Data
TMQ_9 = Cell9Data
TMQ_10 = Cell10Data
TMQ_11 = Cell11Data

# These are my TMQ values taken from another panel. Commented out so I can pull from Excel instead
"""
TMQ_1= {'D': '+','C': '+','c': '0','E': '0','e': '+','f':'0','V':'0','Cw':'+','K':'0','k':'+','Fya':'0','Fyb':'+','Jka':'+','Jkb':'+',"Lea":'0','Leb':'+','P1':'0','M':'0','N':'+','S':'0','s':'+','Lua':'0','Lub':'+','Xga':'0'}
TMQ_2= {'D': '+','C': '+','c': '0','E': '0','e': '+','f':'0','V':'0','Cw':'0','K':'0','k':'+','Fya':'0','Fyb':'+','Jka':'0','Jkb':'+',"Lea":'0','Leb':'+','P1':'+','M':'+','N':'0','S':'+','s':'0','Lua':'0','Lub':'+','Xga':'+'}
TMQ_3= {'D': '+','C': '0','c': '+','E': '+','e': '0','f':'0','V':'0','Cw':'0','K':'0','k':'+','Fya':'+','Fyb':'+','Jka':'+','Jkb':'0',"Lea":'0','Leb':'+','P1':'+','M':'0','N':'+','S':'0','s':'+','Lua':'0','Lub':'+','Xga':'+'}
TMQ_4= {'D': '0','C': '0','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'+','k':'+','Fya':'+','Fyb':'+','Jka':'+','Jkb':'0',"Lea":'+','Leb':'0','P1':'0','M':'+','N':'+','S':'+','s':'+','Lua':'0','Lub':'+','Xga':'0'}
TMQ_5= {'D': '+','C': '0','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'0','k':'+','Fya':'0','Fyb':'0','Jka':'+','Jkb':'+',"Lea":'0','Leb':'+','P1':'+','M':'0','N':'+','S':'0','s':'0','Lua':'0','Lub':'+','Xga':'0'}
TMQ_6= {'D': '0','C': '0','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'0','k':'+','Fya':'0','Fyb':'0','Jka':'+','Jkb':'0',"Lea":'+','Leb':'0','P1':'0','M':'0','N':'+','S':'0','s':'+','Lua':'0','Lub':'+','Xga':'0'}
TMQ_7= {'D': '0','C': '0','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'0','k':'+','Fya':'+','Fyb':'0','Jka':'+','Jkb':'+',"Lea":'0','Leb':'+','P1':'+','M':'+','N':'0','S':'+','s':'+','Lua':'+','Lub':'+','Xga':'0'}
TMQ_8= {'D': '0','C': '0','c': '+','E': '+','e': '+','f':'+','V':'+','Cw':'0','K':'0','k':'+','Fya':'0','Fyb':'+','Jka':'0','Jkb':'+',"Lea":'0','Leb':'+','P1':'+','M':'+','N':'0','S':'+','s':'0','Lua':'0','Lub':'+','Xga':'0'}
TMQ_9= {'D': '0','C': '0','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'+','k':'0','Fya':'+','Fyb':'0','Jka':'0','Jkb':'+',"Lea":'0','Leb':'+','P1':'0','M':'+','N':'+','S':'0','s':'+','Lua':'0','Lub':'+','Xga':'+'}
TMQ_10= {'D': '0','C': '+','c': '+','E': '0','e': '+','f':'+','V':'0','Cw':'0','K':'0','k':'+','Fya':'+','Fyb':'+','Jka':'+','Jkb':'0',"Lea":'0','Leb':'0','P1':'0','M':'0','N':'+','S':'0','s':'+','Lua':'0','Lub':'+','Xga':'+'}
TMQ_11= {'D': '+','C': '+','c': '0','E': '0','e': '+','f':'0','V':'0','Cw':'0','K':'0','k':'+','Fya':'0','Fyb':'0','Jka':'+','Jkb':'0',"Lea":'0','Leb':'+','P1':'+','M':'+','N':'0','S':'+','s':'+','Lua':'0','Lub':'0','Xga':'+'}
"""
TMQ_AC = []  # Left as a reminder to deal with the AC later. Won't be using as list.
Possible_Antigen = {'D': '', 'C': '', 'c': '', 'E': '', 'e': '', 'f': '', 'V': '', 'Cw': '', 'K': '', 'k': '',
                    'Fya': '', 'Fyb': '', 'Jka': '', 'Jkb': '', "Lea": '', 'Leb': '', 'P1': '', 'M': '', 'N': '',
                    'S': '', 's': '', 'Lua': '', 'Lub': '', 'Xga': '','Jsa':'','Jsb':'',"Kpa":'',"Kpb":''}
Antigen_List = ['D', 'C', 'c', 'E', 'e', 'f', 'V', 'Cw', 'K', 'k', 'Fya', 'Fyb', 'Jka', 'Jkb', 'Lea', 'Leb', 'P1', 'M',
                'N', 'S', 's', 'Lua', 'Lub', 'Xga','Jsa','Jsb','Kpa','Kpb']  # Might be useful eventually
Significant_Antigen_List = ['D', 'C', 'c', 'E', 'e', 'K', 'k', 'Fya', 'Fyb', 'Jka', 'Jkb', 'S', 's', 'Lub',
                            'Xga','Kpb','Jsb']  # Modify to your considerations, all conditionals not included here
Significant_If_Pattern = ['f', 'Cw', 'V', 'Xga', 'Lea', 'Leb', 'M', 'N','Kpa','Jsa',]
Can_Weak_If_Dosage = ['N','S','s','Jka', 'Jkb','M','Fya','Fyb',]
Consider_If_Pattern = []  # Empty list saved here for use later
Consider_If_Warm = []
AntigenScoreList = []
HalfCross_Antigen = []
Significant_If_Warm = ["M"]
Probable_Antigen = []
MostProbable_Antigen = []
Excluded_antigen = []
Antigen_Score = []
AntigenScorePerfect = []
PerfectCount = 0
PossibleDosage = []
Score = 0
Kscore = 0  # Tracks K antigen. If it reaches 2 heterozygous cells K is removed from possible antigen list.
P1score = 0  # Tracks P1 antigen. If 3 negative reactions for p1 occur it is removed from possible antigne list.
TMQ_1_Res = input("Enter 1 if Cell_1 reacted, enter 0 if not: ")

if TMQ_1['D'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_1['C'] == '+' and TMQ_1['c'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_1['c'] == '+' and TMQ_1['C'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_1['E'] == '+' and TMQ_1['e'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_1['e'] == '+' and TMQ_1['E'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_1['f'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_1['V'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_1['Cw'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_1['K'] == '+' and TMQ_1['k'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_1['k'] == '+' and TMQ_1['K'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_1['K'] == '+' and TMQ_1['k'] == '+' and TMQ_1_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_1['Jka'] == '+' and TMQ_1['Jkb'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_1['Jkb'] == '+' and TMQ_1['Jka'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_1['Fya'] == '+' and TMQ_1['Fyb'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_1['Fyb'] == '+' and TMQ_1['Fya'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_1['Lea'] == '+' and TMQ_1_Res == '0':  # and TMQ_1['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_1['Leb'] == '+' and TMQ_1_Res == '0':  # and TMQ_1['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_1['P1'] == '+' and TMQ_1_Res == '0':
    P1score = P1score + 1
    if P1score >= 3:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_1['M'] == '+' and TMQ_1['N'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_1['N'] == '+' and TMQ_1['M'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_1['S'] == '+' and TMQ_1['s'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_1['s'] == '+' and TMQ_1['S'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_1['Lua'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_1['Lub'] == '+' and TMQ_1['Lua'] == '0' and TMQ_1_Res == '0':
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_1['Xga'] == '+' and TMQ_1_Res == '0':
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
#Recently added antibodies are below
if TMQ_1['Kpb'] == '+' and TMQ_1['Kpa'] == '0' and TMQ_1_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_1['Kpa'] == '+' and TMQ_1_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_1['Jsa'] == '+' and TMQ_1_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_1['Jsb'] == '+' and TMQ_1_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']
    # print(Possible_Antigen)


### Second Cell Begins
TMQ_2_Res = input("Enter 1 if Cell_2 reacted, enter 0 if not: ")
if TMQ_2[
    'D'] == '+' and TMQ_2_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_2['C'] == '+' and TMQ_2['c'] == '0' and TMQ_2_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_2['c'] == '+' and TMQ_2['C'] == '0' and TMQ_2_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_2['E'] == '+' and TMQ_2['e'] == '0' and TMQ_2_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_2['e'] == '+' and TMQ_2['E'] == '0' and TMQ_2_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_2['f'] == '+' and TMQ_2_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_2['V'] == '+' and TMQ_2_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_2['Cw'] == '+' and TMQ_2_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_2['K'] == '+' and TMQ_2['k'] == '0' and TMQ_2_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_2['k'] == '+' and TMQ_2['K'] == '0' and TMQ_2_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_2['K'] == '+' and TMQ_2['k'] == '+' and TMQ_2_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_2['Jka'] == '+' and TMQ_2['Jkb'] == '0' and TMQ_2_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_2['Jkb'] == '+' and TMQ_2['Jka'] == '0' and TMQ_2_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_2['Fya'] == '+' and TMQ_2['Fyb'] == '0' and TMQ_2_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_2['Fyb'] == '+' and TMQ_2['Fya'] == '0' and TMQ_2_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_2[
    'Lea'] == '+' and TMQ_2_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_2['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_2[
    'Leb'] == '+' and TMQ_2_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_2['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_2['P1'] == '+' and TMQ_2_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_2['M'] == '+' and TMQ_2['N'] == '0' and TMQ_2_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_2['N'] == '+' and TMQ_2['M'] == '0' and TMQ_2_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_2['S'] == '+' and TMQ_2['s'] == '0' and TMQ_2_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_2['s'] == '+' and TMQ_2['S'] == '0' and TMQ_2_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_2['Lua'] == '+' and TMQ_2_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_2['Lub'] == '+' and TMQ_2['Lua'] == '0' and TMQ_2_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_2['Xga'] == '+' and TMQ_2_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']

if TMQ_2['Kpb'] == '+' and TMQ_2['Kpa'] == '0' and TMQ_2_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_2['Kpa'] == '+' and TMQ_2_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_2['Jsa'] == '+' and TMQ_2_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_2['Jsb'] == '+' and TMQ_2_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']


        # print(Possible_Antigen)
# Cell 3 begins
TMQ_3_Res = input("Enter 1 if Cell_3 reacted, enter 0 if not: ")
if TMQ_3['D'] == '+' and TMQ_3_Res == '0' and 'D' in Possible_Antigen:
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_3['C'] == '+' and TMQ_3['c'] == '0' and TMQ_3_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_3['c'] == '+' and TMQ_3['C'] == '0' and TMQ_3_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_3['E'] == '+' and TMQ_3['e'] == '0' and TMQ_3_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_3['e'] == '+' and TMQ_3['E'] == '0' and TMQ_3_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_3['f'] == '+' and TMQ_3_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_3['V'] == '+' and TMQ_3_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_3['Cw'] == '+' and TMQ_3_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_3['K'] == '+' and TMQ_3['k'] == '0' and TMQ_3_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_3['k'] == '+' and TMQ_3['K'] == '0' and TMQ_3_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_3['K'] == '+' and TMQ_3['k'] == '+' and TMQ_3_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_3['Jka'] == '+' and TMQ_3['Jkb'] == '0' and TMQ_3_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_3['Jkb'] == '+' and TMQ_3['Jka'] == '0' and TMQ_3_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_3['Fya'] == '+' and TMQ_3['Fyb'] == '0' and TMQ_3_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_3['Fyb'] == '+' and TMQ_3['Fya'] == '0' and TMQ_3_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_3[
    'Lea'] == '+' and TMQ_3_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_3['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_3[
    'Leb'] == '+' and TMQ_3_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_3['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_3['P1'] == '+' and TMQ_3_Res == '0' and 'P1' in Possible_Antigen:
    P1score = P1score + 1
    if P1score >= 3:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_3['M'] == '+' and TMQ_3['N'] == '0' and TMQ_3_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_3['N'] == '+' and TMQ_3['M'] == '0' and TMQ_3_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_3['S'] == '+' and TMQ_3['s'] == '0' and TMQ_3_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_3['s'] == '+' and TMQ_3['S'] == '0' and TMQ_3_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_3['Lua'] == '+' and TMQ_3_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_3['Lub'] == '+' and TMQ_3['Lua'] == '0' and TMQ_3_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_3['Xga'] == '+' and TMQ_3_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
if TMQ_3['Kpb'] == '+' and TMQ_3['Kpa'] == '0' and TMQ_3_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_3['Kpa'] == '+' and TMQ_3_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_3['Jsa'] == '+' and TMQ_3_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_3['Jsb'] == '+' and TMQ_3_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']


    # print(Possible_Antigen)

# Cell 4 begins

TMQ_4_Res = input("Enter 1 if Cell_4 reacted, enter 0 if not: ")
if TMQ_4[
    'D'] == '+' and TMQ_4_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_4['C'] == '+' and TMQ_4['c'] == '0' and TMQ_4_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_4['c'] == '+' and TMQ_4['C'] == '0' and TMQ_4_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_4['E'] == '+' and TMQ_4['e'] == '0' and TMQ_4_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_4['e'] == '+' and TMQ_4['E'] == '0' and TMQ_4_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_4['f'] == '+' and TMQ_4_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_4['V'] == '+' and TMQ_4_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_4['Cw'] == '+' and TMQ_4_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_4['K'] == '+' and TMQ_4['k'] == '0' and TMQ_4_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_4['k'] == '+' and TMQ_4['K'] == '0' and TMQ_4_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_4['K'] == '+' and TMQ_4['k'] == '+' and TMQ_4_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_4['Jka'] == '+' and TMQ_4['Jkb'] == '0' and TMQ_4_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_4['Jkb'] == '+' and TMQ_4['Jka'] == '0' and TMQ_4_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_4['Fya'] == '+' and TMQ_4['Fyb'] == '0' and TMQ_4_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_4['Fyb'] == '+' and TMQ_4['Fya'] == '0' and TMQ_4_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_4[
    'Lea'] == '+' and TMQ_4_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_4['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_4[
    'Leb'] == '+' and TMQ_4_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_4['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_4['P1'] == '+' and TMQ_4_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_4['M'] == '+' and TMQ_4['N'] == '0' and TMQ_4_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_4['N'] == '+' and TMQ_4['M'] == '0' and TMQ_4_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_4['S'] == '+' and TMQ_4['s'] == '0' and TMQ_4_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_4['s'] == '+' and TMQ_4['S'] == '0' and TMQ_4_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_4['Lua'] == '+' and TMQ_4_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_4['Lub'] == '+' and TMQ_4['Lua'] == '0' and TMQ_4_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_4['Xga'] == '+' and TMQ_4_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_4['Kpb'] == '+' and TMQ_4['Kpa'] == '0' and TMQ_4_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_4['Kpa'] == '+' and TMQ_4_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_4['Jsa'] == '+' and TMQ_4_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_4['Jsb'] == '+' and TMQ_4_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']


# Cell 5 begins
TMQ_5_Res = input("Enter 1 if Cell_5 reacted, enter 0 if not: ")
if TMQ_5[
    'D'] == '+' and TMQ_5_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_5['C'] == '+' and TMQ_5['c'] == '0' and TMQ_5_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_5['c'] == '+' and TMQ_5['C'] == '0' and TMQ_5_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_5['E'] == '+' and TMQ_5['e'] == '0' and TMQ_5_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_5['e'] == '+' and TMQ_5['E'] == '0' and TMQ_5_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_5['f'] == '+' and TMQ_5_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_5['V'] == '+' and TMQ_5_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_5['Cw'] == '+' and TMQ_5_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_5['K'] == '+' and TMQ_5['k'] == '0' and TMQ_5_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_5['k'] == '+' and TMQ_5['K'] == '0' and TMQ_5_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_5['K'] == '+' and TMQ_5['k'] == '+' and TMQ_5_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_5['Jka'] == '+' and TMQ_5['Jkb'] == '0' and TMQ_5_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_5['Jkb'] == '+' and TMQ_5['Jka'] == '0' and TMQ_5_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_5['Fya'] == '+' and TMQ_5['Fyb'] == '0' and TMQ_5_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_5['Fyb'] == '+' and TMQ_5['Fya'] == '0' and TMQ_5_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_5[
    'Lea'] == '+' and TMQ_5_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_5['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_5[
    'Leb'] == '+' and TMQ_5_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_5['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_5['P1'] == '+' and TMQ_5_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_5['M'] == '+' and TMQ_5['N'] == '0' and TMQ_5_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_5['N'] == '+' and TMQ_5['M'] == '0' and TMQ_5_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_5['S'] == '+' and TMQ_5['s'] == '0' and TMQ_5_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_5['s'] == '+' and TMQ_5['S'] == '0' and TMQ_5_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_5['Lua'] == '+' and TMQ_5_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_5['Lub'] == '+' and TMQ_5['Lua'] == '0' and TMQ_5_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_5['Xga'] == '+' and TMQ_5_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_5['Kpb'] == '+' and TMQ_5['Kpa'] == '0' and TMQ_5_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_5['Kpa'] == '+' and TMQ_5_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_5['Jsa'] == '+' and TMQ_5_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_5['Jsb'] == '+' and TMQ_5_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 6 begins
TMQ_6_Res = input("Enter 1 if Cell_6 reacted, enter 0 if not: ")
if TMQ_6[
    'D'] == '+' and TMQ_6_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_6['C'] == '+' and TMQ_6['c'] == '0' and TMQ_6_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_6['c'] == '+' and TMQ_6['C'] == '0' and TMQ_6_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_6['E'] == '+' and TMQ_6['e'] == '0' and TMQ_6_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_6['e'] == '+' and TMQ_6['E'] == '0' and TMQ_6_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_6['f'] == '+' and TMQ_6_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_6['V'] == '+' and TMQ_6_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_6['Cw'] == '+' and TMQ_6_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_6['K'] == '+' and TMQ_6['k'] == '0' and TMQ_6_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_6['k'] == '+' and TMQ_6['K'] == '0' and TMQ_6_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_6['K'] == '+' and TMQ_6['k'] == '+' and TMQ_6_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_6['Jka'] == '+' and TMQ_6['Jkb'] == '0' and TMQ_6_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_6['Jkb'] == '+' and TMQ_6['Jka'] == '0' and TMQ_6_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_6['Fya'] == '+' and TMQ_6['Fyb'] == '0' and TMQ_6_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_6['Fyb'] == '+' and TMQ_6['Fya'] == '0' and TMQ_6_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_6[
    'Lea'] == '+' and TMQ_6_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_6['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_6[
    'Leb'] == '+' and TMQ_6_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_6['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_6['P1'] == '+' and TMQ_6_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_6['M'] == '+' and TMQ_6['N'] == '0' and TMQ_6_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_6['N'] == '+' and TMQ_6['M'] == '0' and TMQ_6_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_6['S'] == '+' and TMQ_6['s'] == '0' and TMQ_6_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_6['s'] == '+' and TMQ_6['S'] == '0' and TMQ_6_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_6['Lua'] == '+' and TMQ_6_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_6['Lub'] == '+' and TMQ_6['Lua'] == '0' and TMQ_6_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_6['Xga'] == '+' and TMQ_6_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_6['Kpb'] == '+' and TMQ_6['Kpa'] == '0' and TMQ_6_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_6['Kpa'] == '+' and TMQ_6_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_6['Jsa'] == '+' and TMQ_6_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_6['Jsb'] == '+' and TMQ_6_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 7 begins
TMQ_7_Res = input("Enter 1 if Cell_7 reacted, enter 0 if not: ")
if TMQ_7[
    'D'] == '+' and TMQ_7_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_7['C'] == '+' and TMQ_7['c'] == '0' and TMQ_7_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_7['c'] == '+' and TMQ_7['C'] == '0' and TMQ_7_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_7['E'] == '+' and TMQ_7['e'] == '0' and TMQ_7_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_7['e'] == '+' and TMQ_7['E'] == '0' and TMQ_7_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_7['f'] == '+' and TMQ_7_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_7['V'] == '+' and TMQ_7_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_7['Cw'] == '+' and TMQ_7_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_7['K'] == '+' and TMQ_7['k'] == '0' and TMQ_7_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_7['k'] == '+' and TMQ_7['K'] == '0' and TMQ_7_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_7['K'] == '+' and TMQ_7['k'] == '+' and TMQ_7_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_7['Jka'] == '+' and TMQ_7['Jkb'] == '0' and TMQ_7_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_7['Jkb'] == '+' and TMQ_7['Jka'] == '0' and TMQ_7_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_7['Fya'] == '+' and TMQ_7['Fyb'] == '0' and TMQ_7_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_7['Fyb'] == '+' and TMQ_7['Fya'] == '0' and TMQ_7_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_7[
    'Lea'] == '+' and TMQ_7_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_7['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_7[
    'Leb'] == '+' and TMQ_7_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_7['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_7['P1'] == '+' and TMQ_7_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_7['M'] == '+' and TMQ_7['N'] == '0' and TMQ_7_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_7['N'] == '+' and TMQ_7['M'] == '0' and TMQ_7_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_7['S'] == '+' and TMQ_7['s'] == '0' and TMQ_7_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_7['s'] == '+' and TMQ_7['S'] == '0' and TMQ_7_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_7['Lua'] == '+' and TMQ_7_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_7['Lub'] == '+' and TMQ_7['Lua'] == '0' and TMQ_7_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_7['Xga'] == '+' and TMQ_7_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_7['Kpb'] == '+' and TMQ_7['Kpa'] == '0' and TMQ_7_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_7['Kpa'] == '+' and TMQ_7_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_7['Jsa'] == '+' and TMQ_7_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_7['Jsb'] == '+' and TMQ_7_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 8 begins
TMQ_8_Res = input("Enter 1 if Cell_8 reacted, enter 0 if not: ")
if TMQ_8[
    'D'] == '+' and TMQ_8_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_8['C'] == '+' and TMQ_8['c'] == '0' and TMQ_8_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_8['c'] == '+' and TMQ_8['C'] == '0' and TMQ_8_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_8['E'] == '+' and TMQ_8['e'] == '0' and TMQ_8_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_8['e'] == '+' and TMQ_8['E'] == '0' and TMQ_8_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_8['f'] == '+' and TMQ_8_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_8['V'] == '+' and TMQ_8_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_8['Cw'] == '+' and TMQ_8_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_8['K'] == '+' and TMQ_8['k'] == '0' and TMQ_8_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_8['k'] == '+' and TMQ_8['K'] == '0' and TMQ_8_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_8['K'] == '+' and TMQ_8['k'] == '+' and TMQ_8_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_8['Jka'] == '+' and TMQ_8['Jkb'] == '0' and TMQ_8_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_8['Jkb'] == '+' and TMQ_8['Jka'] == '0' and TMQ_8_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_8['Fya'] == '+' and TMQ_8['Fyb'] == '0' and TMQ_8_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_8['Fyb'] == '+' and TMQ_8['Fya'] == '0' and TMQ_8_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_8[
    'Lea'] == '+' and TMQ_8_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_8['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_8[
    'Leb'] == '+' and TMQ_8_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_8['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_8['P1'] == '+' and TMQ_8_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_8['M'] == '+' and TMQ_8['N'] == '0' and TMQ_8_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_8['N'] == '+' and TMQ_8['M'] == '0' and TMQ_8_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_8['S'] == '+' and TMQ_8['s'] == '0' and TMQ_8_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_8['s'] == '+' and TMQ_8['S'] == '0' and TMQ_8_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_8['Lua'] == '+' and TMQ_8_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_8['Lub'] == '+' and TMQ_8['Lua'] == '0' and TMQ_8_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_8['Xga'] == '+' and TMQ_8_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_8['Kpb'] == '+' and TMQ_8['Kpa'] == '0' and TMQ_8_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_8['Kpa'] == '+' and TMQ_8_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_8['Jsa'] == '+' and TMQ_8_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_8['Jsb'] == '+' and TMQ_8_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 9 begins
TMQ_9_Res = input("Enter 1 if Cell_9 reacted, enter 0 if not: ")
if TMQ_9['D'] == '+' and TMQ_9_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_9['C'] == '+' and TMQ_9['c'] == '0' and TMQ_9_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_9['c'] == '+' and TMQ_9['C'] == '0' and TMQ_9_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_9['E'] == '+' and TMQ_9['e'] == '0' and TMQ_9_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_9['e'] == '+' and TMQ_9['E'] == '0' and TMQ_9_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_9['f'] == '+' and TMQ_9_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_9['V'] == '+' and TMQ_9_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_9['Cw'] == '+' and TMQ_9_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_9['K'] == '+' and TMQ_9['k'] == '0' and TMQ_9_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_9['k'] == '+' and TMQ_9['K'] == '0' and TMQ_9_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_9['K'] == '+' and TMQ_9['k'] == '+' and TMQ_9_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_9['Jka'] == '+' and TMQ_9['Jkb'] == '0' and TMQ_9_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_9['Jkb'] == '+' and TMQ_9['Jka'] == '0' and TMQ_9_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_9['Fya'] == '+' and TMQ_9['Fyb'] == '0' and TMQ_9_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_9['Fyb'] == '+' and TMQ_9['Fya'] == '0' and TMQ_9_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_9['Lea'] == '+' and TMQ_9_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_9['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_9['Leb'] == '+' and TMQ_9_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_9['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_9['P1'] == '+' and TMQ_9_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_9['M'] == '+' and TMQ_9['N'] == '0' and TMQ_9_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_9['N'] == '+' and TMQ_9['M'] == '0' and TMQ_9_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_9['S'] == '+' and TMQ_9['s'] == '0' and TMQ_9_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_9['s'] == '+' and TMQ_9['S'] == '0' and TMQ_9_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_9['Lua'] == '+' and TMQ_9_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_9['Lub'] == '+' and TMQ_9['Lua'] == '0' and TMQ_9_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_9['Xga'] == '+' and TMQ_9_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_9['Kpb'] == '+' and TMQ_9['Kpa'] == '0' and TMQ_9_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_9['Kpa'] == '+' and TMQ_9_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_9['Jsa'] == '+' and TMQ_9_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_9['Jsb'] == '+' and TMQ_9_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 10 begins
TMQ_10_Res = input("Enter 1 if Cell_10 reacted, enter 0 if not: ")
if TMQ_10[
    'D'] == '+' and TMQ_10_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_10['C'] == '+' and TMQ_10['c'] == '0' and TMQ_10_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_10['c'] == '+' and TMQ_10['C'] == '0' and TMQ_10_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_10['E'] == '+' and TMQ_10['e'] == '0' and TMQ_10_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_10['e'] == '+' and TMQ_10['E'] == '0' and TMQ_10_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_10['f'] == '+' and TMQ_10_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_10['V'] == '+' and TMQ_10_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_10['Cw'] == '+' and TMQ_10_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_10['K'] == '+' and TMQ_10['k'] == '0' and TMQ_10_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_10['k'] == '+' and TMQ_10['K'] == '0' and TMQ_10_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_10['K'] == '+' and TMQ_10['k'] == '+' and TMQ_10_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_10['Jka'] == '+' and TMQ_10['Jkb'] == '0' and TMQ_10_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_10['Jkb'] == '+' and TMQ_10['Jka'] == '0' and TMQ_10_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_10['Fya'] == '+' and TMQ_10['Fyb'] == '0' and TMQ_10_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_10['Fyb'] == '+' and TMQ_10['Fya'] == '0' and TMQ_10_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_10[
    'Lea'] == '+' and TMQ_10_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_10['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_10[
    'Leb'] == '+' and TMQ_10_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_10['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_10['P1'] == '+' and TMQ_10_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_10['M'] == '+' and TMQ_10['N'] == '0' and TMQ_10_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_10['N'] == '+' and TMQ_10['M'] == '0' and TMQ_10_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_10['S'] == '+' and TMQ_10['s'] == '0' and TMQ_10_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_10['s'] == '+' and TMQ_10['S'] == '0' and TMQ_10_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_10['Lua'] == '+' and TMQ_10_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_10['Lub'] == '+' and TMQ_10['Lua'] == '0' and TMQ_10_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_10['Xga'] == '+' and TMQ_10_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_10['Kpb'] == '+' and TMQ_10['Kpa'] == '0' and TMQ_10_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_10['Kpa'] == '+' and TMQ_10_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_10['Jsa'] == '+' and TMQ_10_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_10['Jsb'] == '+' and TMQ_10_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Cell 11 begins
TMQ_11_Res = input("Enter 1 if Cell_11 reacted, enter 0 if not: ")
if TMQ_11[
    'D'] == '+' and TMQ_11_Res == '0' and 'D' in Possible_Antigen:  # The in Possible_Antigen prevents an error when the program tries to delete non existent D.. need to find a better way to do this.
    del Possible_Antigen['D']
    # print(Possible_Antigen)
if TMQ_11['C'] == '+' and TMQ_11['c'] == '0' and TMQ_11_Res == '0' and 'C' in Possible_Antigen:
    del Possible_Antigen['C']
    # print(Possible_Antigen)
if TMQ_11['c'] == '+' and TMQ_11['C'] == '0' and TMQ_11_Res == '0' and 'c' in Possible_Antigen:
    del Possible_Antigen['c']
    # print(Possible_Antigen)
if TMQ_11['E'] == '+' and TMQ_11['e'] == '0' and TMQ_11_Res == '0' and 'E' in Possible_Antigen:
    del Possible_Antigen['E']
    # print(Possible_Antigen)
if TMQ_11['e'] == '+' and TMQ_11['E'] == '0' and TMQ_11_Res == '0' and 'e' in Possible_Antigen:
    del Possible_Antigen['e']
    # print(Possible_Antigen)
if TMQ_11['f'] == '+' and TMQ_11_Res == '0' and 'f' in Possible_Antigen:
    del Possible_Antigen['f']
    # print(Possible_Antigen)
if TMQ_11['V'] == '+' and TMQ_11_Res == '0' and 'V' in Possible_Antigen:
    del Possible_Antigen['V']
    # print(Possible_Antigen)
if TMQ_11['Cw'] == '+' and TMQ_11_Res == '0' and 'Cw' in Possible_Antigen:
    del Possible_Antigen['Cw']
    # print(Possible_Antigen)
if TMQ_11['K'] == '+' and TMQ_11['k'] == '0' and TMQ_11_Res == '0' and 'K' in Possible_Antigen:
    del Possible_Antigen['K']
    # print(Possible_Antigen)
if TMQ_11['k'] == '+' and TMQ_11['K'] == '0' and TMQ_11_Res == '0' and 'k' in Possible_Antigen:
    del Possible_Antigen['k']
    # print(Possible_Antigen)
if TMQ_11['K'] == '+' and TMQ_11['k'] == '+' and TMQ_11_Res == '0':
    Kscore = Kscore + 1
    if Kscore >= 2 and 'K' in Possible_Antigen:
        del Possible_Antigen['K']
        # print(Kscore)
        # print(Possible_Antigen)
if TMQ_11['Jka'] == '+' and TMQ_11['Jkb'] == '0' and TMQ_11_Res == '0' and 'Jka' in Possible_Antigen:
    del Possible_Antigen['Jka']
    # print(Possible_Antigen)
if TMQ_11['Jkb'] == '+' and TMQ_11['Jka'] == '0' and TMQ_11_Res == '0' and 'Jkb' in Possible_Antigen:
    del Possible_Antigen['Jkb']
    # print(Possible_Antigen)
if TMQ_11['Fya'] == '+' and TMQ_11['Fyb'] == '0' and TMQ_11_Res == '0' and 'Fya' in Possible_Antigen:
    del Possible_Antigen['Fya']
    # print(Possible_Antigen)
if TMQ_11['Fyb'] == '+' and TMQ_11['Fya'] == '0' and TMQ_11_Res == '0' and 'Fyb' in Possible_Antigen:
    del Possible_Antigen['Fyb']
    # print(Possible_Antigen)
if TMQ_11[
    'Lea'] == '+' and TMQ_11_Res == '0' and 'Lea' in Possible_Antigen:  # and TMQ_11['Leb'] == '0' May want to add this depending on rules used
    del Possible_Antigen['Lea']
    # print(Possible_Antigen)
if TMQ_11[
    'Leb'] == '+' and TMQ_11_Res == '0' and 'Leb' in Possible_Antigen:  # and TMQ_11['Lea'] == '0'  May want to add this depending on rules used
    del Possible_Antigen['Leb']
    # print(Possible_Antigen)
if TMQ_11['P1'] == '+' and TMQ_11_Res == '0':
    P1score = P1score + 1
    if P1score >= 3 and 'P1' in Possible_Antigen:
        del Possible_Antigen['P1']
        # print(P1score)
        # print(Possible_Antigen)
if TMQ_11['M'] == '+' and TMQ_11['N'] == '0' and TMQ_11_Res == '0' and 'M' in Possible_Antigen:
    del Possible_Antigen['M']
    # print(Possible_Antigen)
if TMQ_11['N'] == '+' and TMQ_11['M'] == '0' and TMQ_11_Res == '0' and 'N' in Possible_Antigen:
    del Possible_Antigen['N']
    # print(Possible_Antigen)
if TMQ_11['S'] == '+' and TMQ_11['s'] == '0' and TMQ_11_Res == '0' and 'S' in Possible_Antigen:
    del Possible_Antigen['S']
    # print(Possible_Antigen)
if TMQ_11['s'] == '+' and TMQ_11['S'] == '0' and TMQ_11_Res == '0' and 's' in Possible_Antigen:
    del Possible_Antigen['s']
    # print(Possible_Antigen)
if TMQ_11['Lua'] == '+' and TMQ_11_Res == '0' and 'Lua' in Possible_Antigen:
    del Possible_Antigen['Lua']
    # print(Possible_Antigen)
if TMQ_11['Lub'] == '+' and TMQ_11['Lua'] == '0' and TMQ_11_Res == '0' and 'Lub' in Possible_Antigen:
    del Possible_Antigen['Lub']
    # print(Possible_Antigen)
if TMQ_11['Xga'] == '+' and TMQ_11_Res == '0' and 'Xga' in Possible_Antigen:
    del Possible_Antigen['Xga']
    # print(Possible_Antigen)
if TMQ_11['Kpb'] == '+' and TMQ_11['Kpa'] == '0' and TMQ_11_Res == '0' and 'Kpb' in Possible_Antigen:
    del Possible_Antigen['Kpb']
    # print(Possible_Antigen)
if TMQ_11['Kpa'] == '+' and TMQ_11_Res == '0' and 'Kpa' in Possible_Antigen:
    del Possible_Antigen['Kpa']
    # print(Possible_Antigen)
if TMQ_11['Jsa'] == '+' and TMQ_11_Res == '0' and 'Jsa' in Possible_Antigen:
    del Possible_Antigen['Jsa']
    # print(Possible_Antigen)
if TMQ_11['Jsb'] == '+' and TMQ_11_Res == '0' and 'Jsb' in Possible_Antigen:
    del Possible_Antigen['Jsb']

# Designating probable antigens (Based off of the rules I use at my location, so only clinically significant antigens)
for x in Significant_Antigen_List:
    if x in Possible_Antigen:
        Probable_Antigen.append(x)
# Designating existing insignificant antigens that may be considered significant
for x in Significant_If_Pattern:
    if x in Possible_Antigen:
        Consider_If_Pattern.append(x)

MostProbable_Antigen = Probable_Antigen[
                       :]  # For now just appending then later substracting those deemed not most probable
##MostProbableAntigen Formation Begins by removing anything that has a pos heterozygous expression. Feel free to comment this out of your code
for x in Probable_Antigen:
    if TMQ_1[x] == '+' and TMQ_1_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_2[x] == '+' and TMQ_2_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_3[x] == '+' and TMQ_3_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_4[x] == '+' and TMQ_4_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_5[x] == '+' and TMQ_5_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_6[x] == '+' and TMQ_6_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_7[x] == '+' and TMQ_7_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_8[x] == '+' and TMQ_8_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_9[x] == '+' and TMQ_9_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_10[x] == '+' and TMQ_10_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
    if TMQ_11[x] == '+' and TMQ_11_Res == '0' and x in MostProbable_Antigen:
        MostProbable_Antigen.remove(x)
##Determining if antigens fit the pattern or not. Still figuring out a not terrible way of doing this
if TMQ_1_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_2_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_3_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_4_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_5_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_6_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_7_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_8_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_9_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_10_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
if TMQ_11_Res == '1':
    Score = Score + 1  # Using Score to keep track of how many times the antibody reacts
for x in Possible_Antigen:
    if TMQ_1[x] == '+' and TMQ_1_Res == '1':
        Antigen_Score.append(x)
    if TMQ_2[x] == '+' and TMQ_2_Res == '1':
        Antigen_Score.append(x)
    if TMQ_3[x] == '+' and TMQ_3_Res == '1':
        Antigen_Score.append(x)
    if TMQ_4[x] == '+' and TMQ_4_Res == '1':
        Antigen_Score.append(x)
    if TMQ_5[x] == '+' and TMQ_5_Res == '1':
        Antigen_Score.append(x)
    if TMQ_6[x] == '+' and TMQ_6_Res == '1':
        Antigen_Score.append(x)
    if TMQ_7[x] == '+' and TMQ_7_Res == '1':
        Antigen_Score.append(x)
    if TMQ_8[x] == '+' and TMQ_8_Res == '1':
        Antigen_Score.append(x)
    if TMQ_9[x] == '+' and TMQ_9_Res == '1':
        Antigen_Score.append(x)
    if TMQ_10[x] == '+' and TMQ_10_Res == '1':
        Antigen_Score.append(x)
    if TMQ_11[x] == '+' and TMQ_11_Res == '1':
        Antigen_Score.append(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Your possible antigens are: ")
print(Possible_Antigen)
print("Your probable antigens are: ")
print(Probable_Antigen)
print("Your most probable antigens are: ")
print(MostProbable_Antigen)
print("The following antigens should be considered probable if they fit the pattern: ")
print(Consider_If_Pattern)
# Designating existing antigens that might be significant if warm.... might simplify this since it only holds 'm' now
for x in Significant_If_Warm:
    if x in Possible_Antigen:
        Consider_If_Warm.append(x)
        print("The Following Antigen(s) might be significant if reacting at 37C: ")
        print(Consider_If_Warm)

# Determining if the antigen fits the pattern based off of its frequency matching positive  cells
Score = float(Score)
print(Score)
for x in Antigen_Score:
    if Antigen_Score.count(x) >= 0.5 * Score and x not in AntigenScoreList:  # Number used here is highly debatable...
        AntigenScoreList.append(x)
print("The following antigens may be following the pattern significantly: ")
print(AntigenScoreList)
""" #Not sure if I want to include this since p1 isn't important
if 'P1' in Possible_Antigen:
    print("You need " + str(3-P1score) + " more cell(s) to exclude p1")
    """
if 'K' in Possible_Antigen:
    print("You need " + str(2 - Kscore) + " more heterozygous cell(s) or a homozygous cell to exclude K")
if not AntigenScoreList and not MostProbable_Antigen:  # Way of determining that nothing seems to be following pattern signigicantly enough to provide decent confidence
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("There doesn't seem to be any antigens that correlate well with the results. Consider another method of testing, multiple antigens, or antigens not included in panel.")
for x in Antigen_Score:
    if Antigen_Score.count(x) == Score and x not in AntigenScorePerfect:
        AntigenScorePerfect.append(x)
        PerfectCount = 1

if PerfectCount == 1:
    print("The Following antigen(s) are positive in each of the reacting cells: ")
    print(AntigenScorePerfect)

"""
The following code is for assessing dosage that might explain some negative results. There is a better way of assessing it
but that way would require hours and hours of coding. This method basically assumes that if several heterozygous cells
reacted negatively with it, and it wasn't excluded that it might be due to dosage. The number of cells here is set at 2 because one
is a complete guess, and 2 is a bit less of a guess. Obviously a human will still have to inspect the manual panel, but the hint
might be useful in that regard. 
"""
Antigen_NScore= []

for x in Possible_Antigen:
    if TMQ_1[x] == '+' and TMQ_1_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_2[x] == '+' and TMQ_2_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_3[x] == '+' and TMQ_3_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_4[x] == '+' and TMQ_4_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_5[x] == '+' and TMQ_5_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_6[x] == '+' and TMQ_6_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_7[x] == '+' and TMQ_7_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_8[x] == '+' and TMQ_8_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_9[x] == '+' and TMQ_9_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_10[x] == '+' and TMQ_10_Res == '0':
        Antigen_NScore.append(x)
    if TMQ_11[x] == '+' and TMQ_11_Res == '0':
        Antigen_NScore.append(x)

for x in Antigen_NScore:
    if Antigen_NScore.count(x) >= 2 and Antigen_Score.count(x) >= 2 and x in Can_Weak_If_Dosage and x not in PossibleDosage:  # Number used here is highly debatable...
        PossibleDosage.append(x)
if len(PossibleDosage): #If the list contains something, print it.
    print("Based off of the results the following antigen(s) should be checked for dosage that might explain negative reactions:")
    print(PossibleDosage)