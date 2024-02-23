class Player:
    new_team=[] 
    def __init__(self, players):
        self.name = players["name"]
        self.age = players["age"]
        self.position = players["position"]
        self.team = players["team"]                                               
        Player.new_team.append(self)    
        
    @classmethod                                                                           
    def team_player (cls):
        for player in cls.new_team :
            print(player.name)


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
player_1=Player(kevin)
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
player_2=Player(jason)
kyrie = {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
player_3=Player(kyrie)

Player.team_player()
# player_jason = ???

print(player_2.name , player_2.age , player_2.position , player_2.team)









