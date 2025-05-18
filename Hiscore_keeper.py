try:
    file= open("Hiscore.txt", "x+")
except FileExistsError:
    file= open("Hiscore.txt", "r+")
import random
def game():
    print("You are playing a game.....")
    score= random.randint(1, 100)
    print("Your score: ", score)
    return str(score)
file.seek(0)
prev_hiscore= file.read()
score= int(game())
if prev_hiscore== "":
    file.write(str(score))
elif score > int(prev_hiscore):
    file.seek(0)
    file.write(str(score))
file.close()