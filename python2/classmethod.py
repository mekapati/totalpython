class Player:
    teamName = 'Zemoso'

    def __init__(self, name="None"):
        self.name = name  

    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName())
obj=Player()
print(obj.getTeamName())
