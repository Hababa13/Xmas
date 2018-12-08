import sys
import math

# Help the Christmas elves fetch presents in a magical labyrinth!
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Distance(self,x,y):
        return math.abs(x-self.x)+math.abs(y-self.y)
    def Distance(self,b):
        return math.abs(b.x-self.x)+math.abs(b.y-self.y)
        
class Vector:
    def __init__(self,orig,dest):
        self.orig = a
        self.dest = b
        self.x = b.x - a.x
        self.y = b.y - a.y
    def Norm(self):
        return a.Distance(b)

class TYPE_TOUR:
    PUSH=0
    MOVE=1

class DIR:
    GAUCHE=0
    DROITE=1
    HAUT=2
    BAS=3

class Case:
    
    def __init__(self,tuile=None):
        self.dicoDir = {DIR.HAUT : False,
            DIR.DROITE : False,
            DIR.BAS : False,
            DIR.GAUCHE : False
            }
        if tuile is not None:
            self.SetDir(tuile[0]=='1', tuile[1]=='1',tuile[2]=='1',tuile[3]=='1')
        
    def SetDir(self,up,right,down,left):
        self.dicoDir[DIR.HAUT] = up
        self.dicoDir[DIR.DROITE] = right
        self.dicoDir[DIR.BAS] = down
        self.dicoDir[DIR.GAUCHE] = left
    
class Plateau:
    def __init__(self):
        self.cases = [[Case() for x in range(7)] for y in range(7)]

    def UpdatePlateau(self,tile):
        for y,i in enumerate(tile):
            print >> sys.stderr, i
            for x,j in enumerate(i):
                self.cases[x][y].SetDir(j[0]=='1',
                j[1]=="1",
                j[2]=="1",
                j[3]=="1")
    
    def PushTuile(self,num,direction,tuile):
        caseTempo = cases[:][:]
        if direction==DIR.DROITE:
            for x in reversed.range(6):
                caseTempo[x+1][num] = self.cases[x][num]
            # Ajout de tuile joueur
            caseTempo[0][num] = Case(tuile)
        elif direction==DIR.GAUCHE:
            for x in range(6):
                caseTempo[x][num] = self.cases[x+1][num]
            # Ajout de tuile joueur
            caseTempo[6][num] = Case(tuile)
        elif direction==DIR.HAUT:
            for y in range(6):
                caseTempo[num][y] = self.cases[num][y+1]
            # Ajout de tuile joueur
            caseTempo[num][6] = Case(tuile)
        elif direction==DIR.BAS:
            for y in reversed.range(6):
                caseTempo[num][y+1] = self.cases[num][y]
            # Ajout de tuile joueur
            caseTempo[num][0] = Case(tuile)
        return CaseTempo
        

class QueteCtrl:
    def __init__(self):
        self.listeJ1 = []
        self.listeJ2 = []
        
    def Reset(self):
        self.listeJ1 = []
        self.listeJ2 = []
	
    def Update(self,item_name,item_x,item_y,item_player_id):
        if item_player_id==0:
            self.listeJ1.append(Item(item_name,item_x,item_y))
        else:
            self.listeJ2.append(Item(item_name,item_x,item_y))
    
class Quete:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.listeItem = []
    def Reset(self):
        self.x = 0
        self.y = 0
        self.listeItem.clear()
    def Update(self,item_name,item_x,item_y,item_player_id):
        Reset()
        

class Item:
    def __init__(self,typeItem,x,y):
        self.typeItem = typeItem
        self.x = x
        self.y = y
        self.p = Point(x,y)
    
class Joueur:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.nbQuetes = 0
        self.tuile = ""
        self.p = Point(x,y)
        
    def UpdateJoueur(self,nbQuetes,x,y,tuile):
        self.x = x
        self.y = y
        self.p = Point(x,y)
        self.nbQuetes = nbQuetes
        self.tuile = tuile
    
class STRATEGIE:
    RAPPROCHE=0
    MINMAX = 1
    
class Jeu:
    def __init__(self):
        self.turn_type = TYPE_TOUR.MOVE
        self.plateau = Plateau()
        self.J1 = Joueur()
        self.J2 = Joueur()
        self.queteCtrl = QueteCtrl()
        self.action = ""
        self.strategie = STRATEGIE.RAPPROCHE

    def UpdatePlateau(self,turn_type, tile):
        self.turn_type = turn_type
        self.plateau.UpdatePlateau(tile)
        
    def Action(self):
        return self.action
    
    def UpdateJoueur(self,numJoueur,nbQuetes,x,y,tuile):
        if numJoueur==0:
            self.J1.UpdateJoueur(nbQuetes,x,y,tuile)
        else:
            self.J2.UpdateJoueur(nbQuetes,x,y,tuile)

    def ResetQuete(self):
        self.queteCtrl.Reset()
		
    def UpdateQuete(self,item_name,item_x,item_y,item_player_id):
        self.queteCtrl.Update(item_name,item_x,item_y,item_player_id)
		
    def StrategieRapproche(self):
        if self.turn_type==TYPE_TOUR.PUSH:
            self.StrategieRapprochePush()
        elif self.turn_type==TYPE_TOUR.MOVE:
            self.StrategieRapprocheMove()
        
    def StrategieRapprochePush(self):
        item = queteCtrl.FindNearestItem()
        distance_courante = J1.p.Distance(item.p)
        # Test e, déplacant à gauche
        if J1.p.Distance(Point(max(0,item.x-1))) <distance_courante
        self.action = "PUSH 3 RIGHT"
    
    def StrategieRapprocheMove(self):
        self.action = "PASS"
    
    def StrategieMinimax(self):
        if self.turn_type==TYPE_TOUR.PUSH:
            self.StrategieMinimaxPush()
        elif self.turn_type==TYPE_TOUR.MOVE:
            self.StrategieMinimaxMove()
            
    def StrategieMinimaxPush(self):
        self.action = "PUSH 3 RIGHT"
    
    def StrategieMinimaxMove(self):
        self.action = "PASS"

    def Run(self):
        if self.strategie == STRATEGIE.RAPPROCHE:
            self.StrategieRapproche()
        else:   # MINIMAX
            self.StrategieMinimax()
            
###########################################################
################# MAIN ####################################
###########################################################
# Creation du jeu        
jeu = Jeu()

# game loop
while True:
    turn_type = int(raw_input())
    tile = []
    for i in xrange(7):
        tile.append(raw_input().split())
    jeu.UpdatePlateau(turn_type, tile)
    
    for i in xrange(2):
        # num_player_cards: the total number of quests for a player (hidden and revealed)
        num_player_cards, player_x, player_y, player_tile = raw_input().split()
        num_player_cards = int(num_player_cards)
        player_x = int(player_x)
        player_y = int(player_y)
        jeu.UpdateJoueur(i,num_player_cards,player_x, player_y,player_tile)
    num_items = int(raw_input())  # the total number of items available on board and on player tiles
    jeu.ResetQuete()
    for i in xrange(num_items):
        item_name, item_x, item_y, item_player_id = raw_input().split()
        item_x = int(item_x)
        item_y = int(item_y)
        item_player_id = int(item_player_id)
        jeu.UpdateQuete(item_name,item_x,item_y,item_player_id)
        print >>sys.stderr, item_name, item_x, item_y, item_player_id
		
    num_quests = int(raw_input())  # the total number of revealed quests for both players
    for i in xrange(num_quests):
        quest_item_name, quest_player_id = raw_input().split()
        quest_player_id = int(quest_player_id)
        print >>sys.stderr, quest_item_name, quest_player_id

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    jeu.Run()
    # PUSH <id> <direction> | MOVE <direction> | PASS
    print jeu.Action()