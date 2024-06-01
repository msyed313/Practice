import random
min_val=1;max_val=6;maxscore=30
def roll():
    roll=random.randint(min_val,max_val)
    return roll
while True:
        player = input("Enter the number of players who want to play (2-4): ")
        player=int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Invalid number of players. Please enter a number between 2 and 4:3")
players_score=[0 for _ in range(player)]
while max(players_score)<maxscore:
    for playerindx in range((len(players_score))):
        rollit=input("Do you want to rool it (y,n): ").lower()
        if rollit =='y':
            rolldice = roll()
            print("roll =>",rolldice)
            players_score[playerindx] += rolldice
            print(playerindx,"=>",players_score[playerindx])
            while rolldice==6:
                rolldice=roll()
                print("roll =>", rolldice)
                players_score[playerindx] += rolldice
                print(playerindx, "=>", players_score[playerindx])
        else:
            continue
print(players_score)



