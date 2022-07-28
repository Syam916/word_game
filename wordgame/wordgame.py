import random
print('Game instructions are---->')
print('if * is appeard in your guess ,then that letter is correct and in correct position with  word.')
print('if @ is appeard in your guess , then that letter is present in the word but not in correct position with the word.')
print('if ? is appeard in your guess, then that letter is not there in the word.')
name=input('Hey Enter your name: ')
 
print(f'Hey {name} welcome to wordle game!!!')

def checkingGuess(guess,word):
    messege=''
    place=0
    place2=0
    letter2=[]
    let3=[]
    dup=[]
    dup2=[]
    for i in guess:
       if guess.count(i)>1:
           if i not in dup:
               dup.append(i)
    for i in word:
       if word.count(i)>1:
           if i not in dup2:
               dup2.append(i)
    for letter in guess:
        if letter==word[place2]:
            letter2.append(letter)
        place2+=1
    for letter in guess:
        if letter==word[place]:
           
            messege+='*'
        #elif letter in dup and letter in letter2 and letter in let3:
            #messege+='?'
        elif letter not in letter2 and letter in word :
            if letter in dup2 or letter not in let3 :
                let3.append(letter)
                messege+='@'
            else:
                messege+='?'
        else:
            messege+='?'
        place+=1
    print(guess)
    #print(dup)
    #print(dup2)
    print(messege)
    print(f'hey {name}, you have {6-guesses} guesses remaining....')
    return messege=='*****'
word_list=['their']
'''words=open('E:\words.py')
for letter in words:
    word_list.append(letter.strip())'''
word=random.choice(word_list)
print(word)
guesses=0
correct_guess=False
while guesses<6 and not correct_guess:
    guess=input(f'enter a 5 letter word and press enter : ')
    guess=guess.lower()
    if len(guess)!=5:
        print('you need to enter only 5 letters')
        continue
       
    print('your guessed word is :')
    guesses+=1
   
    correct_guess=checkingGuess(guess,word)
if correct_guess:
    print(f'congratulations {name}! you guessed the correct word in {guesses} guesses welldone ')
else:
    print(f'sorry {name}!, you have completed maximum guesses')
    print(f'better luck next time..{name}...the correct word is {word}')
