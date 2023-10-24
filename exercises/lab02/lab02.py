import random as rn

class container:
    class Gracz1:
        def __init__(self, name):
            self.hp = 100
            self.name = name

    class Gracz2:
        def __init__(self, name):
            self.hp = 100
            self.name = name

    team1 = []
    team2 = []

    x = 0

    def __init__(self):
        for i in range(0, 3):
            player1 = input(f"Podaj imie teamu niebieskiego {i}: ")
            self.team1.append(self.Gracz1(player1))
            player2 = input(f"Podaj imie teamu czerwonego {i}: ")
            self.team2.append(self.Gracz2(player2))

    def isDead(self, team):
        for i in team:
            if i.hp <= 0:
                return True
        return False

    def score(self, team):
        for i in team:
            print(f"Player {i.name} has {i.hp} hp")

    def fight(self):
        while(not self.isDead(self.team1) and not self.isDead(self.team2)):
            teamBlue = rn.randint(0, len(self.team1) - 1)
            teamRed = rn.randint(0, len(self.team2) - 1)

            self.team1[teamBlue].hp -= rn.randint(0, 20)
            self.team2[teamRed].hp -= rn.randint(0, 20)

            #print(teamBlue)
            #print(teamRed)

        if self.isDead(self.team1):
            print("Red wins!")
            print("Team Blue")
            self.score(self.team1)
            print("Team Red")
            self.score(self.team2)

        if self.isDead(self.team2):
            print("Blue wins!")
            print("Team Blue")
            self.score(self.team1)
            print("Team Red")
            self.score(self.team2)

con = container()
con.fight()
