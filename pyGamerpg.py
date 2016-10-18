#!/usr/bin/python
import os,time,random,sys,platform
global player
global OS
OS=platform.system()
def Main():
    Clear()
    e=''
    global player
    yousAb=1
    Name=raw_input("Whats your characters name: ").capitalize()
    player=character(Name)
    while yousAb == 1:
        try:
            print "1.Rogue"
            print "2.Mage"
            inp = raw_input("Choose your class:")
            inp=inp.lower()
            if inp == '1' or inp == 'rogue':
                yousAb=0
                player.Rogue()
                Stat_Distro()
                Game()
            if inp=='2' or inp =='mage':
                player.Mage()
                yousAb=0
                Stat_Distro()
                Game()
        except:
            print "Oops somthing went wrong in Main()"
            print "Unexpected error:", sys.exc_info()[0]
            time.sleep(1)
def AbiDistro():
    pass
def Stat_Distro():
    global player
    global OS
    finished = 0
    correct = 1
    e=''
    StatList=['','health','mana','inteligence','strength','defence','dexterity','agility']
    StatDic={'health':'player.hp','mana':'player.m','inteligence':'player.int','strength':'player.str',\
    'defence':'player.de','dexterity':'player.dex','agility':'player.agi'}
    while finished ==0:
        Clear()
        print
        print "You have",player.sp,"sp left to spend"
        print
        print
        print "Stats:"
        print "1.Health:",player.hp
        print "2.Mana:",player.m
        print "3.Inteligence:",player.int
        print "4.Strength:",player.str
        print "5.Defence:",player.de
        print "6.Dexterity:",player.dex
        print "7.Agility:",player.agi
        print "8.Reset all allocated points"
        print "9.Done"
        try:
            inp=raw_input("What do you want to put points in(ex. 1=Health): ")
            if inp == 'q':
                break
            if inp in StatList and inp !='':
                inp = StatList.index(inp)
            if int(inp) < 8:
                s=StatList[int(inp)]
                statInp=input('How much %s do you wanna add?'%s)
                if statInp >=0 and player.sp>=statInp:
                    player.sp-=statInp
                    exec StatDic[s]+'+=statInp'
            elif int(inp) == 8:
                reset= raw_input("Are you sure you want to reset all stats?(y/n):")
                if reset == 'y':
                    if player.clas=="Rogue":
                        player.Rogue()
                    if player.clas=="Mage":
                        player.Mage()     
                    player.sp = 10
            elif int(inp) == 9:
                done = raw_input("Are you finished editing?(y/n):")
                player.chp=player.hp
                player.cm=player.m
                player.TotDmg()
                finished =1
                break
        except:
            print "Somthing went wrong in Stat_Distro()"
            print "Unexpected error:", sys.exc_info()[0]
            time.sleep(1)
#character class keeps track of all variables relating to
# to the character. variable player is the instance of this class
class character():
    def __init__(self,NewName):
        self.lvl=1
        self.pos=[0][0]
        self.sp=10
        self.name=NewName
        self.items=[]
        self.itemsC=0
        self.inv=[]
        self.invC=0
        self.Equip=[[0 for x in range(3)] for y in range(4)]
        self.exp=0
        self.gold=0
        self.limit=0
    def Rogue(self):
        self.hp=25
        self.chp=25
        self.m=15
        self.cm=15
        self.int=10
        self.str=15
        self.de=10
        self.dex=20
        self.agi=25
        self.TotalDmg=self.str
        self.clas="Rogue"
        self.New_Inv('dagger')
        self.Equipment()
    def Mage(self):
        self.hp=20
        self.chp=20
        self.m=40
        self.cm=40
        self.int=20
        self.str=10
        self.de=8
        self.dex=10
        self.agi=6
        self.TotalDmg=self.str
        self.clas="Mage"
        self.New_Inv('staff')
        self.Equipment()
    def Equipment(self):
        self.Equip[1][2]=self.inv[0]
        self.wep.isequip=1
        self.TotDmg()
    def TotDmg(self):
        self.TotalDmg=self.str+self.Equip[1][2].str
    def New_Inv(self,Type='dagger'):
        self.wep=Wep()
        if Type=='dagger':                
            self.wep.Dagger()
            self.inv.append(self.wep)
        if Type=='staff':
            self.wep.Staff()
            self.inv.append(self.wep)
class Wep():
    def __init__(self):
        self.agi=5.0
        self.dex=5.0
        self.str=3.0
        self.int=4.0
        self.name=''
        self.isequip=0  #testing to check if i can flag an wepon as equiped to player
        self.GlobNames=['of','9000',\
                        'over','oblivion','demon','blood','soaked','diamond']
    def Dagger(self):
        self.type='Dagger'
        self.hand=1
        self.names=['dagger','blade','knife','cutter','stabby','thingy']
        self.Name_Gen()
        self.Stat_Randomazation()
    def Staff(self):
        self.type='Staff'
        self.hand=2
        self.names=['staff','stick','cane','blunt','magical','forever']
        self.Name_Gen()
        self.Stat_Randomazation()
    def Name_Gen(self):
        self.Namerange=random.randint(2,4)
        glo=0
        for counter in range(self.Namerange):
            insrt=random.randint(1,5)
            if insrt <=2 and glo !=1:
                self.name+=random.choice(self.GlobNames)+ " "
                glo=1
            else:
                self.name+=random.choice(self.names)+" "
        self.name=self.name.capitalize()
    def Stat_Randomazation(self):
        multiplierlis = [0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5]
        multiplier=random.choice(multiplierlis)
        stat=player.lvl*multiplier
        self.int+=stat
        self.agi+=stat
        self.dex+=stat
        self.str+=stat
        self.agi*=(random.choice(multiplierlis)+1)
        self.dex*=(random.choice(multiplierlis)+1)
        self.str*=(random.choice(multiplierlis)+1)
        self.int*=(random.choice(multiplierlis)+1)
    def New_Dagger(self):
        pass
class Goblin():
    def __init__(self):
        self.name="Goblin"
        self.lvl=1
        self.sp=10
        self.hp=15
        self.m=10
        self.int=5
        self.str=12
        self.de=9
        self.dex=8
        self.agi=10
        self.stats=['self.hp','self.m','self.int','self.str','self.de','self.dex','self.agi']
        self.Stat_Rand()
    def Stat_Rand(self):
        while self.sp != 0:
            NewStat=random.choice(self.stats)
            exec (NewStat+'+=1')
            self.sp-=1
def Print_Stats():
    Clear()
    #size x
    x=30
    print
    print player.name + " the " + player.clas
    print "Character stats:"
    print "|".ljust(x,'-')+"|"
    print ("|Health: "+str(player.chp)+'/'+str(player.hp)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Mana: "+str(player.cm)+'/'+str(player.m)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Inteligence: "+str(player.int)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Stregth: "+str(player.str)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Defence: "+str(player.de)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Dexterity: "+str(player.dex)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ("|Agility: "+str(player.agi)).ljust(x,' ')+"|"
    print "|".ljust(x,'-')+"|"
    print ('|Skill points to spend:' +str(player.sp)).ljust(x,' ')+'|'
    print "|".ljust(x,'-')+"|"
    print
    lvl=raw_input("press enter to return L to lvl up")
    if lvl == 'L' or lvl == 'l':
        Stat_Distro()
def Print_Inv():
    Clear()
    print ('|'.ljust(59,'-')+'|')#49
    print ('| Inventory'.ljust(59,' ')+'|')#49
    print ('|'.ljust(59,'-')+'|')#49
    print ('| Name'.ljust(43,' ')+'Type'.ljust(16,' ')+'|')#33,16
    print ('|'.ljust(59,'-')+'|')#49
    for x in range(0,len(player.inv)):
        equiped=''
        ln = 40 #30 defult spaces after weapon name. need to suptract 1 if it is  or number is over 9
        if player.inv[x].isequip ==1:
            equiped='*'
            ln-=1
        if x+1 >= 10:
            ln-=1
        print ('|'+str(x+1)+'.'+equiped+player.inv[x].name.ljust(ln,' ')+player.inv[x].type.ljust(16,' ')+'|')#16
        print ('|'.ljust(59,'-')+'|')#49
    usrIn=raw_input('what item do you want to look at(testing, n for new wepon): ')
    if usrIn.isdigit():
        usrIn = int(usrIn)
        usrIn-=1
        if usrIn <= x:
            Clear()
            print 'Name:',player.inv[usrIn].name
            print 'Agi:',player.inv[usrIn].agi
            print 'Dex:',player.inv[usrIn].dex
            print 'Str:',player.inv[usrIn].str
            print
            equip=raw_input("Press enter to exit e to equip:")
            if equip == 'e':
                player.Equip[1][2]=player.inv[usrIn]
                print 'Equiped'
                player.TotalDmg=player.str+player.Equip[1][2].str
                print 'New Total Dmg:',player.TotalDmg
                raw_input("enter to exit")
    elif usrIn == 'n':
        inv=['dagger','staff']
        weps=random.choice(inv)
        player.New_Inv(weps)
        player.invC+=1
        Print_Inv()
def Equipmnt():
    Clear()
    #print (player.Equip)
    #print (player.Equip[1][2].name)
    #need to figureout how to iterate thru the equipment matrix and give each one a name...
    #or make the matrix a dict
    player.equip[0][0]
    x=30
    print
    print player.name + " the " + player.clas
    print "Equipment:"
    print "|".ljust(x,'-')+"|"
    raw_input()
    
    
def Clear():
    global OS
    if OS =='Linux':
        os.system("clear")
    else:
        os.system("cls")
def Fight(go):
    gob=Goblin()
    tmpDef=player.de
    print 'A wild '+ gob.name + ' appeared'
    finished =0
    while finished ==0:
        playerTurn=1
        if player.chp <=0:
            print 'Game Over'
            go=1
            time.sleep(1)
            return go
        if gob.hp <=0:
            player.exp+=5
            print 'you won gained 5 exp'
            time.sleep(1)
            finished = 1
        if player.chp<=player.hp*0.25:
            chance=random.randint(0,10)
            if chance <=3:
                player.limit=1
        while playerTurn==1 and player.chp >=0 and gob.hp>=0:
            print
            print '|'.ljust(14,'-')+'|'
            print ('|HP: '+str(player.chp)+'/'+str(player.hp)).ljust(14,' ')+'|'
            print ('|Mana: '+str(player.cm)+'/'+str(player.m)).ljust(14,' ')+'|'
            print '|'.ljust(14,'-')+'|'
            print '1. Attack'
            print '2. Abilities'
            print '3. Defend'
            print '4. Do nothing'
            print '5. Run like a...'
            if player.limit==1:
                print 'limit avalible'
            print
            inp=raw_input('What do you want to do?(1,2,3,4):').lower()
            if inp =='1' or inp =='attack':
                if player.TotalDmg-gob.de >0:
                    dmg=player.TotalDmg-gob.de
                else:
                    dmg=0
                print 'You struck the '+ gob.name+' for',dmg,'damage'
                gob.hp-=dmg
                playerTurn=0
                time.sleep(1)
            elif inp == '2' or inp =='abilities':
                print 'Abilities:'
                Print_Abilities()
                #playerTurn=0
                time.sleep(1)
            elif inp == '3' or inp == 'defend':
                print 'You take a defensive stance'
                tmpDef+=5
                playerTurn=0
                time.sleep(1)
            elif inp == '4' or inp=='do nothing':
                print 'You stand around and look at flowers'
                playerTurn=0
                time.sleep(1)
            elif inp=='5' or inp=='run like a...':
                run=random.randint(0,100)
                if run <=20:
                    print 'ran away'
                    playerTurn =0
                    finished=1
                    time.sleep(1)
                else:
                    print 'failed to get away'
                    playerTurn=0
                    time.sleep(1)
            else:
                print 'not a choice'
        if finished !=1 and gob.hp>0:
            dmg=abs(tmpDef-gob.str)
            if gob.str-tmpDef >0:
                dmg=gob.str-tmpDef
            else:
                dmg=0
            print gob.name +' hits you for',dmg,'amount of damage'
            player.chp-=dmg
            time.sleep(1)
            tmpDef=player.de
def Print_Abilities():
    print 'Print_abi. function'
def Game():
    e=''
    go=0
    while True:
        Clear()
        if go == 1:
            break
        try:
            print "This is the game"
            print "Press s to view stats"
            print "Press i to view inventory"
            print "Press e to view equipment"
            print 'Press h to heal'
            print "Press f for fight test"
            print "q to quit"
            print
            gmenu=raw_input("What to do?:").lower()
            if gmenu == 's':
                Print_Stats()
            elif gmenu == 'i':
                Print_Inv()
            elif gmenu == 'q':
                print 'Goodbye'
                break
            elif gmenu =='f':
                Clear()
                go=Fight(go)
            elif gmenu == 'h':
                print 'healed'
                player.chp=player.hp
                time.sleep(1)
            elif gmenu =='e':
                Equipmnt()
        except:
            print "Somthings wrong in Game()"
            print "Unexpected error:", sys.exc_info()[0]
            time.sleep(1)
Main()
raw_input("Press enter to exit")
