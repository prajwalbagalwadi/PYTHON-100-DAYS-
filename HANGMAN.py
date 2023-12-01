JAI _SHREE _RAM 

# generate a random module
# create  word list
# choose the random word from list 
#replace the word name with ( _ )
#if letter match than  replace (_)with it
# if word match by gussing the word than player won or else lose 

    
import random
lives=6
word=["raj","ram","chandra"]
disp=[]
rnd_word=random.choice(word)
print(rnd_word)
for i in range(len(rnd_word)):
    disp+="_"
print(disp)
game_over=False
while not game_over:
    gusses=input("word gus\n").lower() 
    # postion to replace with letter 
    for pos in range(len(rnd_word)):
        letter=rnd_word[pos]
        if letter==gusses:
            disp[pos]=letter 
    print(disp) 
    if gusses not in rnd_word:
        lives-=1
        if lives==0:
            print("LOOSE")
            print("game_over")
        
    if "_" not in disp:
        game_over= True
        print("WON")
        print("GAME_OVER")
