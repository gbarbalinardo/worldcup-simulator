# -*- coding: UTF-8 -*-
__author__ = 'giuseppe'
import numpy as np
from math import pow
import operator



class Team:
    def __init__(self, name, data):
        self.points = 0
        self.won = 0
        self.lost = 0
        self.drawn = 0
        self.scored = 0
        self.conceded = 0
        self.difference = 0
        self.name = name.lower()
        for result in data:
            if self.name in result[0].lower():
                self.attack = result[1]
                self.defense = result[2]
                break
        if self.attack is None:
            print "error" + name + "is not a team"

    # def __init__(self, name, attack, defense, points):
    #     self.points = points
    #     self.won = 0
    #     self.lost = 0
    #     self.drawn = 0
    #     self.scored = 0
    #     self.conceded = 0
    #     self.difference = 0
    #     self.name = name
    #     self.attack = attack
    #     self.defense = defense

    def displayTeam(self):
        print self.name,"\t(%0.2f," %self.attack,"%0.2f)\t" %self.defense, \
            # "\t Points: ", self.points,\
            # "\t Goal Scored: ", self.scored, "\t Goal conceded: ", self.conceded, "\t Goal Difference: ", self.difference, \
            # "\t Won ", self.won, "\t Lost ", self.lost, "\t Drawn ", self.drawn


class Group:
    def __init__(self, teams):
        self.firstQualified = None
        self.secondQualified = None
        self.teams = teams
        self.reset()
        self.playFirstStage()

    def reset(self):
        for team in self.teams:
            team.points = 0
            team.won = 0
            team.lost = 0
            team.drawn = 0
            team.scored = 0
            team.conceded = 0
            team.difference = 0

    def playFirstStage(self):
        for i in range(0, len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                    Match(self.teams[i], self.teams[j], True)

        # 1 - points
        # 2 - goal difference
        # 3 - goal scored
        # (other factors not considered)
        self.teams = sorted(self.teams, key=operator.attrgetter('points', 'difference', 'scored'))
        self.firstQualified = self.teams[len(self.teams)-1]
        # self.firstQualified.displayTeam()
        # self.firstQualified
        self.secondQualified = self.teams[len(self.teams)-2]
        # self.secondQualified.displayTeam()
        # print "\n"



class Match:
    def __init__(self, team1, team2, isGroup):
        self.team1 = team1
        self.team2 = team2
        self.isGroup = isGroup
        self.winner = None
        self.goalScoredTeam1 = 0
        self.goalScoredTeam2 = 0
        self.playMatch()

    def playMatch(self):
        k = 1
        avgScoredByTeam1 = self.team1.attack / self.team2.defense * k
        avgScoredByTeam2 = self.team2.attack / self.team1.defense * k

        # print "avgScoredByTeamA: " + str(avgScoredByTeam1) + " avgScoredByTeamB: " + str(avgScoredByTeam2)

        while True:
            self.goalScoredTeam1 = np.random.poisson(avgScoredByTeam1)
            self.goalScoredTeam2 = np.random.poisson(avgScoredByTeam2)
            if self.goalScoredTeam1 > self.goalScoredTeam2:
                self.team1.points += 3
                self.team1.won += 1
                self.team2.lost += 1
                self.winner = self.team1
                break
            elif self.goalScoredTeam1 < self.goalScoredTeam2:
                self.team2.points += 3
                self.team2.won += 1
                self.team1.lost += 1
                self.winner = self.team2
                break
                # print "The winner is ", team2.name
            else:
                if self.isGroup is True:
                    self.team1.points += 1
                    self.team2.points += 1
                    self.team1.drawn += 1
                    self.team2.drawn += 1
                    break


        self.team1.scored += self.goalScoredTeam1
        self.team2.scored += self.goalScoredTeam2
        self.team1.conceded += self.goalScoredTeam2
        self.team2.conceded += self.goalScoredTeam1
        self.team1.difference += self.goalScoredTeam1-self.goalScoredTeam2
        self.team2.difference += self.goalScoredTeam2-self.goalScoredTeam1
    def printMatch(self):
        print self.team1.name + " - " + self.team2.name + " : " + str(self.goalScoredTeam1) + " - " + str(self.goalScoredTeam2) #+ (" -> " + self.winner.name if self.winner else "")


def main():

    # TEAM, ATT, DEF
    allResults = [
        ['Brazil', 1.1619160060718503, 1.3240758115969224],
        ['Croatia', 1.0, 1.1125914805779695],
        ['Mexico', 1.0526227019733514, 1.0],
        ['Cameroon', 0.9487265980772475, 1.0838806530305873],
        ['Spain', 1.2185866081969978, 1.2617751923437794],
        ['Netherlands', 1.190082644628099, 1.0555451304184653],
        ['Chile', 0.9741946365322989, 1.0275849127416026],
        ['Australia', 0.8743464327879912, 0.8677050103208857],
        ['Colombia', 1.0, 1.0555451304184653],
        ['Greece', 0.9235958846348457, 1.0555451304184653],
        ["Cote D'Ivoire", 1.0261426884803506, 1.0],
        ['Japan', 0.8502276943835385, 1.0],
        ['Uruguay', 1.1619160060718503, 1.1416776130606119],
        ['Costa Rica', 0.8743464327879912, 0.8423719271908425],
        ['England', 1.1340866925282507, 1.2009757928316755],
        ['Italy', 1.1619160060718503, 1.2009757928316755],
        ['Switzerland', 0.9235958846348457, 1.0838806530305873],
        ['Ecuador', 0.8743464327879912, 0.8423719271908425],
        ['France', 1.1065947039973014, 1.1416776130606119],
        ['Honduras', 0.7125990892224657, 0.8934133983861888],
        ['Argentina', 1.2185866081969978, 1.171139050478514],
        ['Bosnia-Herzegovina', 1.1340866925282507, 0.9727903921936573],
        ['Iran', 0.7798954292460786, 0.4880840683054982],
        ['Nigeria', 0.9235958846348457, 0.8174141489960592],
        ['Germany', 1.190082644628099, 1.2617751923437794],
        ['Portugal', 1.1340866925282507, 1.2009757928316755],
        ['Ghana', 1.0794400404790012, 0.8934133983861888],
        ['USA', 0.9741946365322989, 0.9727903921936573],
        ['Belgium', 1.0794400404790012, 1.171139050478514],
        ['Algeria', 0.9235958846348457, 0.9459560893225746],
        ['Russia', 1.0, 1.1125914805779695],
        ['Korea Republic', 0.9235958846348457, 0.8934133983861888]
    ]

    brazil = Team("BRAZIL", allResults)
    mexico = Team("MEXICO", allResults)
    cameroon = Team("CAMEROON", allResults)
    croatia = Team("CROATIA", allResults)
    netherlands = Team("NETHERLANDS", allResults)
    chile = Team("CHILE", allResults)
    australia = Team("AUSTRALIA", allResults)
    spain = Team("SPAIN", allResults)
    colombia = Team("COLOMBIA", allResults)
    greece = Team("GREECE", allResults)
    cote_divoire = Team("COTE D'IVOIRE", allResults)
    japan = Team("JAPAN", allResults)
    uruguay = Team("URUGUAY", allResults)
    italy = Team("ITALY", allResults)
    england = Team("ENGLAND", allResults)
    costa_rica = Team("COSTA RICA", allResults)
    switzerland = Team("SWITZERLAND", allResults)
    france = Team("FRANCE", allResults)
    ecuador = Team("ECUADOR", allResults)
    honduras = Team("HONDURAS", allResults)
    argentina = Team("ARGENTINA", allResults)
    bosnia_herzegovina = Team("BOSNIA-HERZEGOVINA", allResults)
    iran = Team("IRAN", allResults)
    nigeria = Team("NIGERIA", allResults)
    germany = Team("GERMANY", allResults)
    portugal = Team("PORTUGAL", allResults)
    usa = Team("USA", allResults)
    ghana = Team("GHANA", allResults)
    belgium = Team("BELGIUM", allResults)
    russia = Team("RUSSIA", allResults)
    algeria = Team("ALGERIA", allResults)
    korea_republic = Team("KOREA REPUBLIC", allResults)

    # SINGLE MATCH
    brazil.displayTeam()
    print "\t"
    croatia.displayTeam()
    print "\n"
    winners = {}
    for i in range(0, 10000):
        match = Match(brazil, croatia, False)
        # match.printMatch()
        winner = match.winner
        if winners.has_key(winner.name):
            winners[winner.name] += 1
        else:
            winners[winner.name] = 1
    for key in sorted(winners, key=winners.get, reverse=True):
        print key + ": " + str(winners[key])
    print "\n"

    # FULL WORLD CUP
    winners = {}
    for i in range(0, 10000):
        # Play first stage
        groupA = Group([brazil, mexico, cameroon, croatia])
        groupB = Group([netherlands, chile, australia, spain])
        groupC = Group([colombia, greece, cote_divoire, japan])
        groupD = Group([uruguay, italy, england, costa_rica])
        groupE = Group([switzerland, france, ecuador, honduras])
        groupF = Group([argentina, bosnia_herzegovina, iran, nigeria])
        groupG = Group([germany, portugal, usa, ghana])
        groupH = Group([belgium, russia, algeria, korea_republic])

        # Play second stage
        quarter1 = Match(groupA.firstQualified, groupB.secondQualified, False).winner
        quarter2 = Match(groupC.firstQualified, groupD.secondQualified, False).winner
        quarter3 = Match(groupE.firstQualified, groupF.secondQualified, False).winner
        quarter4 = Match(groupG.firstQualified, groupH.secondQualified, False).winner
        quarter5 = Match(groupB.firstQualified, groupA.secondQualified, False).winner
        quarter6 = Match(groupD.firstQualified, groupC.secondQualified, False).winner
        quarter7 = Match(groupF.firstQualified, groupE.secondQualified, False).winner
        quarter8 = Match(groupH.firstQualified, groupG.secondQualified, False).winner

        # Quarters
        semifinalist1 = Match(quarter1, quarter2, False).winner
        semifinalist2 = Match(quarter3, quarter4, False).winner
        semifinalist3 = Match(quarter5, quarter6, False).winner
        semifinalist4 = Match(quarter7, quarter8, False).winner

        # Semifinals
        finalist1 = Match(semifinalist1, semifinalist2, False).winner
        finalist2 = Match(semifinalist3, semifinalist4, False).winner

        # Final
        winner = Match(finalist1, finalist2, False).winner
        # print winner.displayTeam()

        if winners.has_key(winner.name):
            winners[winner.name] += 1
        else:
            winners[winner.name] = 1


    # print "Result after 12 matches"
    # brazil.displayTeam()
    # italy.displayTeam()

    # winners = sorted(winners.iteritems(), key=operator.itemgetter(1))
    for key in sorted(winners, key=winners.get, reverse=True):
        print key + ": " + str(winners[key])

    #
    # print "\nURUGUAY WINS"
    # for i in range(0, 10000):
    #
    #     italy = Team("ITALY", 1.1, 1, 3)
    #     costa_rica = Team("COSTA RICA", .8, 1, 3)
    #     england = Team("ENGLAND", 1.1, 1, 0)
    #     uruguay = Team("URUGUAY", 1, 1, 3)
    #     Match(italy, costa_rica, True)
    #     Match(italy, uruguay, True)
    #     Match(costa_rica, england, True)
    #
    #     teams = [italy, costa_rica, uruguay, england]
    #     teams = sorted(teams, key=operator.attrgetter('points', 'difference', 'scored'))
    #
    #     if winners.has_key(teams[2].name):
    #         winners[teams[2].name] += 1
    #     else:
    #         winners[teams[2].name] = 1
    #
    # for key in sorted(winners, key=winners.get, reverse=True):
    #     print key + ": " + str(winners[key])
    #
    #
    # print "\nENGLAND WINS"
    # winners = {}
    #
    # for i in range(0, 10000):
    #
    #     italy = Team("ITALY", 1.1, 1, 3)
    #     costa_rica = Team("COSTA RICA", .8, 1, 3)
    #     england = Team("ENGLAND", 1.1, 1, 3)
    #     uruguay = Team("URUGUAY", 1, 1, 0)
    #     Match(italy, costa_rica, True)
    #     Match(italy, uruguay, True)
    #     Match(costa_rica, england, True)
    #
    #     teams = [italy, costa_rica, uruguay, england]
    #     teams = sorted(teams, key=operator.attrgetter('points', 'difference', 'scored'))
    #
    #     if winners.has_key(teams[2].name):
    #         winners[teams[2].name] += 1
    #     else:
    #         winners[teams[2].name] = 1
    #
    # for key in sorted(winners, key=winners.get, reverse=True):
    #     print key + ": " + str(winners[key])
    #
    #
    # print "\nDRAW"
    # winners = {}
    #
    # for i in range(0, 10000):
    #
    #     italy = Team("ITALY", 1.1, 1, 3)
    #     costa_rica = Team("COSTA RICA", .8, 1, 3)
    #     england = Team("ENGLAND", 1.1, 1, 1)
    #     uruguay = Team("URUGUAY", 1, 1, 1)
    #     Match(italy, costa_rica, True)
    #     Match(italy, uruguay, True)
    #     Match(costa_rica, england, True)
    #
    #     teams = [italy, costa_rica, uruguay, england]
    #     teams = sorted(teams, key=operator.attrgetter('points', 'difference', 'scored'))
    #
    #     if winners.has_key(teams[2].name):
    #         winners[teams[2].name] += 1
    #     else:
    #         winners[teams[2].name] = 1
    #
    # for key in sorted(winners, key=winners.get, reverse=True):
    #     print key + ": " + str(winners[key])
    #
if __name__ == '__main__':
    main()