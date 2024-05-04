# -*- coding: utf-8 -*-
import Morpion

class MorpionIA(Morpion.Morpion) :

    def __init__(self) :
        '''MorpionIA hérite des méthodes/attributs de Morpion'''
        Morpion.Morpion.__init__(self)

    def adversaire(self,joueur):
        '''Renvoie le joueur adverse du joueur
        Retour : joueur adeverse (str) -> 'x' ou '.'
        '''
        return {'x' : 'o', 'o' : 'x'}[joueur]

    def evaluationStatique(self):
        '''Evalue la situation du plateau (+10,-10,0, None)

        ** Test **
        >>>obj.setPlateau(['x','.','.','x','.','.','x','.','.'])
        >>>obj.evaluationStatique()
        10
        >>>obj.setPlateau(['o','o','o','x','x','.','x','.','.'])
        >>>obj.evaluationStatique()
        -10
        >>>obj.setPlateau(['o','x','x','x','o','o','o','o','x'])
        >>>obj.evaluationStatique()
        0
        >>>obj.setPlateau(['o','x','.','.','.','.','.','.','o'])
        >>>obj.evaluationStatique()
        >>>
        '''
        if self.analyserPlateau()[0] == True and self.analyserPlateau()[1] == 'x':
            return 10
        elif self.analyserPlateau()[0] == True and self.analyserPlateau()[1] == 'o':
            return -10
        elif self.analyserPlateau()[0] == False and self.plateauComplet() == False:
            return None
        elif self.analyserPlateau()[0] == False :
            return 0

    def evaluerCoup(self, joueur,positionCoup):
        ''' Evalue un nouveau coup
            Paramètres : joueur (str) : 'x' ou 'o'
                         positionCoup (int) : position sur la grille intervalle [0;8]
            retour : evaluation du coup : None, +10 , -10, 0
        '''
        self.jouer(joueur,positionCoup)
        return self.evaluationStatique()


    def minmax(self,joueur):
        '''Identifie le meilleur coup (algo Min_Max)
        Parametre : joueur (str) : 'x', 'o'
        retour : position du meilleur coup (int)

        ** Test **
        >>>obj.setPlateau(['x','x','o','.','o','.','x','.','.'])
        >>>obj.minmax('o')
        (0,3)
        >>>obj.setPlateau(['x','x','o','o','o','.','x','.','.'])
        >>>obj.minmax('x')
        (0,5)


        '''
        scoreBranches = [] #Liste des scores de chaque branche

        for coup in self.coupsRestants():
            score=self.evaluerCoup(joueur,coup)
            if score==None:
                score,_=self.minmax(self.adversaire(joueur))

            scoreBranches.append((score,coup))
            self.jouer('.', coup)  # efface le coup joué

        if joueur=='x' : return max(scoreBranches)
        else : return min(scoreBranches)

obj = MorpionIA()


def Morpion_ia():
    M = MorpionIA()
    while M.plateauComplet() != True:
        a = int(input('Choisis ta case joueur 1'))
        M.jouer('x',a)
        M.afficherPlateau()
        if M.analyserPlateau()[0] == True:
            return ('Le joueur 1 a gagné')
        b = int(input('Choisis ta case joueur 2'))
        M.jouer('o',b)
        M.afficherPlateau()
        if M.analyserPlateau()[0] == True:
            return ('Le joueur 2 a gagné')
        if M.coupsRestants() == [] and M.analyserPlateau() == False:
            return ('Egalité')

def jeux():
    M = MorpionIA()
    choix = int(input('Jouer à deux(press 1) ou contre un ordinateur(press2)'))
    if choix == 1 :
        return MorpionGaming()
    elif choix == 2 :
        while M.plateauComplet() != True or M.analyserPlateau()[0] != True :
            M.afficherPlateau()
            if M.analyserPlateau()[0] == True :
                return 'joueur 2 à gagné'
            print('************')
            case = int(input('Quelle case choisis-tu?'))
            M.jouer('x',case)
            M.afficherPlateau()
            print('************')
            if M.analyserPlateau()[0] == True :
                return 'joueur 1 à gagné'
            if M.plateauComplet() == True :
                return 'égaltité'
            valbot = M.minmax('o')
            M.jouer('o',valbot[1])
        return ('égalité')

