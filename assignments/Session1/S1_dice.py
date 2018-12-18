#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 23:04:09 2018

@author: nicolasduwavrent
"""

def shuffle(score):
    """
    brief: A user fights against the computer in a dice game, here are the rules
    At the beginning, each player has a null score and the winner is the first obtaining at least 100 points.Participants play in turn but the user always starts.Each player throws a dice as many times as he wants. Stop throws dice before have a '1 to add the thows to your score. '1' does not increase the score.
    Args:
        tab :a list, raise Exception if not
    Returns:
        the score of the game like [['name',score],['Ordi',score]]
    Raises:
        ValueError if input tab is not a list
    """
    if not(isinstance(score, list)):
        raise ValueError('Expected a list as input')
    score=[["J1",0],["Ordi",0]]
    player=0
    jeu=[]
    reponse=''
    while(score[0][1]<=100) and (score[1][1]<=100) and (reponse!='1234'):
        jeu=lance(jeu)
        reponse=''
        print("Vous avez fait "+str(jeu[len(jeu)-1])+"\n")
        if (jeu[len(jeu)-1]==1):
            print ("C'est un 1, dommage "+score[player][0]+" vous ne gagnez pas de points")
            print ("------------------------------------------------------\n")
            jeu=[]
            player=joueur(player)
            reponse=2
        if (reponse==''):
            print ("Joueur :"+ score[player][0])
            print ( score[0][0]+ " : "+str(score[0][1])+ " points")
            print ( score[1][0]+ " : "+str(score[1][1])+ " points")
            display=''
            for i in jeu:
                display=display+str(i)+"  "
            print ("Vos lancers : "+ display)
            print ("Rejouer: Entrer, Stop: 0, Quiter: 1234")
            if (player==0):
                reponse = input()
            else:
                sum=0
                for number in jeu:
                    sum=sum+number
                if (len(jeu)>=random.randint(3,6)) or (sum>=15):
                    reponse='0'
                else:
                    reponse=''
        if (reponse=='0'):
            for i in jeu:
                score[player][1]=score[player][1]+i
            print("Score: "+score[player][0]+" : "+str(score[player][1]))
            print ("------------------------------------------------------")
            print (" ")
            player=joueur(player)
            jeu=[]
    print ("fin")
    return score

def lance(jeu):
    jeu.append(random.randint(1,6))
    return jeu

def joueur(player):
    if (player==0):
        player=1
    else:
        player=0
    return player
