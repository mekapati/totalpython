class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player('Mark')
p2 = Player('Steve')
p1.teamName ="g"
p2.ad="13"
print("Name:", p1.name)
print("Team Name:", Player.teamName)
print("Name:", p2.name)
print("Team Name:", p2.ad)
